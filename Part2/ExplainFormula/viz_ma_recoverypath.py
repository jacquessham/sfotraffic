import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfo2020pax_month.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# Calculate Moving Average
df['MA'] = df['pax_count'].rolling(12).mean()
index_base = df[df['date']=='2008-12-31']['pax_count'].tolist()[0]
ma_index_base = df[df['date']=='2008-12-31']['MA'].tolist()[0]
df['index'] = df['pax_count']/index_base*100
df['MA_index'] = df['MA']/ma_index_base*100
df = df[(df.date>='2008-12-31') & (df.date<='2013-12-31')]

# Change the date range to string and replace years with Year 1-4
def date2str(row):
	month = row['date'].strftime('%b')
	if row.row_index == 0: 
		year = 0
	elif month == 12: 
		year = int((row.row_index)/12)
	else: 
		year = int((row.row_index)/12)+1
	return f'{month} Year {year}'
df['row_index'] = range(len(df))
df['date_str'] = df.apply(lambda row: date2str(row), axis=1)

# Create graph
## Prepare Graph
data = []
data.append(go.Scatter(x=df['date_str'], y=df['index'],
              mode='lines', name='Monthly Passenger Traffic Index',
              line=dict(color='rgb(102,178,255)')))
data.append(go.Scatter(x=df['date_str'], y=df['MA_index'],
              mode='lines', name='Monthly Passenger Traffic Moving Average Index',
              line=dict(color='rgb(255,178,102)')))

## Prepare layout
layout = dict(title={'text':'SFO Month Passenger Traffic Recovery Path',
                     'x':0.5},
	          xaxis=dict(title='Period', dtick=6), 
	          yaxis=dict(title='Index (Base: Jan 2009', gridcolor='lightgray'),
	          legend=dict(x=0.6, y=1, orientation='h'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='recovery_path.html')
