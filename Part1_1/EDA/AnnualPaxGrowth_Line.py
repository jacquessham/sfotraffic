import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Convert to annual number
df = pd.read_csv('../../Data/sfopax_month.csv')
# Extract year and obtain annual traffic
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year
df = df.groupby('year').sum().reset_index()
df = df[df['year']>2005] # 2005 does not have full year data, drop
# Calculate Growth Rate
df['growth'] = df['pax_count'].pct_change()
df['growth'] = (df['growth']*100).round(2)

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['year'], y=df['growth'],
              mode='lines+markers', name='Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))

## Prepare layout
layout = dict(title='SFO Passenger Traffic Growth Rate',
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Rate (%)'))

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='annualpaxgrowth_line.html')
