import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfopax_month.csv')

# Calculate moving average
df['pax_count_ma'] = df.pax_count.rolling(12).mean()

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['date'], y=df['pax_count'],
              mode='lines+markers', name='Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))
data.append(go.Scatter(x=df['date'], y=df['pax_count_ma'],
              mode='lines', name='Passenger Traffic Moving Average',
              line=dict(color='rgb(255,178,102)')))

## Prepare layout
layout = dict(title='SFO Passenger Traffic',
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Passenger (M)'),
	          legend=dict(x=0.6, y=1, orientation='h'))

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='annualpax_line.html')
