import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfopax_eda.csv')

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year


df_xlair = df[df['pub_airlines']=='XL Airways France']
df_xlair = df_xlair.groupby('year').sum().reset_index()

df_wow = df[df['pub_airlines']=='WOW Air']
df_wow = df_wow.groupby('year').sum().reset_index()

df_wj = df[df['pub_airlines']=='WestJet Airlines']
df_wj = df_wj.groupby('year').sum().reset_index()


data = []
data.append(go.Bar(name='XL Airways France', 
                   x=df_xlair['year'], y=df_xlair['pax_count'],
                   text=df_xlair['pax_count'], textposition='auto',
                   textfont=dict(color='gray'),
                   marker=dict(color='rgb(51, 255, 153)')))

data.append(go.Bar(name='Wow Air', 
                   x=df_wow['year'], y=df_wow['pax_count'],
                   text=df_wow['pax_count'], textposition='auto',
                   textfont=dict(color='gray'),
                   marker=dict(color='rgb(255, 255, 153)')))

data.append(go.Bar(name='WestJet Airlines', 
	               x=df_wj['year'], y=df_wj['pax_count'],
	               text=df_wj['pax_count'], textposition='auto',
	               textfont=dict(color='gray'),
	               marker=dict(color='rgb(255, 178, 102)')))

fig_title = 'Annual Passenger Traffic on International Low Cost Carrier'
layout = dict(title={'text':fig_title, 'x':0.5},
              barmode='stack', xaxis=dict(tickmode='linear'),
              plot_bgcolor='rgba(0,0,0,0)')

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='llcpax_bar.html')
