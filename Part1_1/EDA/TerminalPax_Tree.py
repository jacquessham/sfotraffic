import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfopax_eda.csv')

df_plot = df[df['geo_summ']=='Domestic']
df_plot = df_plot.groupby(['pub_airlines', 'terminal'])['pax_count'] \
                         .sum().reset_index()
df_plot = df_plot[df_plot['pax_count'] > 10000] # Filter out outliers
df_plot.loc[len(df_plot)] = ['Terminal 1', '', 0]
df_plot.loc[len(df_plot)+1] = ['Terminal 2', '', 0]
df_plot.loc[len(df_plot)+2] = ['Terminal 3', '', 0]
df_plot.loc[len(df_plot)+3] = ['International', '', 0]
print(df_plot)

data = go.Treemap(labels=df_plot['pub_airlines'],
	              values=df_plot['pax_count'],
	              parents=df_plot['terminal'])

fig_title = 'Domestic Passenger Traffic by Airline and Terminal'
layout = dict(title=fig_title)

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='terminalpax_tree.html')
