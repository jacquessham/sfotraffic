import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfo2020pax_month.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
index_base = df[df['date']=='2008-12-31']['pax_count'].tolist()[0]
df['index'] = df['pax_count']/index_base*100
df_index = df[(df.date>='2008-12-31') & (df.date<='2013-12-31')]
indices = df_index['index'].tolist()
lastpax = df.tail(1)['pax_count'].tolist()[0]
pred = [lastpax*(index/100.0) for index in indices]
df_pred = pd.DataFrame()
df_pred['date'] = pd.date_range(start='2020-12-31', periods=12*4+1, freq='M')

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['date'], y=df['pax_count'],
              mode='lines', name='Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))
data.append(go.Scatter(x=df_pred['date'],y=pred,
			  mode='lines', name='Recovery Trench',
              	  line=dict(color='red')))


## Prepare layout
layout = dict(title={'text':'SFO Month Passenger Traffic Recovery Path',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Passenger', gridcolor='lightgray'),
	          legend=dict(x=0.8, y=1, orientation='h'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='recovery_trend.html')
