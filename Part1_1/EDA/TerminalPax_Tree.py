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
df['year'] = df['date'].dt.year
# Filter and obtain passenger count
df_plot = df[(df['geo_summ']=='Domestic') & (df['year']==df.year.max())]
df_plot = df_plot.groupby(['pub_airlines', 'terminal'])['pax_count'] \
                         .sum().reset_index()
# Filter out outliers
df_plot = df_plot[df_plot['pax_count'] > 10000]
# Add entries for parent node for tree map
df_plot.loc[len(df_plot)+1] = ['Terminal 1', '', 0]
df_plot.loc[len(df_plot)+2] = ['Terminal 2', '', 0]
df_plot.loc[len(df_plot)+3] = ['Terminal 3', '', 0]
df_plot.loc[len(df_plot)+4] = ['International', '', 0]

# Data
data = []
data.append(go.Treemap(labels=df_plot['pub_airlines'],
	                   values=df_plot['pax_count'],
	                   parents=df_plot['terminal']))
# Layout
fig_title = 'Domestic Passenger Traffic by Airline and Terminal'
layout = dict(title={'text':fig_title, 'x': 0.5},
	          treemapcolorway=['rgb(153, 153, 255)','rgb(255, 153, 253)',
	                           'rgb(255, 153, 153)','rgb(255, 204, 153)'])

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='terminalpax_tree.html')
