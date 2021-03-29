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

print(df)

df_domestic = df[df['geo_summ']=='Domestic']
df_domestic = df_domestic.groupby('month').mean().reset_index()

df_intl = df[df['geo_summ']=='International']
df_intl = df_intl.groupby('month').mean().reset_index()

print(df_domestic)
print(df_intl)

data = []
data.append(go.Bar(name='International', x=df_intl.month, y=df_intl.pax_count))
data.append(go.Bar(name='Domestic', x=df_domestic.month, y=df_domestic.pax_count))


layout = dict(title='Monthly Average Passenger Traffic',
	          barmode='stack')

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='monthlypax_bar.html')
