import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfopax_eda.csv')

# Reformat the data
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
# Filter data to United Airlines
df_plot = df[df['pub_airlines']=='United Airlines']
df_plot = df_plot.groupby(['year', 'month'])['pax_count'] \
                         .sum().reset_index()
df_plot = df_plot[df_plot.year>2005]
print(df_plot)

data = []
data.append(go.Heatmap(z=df_plot.pax_count, x=df_plot.month,
	                   y=df_plot.year, colorscale='ylorrd'))
layout = dict(title='United Ailrines Passenger Traffic',
	          xaxis=dict(tickmode='linear'),
	          yaxis=dict(tickmode='linear'))
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='uapax_heat.html')
