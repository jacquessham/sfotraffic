import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('Results/training_index.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df = df[(df.date>='2008-12-31') & (df.date<='2013-12-31')]

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['date'], y=df['index'],
              mode='lines+markers', name='Monthly Passenger Traffic Index',
              line=dict(color='rgb(102,178,255)')))

## Prepare layout
layout = dict(title={'text':'SFO Month Passenger Traffic',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Index (Base: Jan 2009', gridcolor='lightgray'),
	          legend=dict(x=0.6, y=1, orientation='h'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='training_index.html')