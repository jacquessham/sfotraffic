import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../Data/sfo2020pax_month.csv')
# Read prediction data
df_pred = pd.read_csv('Results/prediction_step4.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df_pred['date'] = pd.to_datetime(df_pred['date'], format='%Y-%m-%d')
# Filter out data prior to 2007
df = df[df.date>'2007-01-01']

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['date'], y=df['pax_count'],
              mode='lines+markers', name='Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))
data.append(go.Scatter(x=df_pred['date'],y=df_pred['domestic_prediction'],
			  mode='lines+markers', name='Predicted Domestic Passenger Traffic',
              	  line=dict(color='red')))
data.append(go.Scatter(x=df_pred['date'],y=df_pred['intl_prediction'],
			  mode='lines+markers', name='Predicted International Passenger Traffic',
              	  line=dict(color='pink')))

## Prepare layout
layout = dict(title={'text':'SFO Month Passenger Traffic Prediction',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Passenger', gridcolor='lightgray'),
	          legend=dict(x=0.6, y=1, orientation='h'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='pred_step4_viz.html')
