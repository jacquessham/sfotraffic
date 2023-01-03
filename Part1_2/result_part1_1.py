import pandas as pd
from pandas.tseries.offsets import MonthEnd
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Import real world data
df_2022 = pd.read_csv('../Data/sfo2022pax_month.csv')
df_2022['date'] = pd.to_datetime(df_2022['date'], format='%Y-%m-%d')
df_2022['year'] = df_2022['date'].dt.year
df_2022['pax_count'] = df_2022['pax_count']/1000000

# Partition data from pre-2018
y_plot = df_2022[df_2022['year']<2020]


# Import prediction
df_pred = pd.read_csv('../Part1_1/Results/sfopred.csv')
# Shift date to end of the month
df_pred['date'] = pd.to_datetime(df_pred['date_str'], format='%b, %Y') + MonthEnd(0)

# Calculate R2 score
y = df_2022[(df_2022['year']>=2018)&(df_2022['year']<=2019)]
y_hat = df_pred[['date','pred']]
r2 = r2_score(y['pax_count'],y_hat['pred'])

# Calculate MSE
mse_result = mse(y['pax_count'],y_hat['pred'])

# Save result
file = open('Prediction_result.txt','w')
file.write('The R2 Score of the prediction with real world data is: ')
file.write(f'{r2:.4f}\n')
file.write('The MSE of the prediction with real world data is: ')
file.write(f'{mse_result:.4f} million passengers\n')
file.close()

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=y_plot['date'], y=y_plot['pax_count'],
              mode='lines', name='Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))
data.append(go.Scatter(x=y_hat['date'],y=y_hat['pred'],
			  mode='lines', name='Predicted Passenger Traffic',
              	  line=dict(color='red')))


## Prepare layout
layout = dict(title={'text':'SFO Month Passenger Traffic Prediction',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Passenger (M)', gridcolor='lightgray'),
	          legend=dict(x=0.6, y=1, orientation='h'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='result_part1_1.html')
