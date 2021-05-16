import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfo2020pax_month.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Monthly growth rate
df['growth_month'] = df.pax_count.pct_change()
# Calculate moving average
df['growth_ma'] = df.growth_month.rolling(12).mean()

df = df[(df.date>'2007-01-01') & (df.date<'2020-01-01')]
df_temp = df[df.date==df.date.min()]
lowest_growth = df[df.date==df.date.min()]['growth_month'].tolist()[0]
lowest_growthma = df[df.date==df.date.min()]['growth_ma'].tolist()[0]


# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['date'], y=df['growth_month'],
              mode='lines', name='Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))
data.append(go.Scatter(x=df['date'], y=df['growth_ma'],
              mode='lines', name='Passenger Traffic Moving Average',
              line=dict(color='rgb(255,178,102)')))

## Prepare layout
layout = dict(title={'text':'SFO Month Passenger Traffic Growth Rate between 2007-2020',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Growth Rate', gridcolor='lightgray'),
	          legend=dict(x=0.6, y=1, orientation='h'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='annualpax2020_line.html')
