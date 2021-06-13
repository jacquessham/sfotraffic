import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../Data/sfo2020pax_month.csv')
df_pred = pd.read_csv('Results/prediction.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df_pred['date'] = pd.to_datetime(df_pred['date'], format='%Y-%m-%d')

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['date'], y=df['pax_count'],
              mode='lines+markers', name='Historical Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))

for volatility in [num/100 for num in range(100,0,-10)]:
       colname = 'pax_count_'+str(volatility)
       data.append(go.Scatter(x=df_pred['date'],y=df_pred[colname],
				  mode='lines+markers',
                              name='Predicted Passenger Traffic (Volatility:'+str(volatility)+')'))

## Prepare layout
layout = dict(title={'text':'SFO Month Passenger Traffic Prediction',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Passenger', gridcolor='lightgray'),
	          legend=dict(x=0.1, y=1, orientation='v'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='pred_multiline.html')
