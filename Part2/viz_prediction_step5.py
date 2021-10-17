import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Prepare training data
df = pd.read_csv('../Data/sfo2020pax_month_type.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df_domestic = df[df['geo_type']=='Domestic']
df_intl = df[df['geo_type']=='International']
# Read prediction data
df_pred = pd.read_csv('Results/prediction_step5.csv')
df_pred['date'] = pd.to_datetime(df_pred['date'], format='%Y-%m-%d')

# Create the stacked graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df_domestic['date'], y=df_domestic['pax_count'],
              mode='lines', name='Domestic Passenger Traffic',
              line=dict(color='rgb(0,128,255)')))
data.append(go.Scatter(x=df_intl['date'], y=df_intl['pax_count'],
              mode='lines', name='International Passenger Traffic',
              line=dict(color='rgb(160,160,160)')))
data.append(go.Scatter(x=df_pred['date'],y=df_pred['domestic_prediction'],
              mode='lines', name='Predicted Domestic Passenger Traffic',
              line=dict(color='pink')))
data.append(go.Scatter(x=df_pred['date'],y=df_pred['intl_prediction'],
              mode='lines', name='Predicted International Passenger Traffic',
              line=dict(color='red')))

## Prepare layout for stacked graph
layout = dict(title={'text':'SFO Month Passenger Traffic Prediction',
                     'x':0.5},
              xaxis=dict(title='Date'), 
              yaxis=dict(title='Passenger', gridcolor='lightgray'),
              legend=dict(x=0.1, y=1, orientation='h'),
              plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='pred_step5_viz.html')

# Create the aggregated graph
## Get aggregated training data
df_agg = pd.read_csv('../Data/sfo2020pax_month.csv')
# Aggregate domestic and intl prediction
df_pred['combined_prediction'] = df_pred['domestic_prediction']+df_pred['intl_prediction']
## Prepare Graph
data_agg = []
data_agg.append(go.Scatter(x=df_agg['date'], y=df_agg['pax_count'],
                mode='lines', name='Monthly Passenger Traffic',
                line=dict(color='rgb(102,178,255)')))
data_agg.append(go.Scatter(x=df_pred['date'],
	                       y=df_pred['combined_prediction'],
                mode='lines', name='Predicted Passenger Traffic',
                line=dict(color='red')))

## Prepare layout for stacked graph
layout_agg = dict(title={'text':'SFO Month Passenger Traffic Prediction',
                     'x':0.5},
                  xaxis=dict(title='Date'), 
                  yaxis=dict(title='Passenger', gridcolor='lightgray'),
                  legend=dict(x=0.1, y=1, orientation='h'),
                  plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data_agg, layout=layout_agg)
plotly.offline.plot(fig, filename='pred_step5_viz2.html')
