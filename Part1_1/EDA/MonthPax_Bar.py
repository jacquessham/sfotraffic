import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfopax_eda.csv')

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['month'] = df['date'].dt.month



df_domestic = df[df['geo_summ']=='Domestic']
df_domestic = df_domestic.groupby('month').mean().reset_index()

df_intl = df[df['geo_summ']=='International']
df_intl = df_intl.groupby('month').mean().reset_index()

df_intl.pax_count = df_intl.pax_count.round(1)
df_domestic.pax_count = df_domestic.pax_count.round(1)

data = []
data.append(go.Bar(name='International', 
	               x=df_intl.month, y=df_intl.pax_count,
	               text=df_intl.pax_count, textposition='auto',
	               textfont=dict(color='white'),
	               marker=dict(color='rgb(0, 204, 204)')))

data.append(go.Bar(name='Domestic', 
	               x=df_domestic.month, y=df_domestic.pax_count,
	               text=df_domestic.pax_count, textposition='auto',
	               textfont=dict(color='white'),
	               marker=dict(color='rgb(255, 153, 153)')))


layout = dict(title='Monthly Average Passenger Traffic',
	          barmode='stack', xaxis=dict(tickmode='linear'))

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='monthlypax_bar.html')
