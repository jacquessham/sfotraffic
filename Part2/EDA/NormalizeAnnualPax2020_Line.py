import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfo2020pax_month.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')


# Calculate moving average
df['pax_count_ma'] = df.pax_count.rolling(12).mean()

df = df[df.date>'2007-01-01']
df_temp = df[df.date==df.date.min()]
lowest_pax = df[df.date==df.date.min()]['pax_count'].tolist()[0]
lowest_paxma = df[df.date==df.date.min()]['pax_count_ma'].tolist()[0]

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['date'], y=(df['pax_count']/lowest_pax)*100,
              mode='lines+markers', name='Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))
data.append(go.Scatter(x=df['date'], y=(df['pax_count_ma']/lowest_paxma)*100,
              mode='lines', name='Passenger Traffic Moving Average',
              line=dict(color='rgb(255,178,102)')))

## Prepare layout
layout = dict(title={'text':'SFO Month Passenger Traffic between 2007-2020',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Index (Base: Jan, 2007)', gridcolor='lightgray'),
	          legend=dict(x=0.6, y=1, orientation='h'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='annualpax2020_line.html')
