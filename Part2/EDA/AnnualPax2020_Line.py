import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfo2020pax_month.csv')

# Calculate moving average
df['pax_count'] = df['pax_count']/1000000
df['pax_count_ma'] = df.pax_count.rolling(12).mean()
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year
df = df[df['year']>=2007]

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['date'], y=df['pax_count'],
              mode='lines', name='Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))
data.append(go.Scatter(x=df['date'], y=df['pax_count_ma'],
              mode='lines', name='Passenger Traffic Moving Average',
              line=dict(color='rgb(255,178,102)')))

## Prepare layout
layout = dict(title={'text':'SFO Monthly Passenger Traffic between 2007-2020',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Passenger (M)', gridcolor='lightgray'),
	          legend=dict(x=0.05, y=1),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='annualpax2020_line.html')
