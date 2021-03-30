import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfopax_eda.csv')

# Get sum by type (Depart/Arrival)
df = df.groupby('type').sum().reset_index()
# Change from technical terms to common use terms
df.replace({'Deplaned':'Arrival', 'Enplaned':'Departure',
	            'Thru / Transit':'Transit'})

# Plot Graph
data = [go.Pie(labels=df['type'],values=df['pax_count'],
	           marker=dict(colors=['rgb(0, 204, 102)',
	          	                  'rgb(255, 153, 91)',
	          	                  'rgb(102, 178, 255)']))]
layout = dict(title='Percentage of Airplane Activities')
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='type_pie.html')
