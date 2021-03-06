import pandas as pd
from pandas.tseries.offsets import MonthEnd
from sklearn.metrics import mean_squared_error as mse
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Dataframe of real data
df_2020 = pd.read_csv('../Data/sfo2020pax_month.csv')
# Dataframe of prediction
df_pred = pd.read_csv('Results/sfopred.csv')
# Convert original to Million
df_2020['pax_count'] = df_2020['pax_count']/1000000
# Convert date_str to datetime
df_pred['date'] = pd.to_datetime(df_pred['date_str'], format='%b, %Y') + \
                     MonthEnd(1)
# Filter out 2020 data
df_2020['date'] = pd.to_datetime(df_2020['date'], format='%Y-%m-%d')
df_2020['year'] = df_2020['date'].dt.year
df_2020 = df_2020[df_2020['year']<2020]

# Calculate RMSE with real world data
df_pred['year'] = df_pred['date'].dt.year
y_hat = df_pred[(df_pred['year']>2017)&(df_pred['year']<2020)]['pred']
y = df_2020[df_2020['year']>2017]['pax_count']
rmse = mse(y, y_hat)**0.5
# Save the result
file = open('Results/Part1_1compare.txt','w')
file.write('The RMSE of the prediction with real world data is: ')
file.write(f'{rmse:.4f}')
file.close()

# Plot 2020 data and prediction
data = []
data.append(go.Scatter(x=df_2020['date'], y=df_2020['pax_count'],
                       mode='lines', name='Original Data (Downloaded in 2021)',
                       line=dict(color='rgb(160,160,160)')))

data.append(go.Scatter(x=df_pred['date'], y=df_pred['pred'],
                       mode='lines', name='Prediction',
                       line=dict(color='rgb(255,0,0)')))

plot_title = 'SFO Passenger Traffic Prediction '+\
             'between 2018-2019 with Updated Data'
layout = dict(title={'text':plot_title,
                     'x':0.5},
              xaxis=dict(title='Date'), 
              yaxis=dict(title='Passenger (M)', gridcolor='lightgray'),
              legend=dict(x=0.7, y=1, orientation='h'),
              plot_bgcolor='rgba(0,0,0,0)')

fig = go.Figure(data=data, layout=layout)
# Plot chart
plotly.offline.plot(fig, filename='sfopred_2020.html')