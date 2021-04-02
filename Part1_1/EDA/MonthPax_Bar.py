import pandas as pd
import calendar
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# Function to reformat number with thousand separator and decimals
def text_reformat(count):
	return f'{count:,.1f}'

# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/sfopax_eda.csv')
# Reformat date columns
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['month'] = df['date'].dt.month
df['month_abbr'] = df['month'].apply(lambda x: calendar.month_abbr[x])

# Average Domestic data, use month in int and abbr, so that sort by month in int
df_domestic = df[df['geo_summ']=='Domestic']
df_domestic = df_domestic.groupby(['month','month_abbr']).mean().reset_index()
# Average intl data, same reason group by 2 cols
df_intl = df[df['geo_summ']=='International']
df_intl = df_intl.groupby(['month','month_abbr']).mean().reset_index()
# Create new columns to format number in text with thousand separator
df_intl['pax_count_text'] = df_intl.pax_count.apply(lambda x: text_reformat(x))
df_domestic['pax_count_text'] = df_domestic.pax_count.apply(lambda x: 
	                                                          text_reformat(x))
# Plots
data = []
data.append(go.Bar(name='International', 
	               x=df_intl.month_abbr, y=df_intl.pax_count,
	               text=df_intl.pax_count_text, textposition='auto',
	               textfont=dict(color='white'),
	               marker=dict(color='rgb(0, 204, 204)')))

data.append(go.Bar(name='Domestic', 
	               x=df_domestic.month_abbr, y=df_domestic.pax_count,
	               text=df_domestic.pax_count_text, textposition='auto',
	               textfont=dict(color='white'),
	               marker=dict(color='rgb(255, 153, 153)')))

# Layouts
layout = dict(title={'text':'Monthly Average Passenger Traffic between 2005-2017',
	                 'x':0.5},
	          barmode='stack', 
	          xaxis=dict(title='Month', tickmode='linear'),
	          yaxis=dict(title='Passenger Traffic',
	          	         tickformat=','),
	          plot_bgcolor='rgba(0,0,0,0)')

fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='monthlypax_bar.html')
