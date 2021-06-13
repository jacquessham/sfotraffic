import pandas as pd
from pandas.tseries.offsets import MonthEnd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Use monthly data
df = pd.read_csv('../../Data/Air_Traffic_Passenger_Statistics_2020.csv')
df = df.drop(['Operating Airline','Operating Airline IATA Code'],axis=1)
df = df.rename(columns={'Activity Period':'date',
                        'Published Airline':'pub_airlines',
                        'Published Airline IATA Code':'pub_code',
                        'GEO Summary':'geo_summ', 'GEO Region': 'geo_region',
                        'Activity Type Code':'type',
                        'Price Category Code':'price', 'Terminal': 'terminal',
                        'Boarding Area': 'boarding_area',
                        'Passenger Count': 'pax_count'})
## Convert date column to datetime type
df['date'] = pd.to_datetime(df['date'], format='%Y%m')
df['year'] = df['date'].dt.year

df = df.groupby(['date','year','geo_summ']).sum().reset_index()
df_domestic = df[(df['geo_summ']=='Domestic') & (df['year']>2018)]
df_intl = df[(df['geo_summ']=='International') & (df['year']>2018)]


# Create graph
data = []
data.append(go.Bar(x=df_domestic['date'], y=df_domestic['pax_count'],
              name='Domestic Passenger Traffic',
              marker_color='rgb(0,128,255)'))
data.append(go.Bar(x=df_intl['date'], y=df_intl['pax_count'],
              name='International Passenger Traffic',
              marker_color='rgb(160,160,160)'))

## Prepare layout
layout = dict(title={'text':'SFO Monthly Passenger Traffic between 2019-2020',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Passenger (M)', gridcolor='lightgray'),
	          barmode='stack',
	          legend=dict(x=0.6, y=1, orientation='h'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='geo_pax_line.html')
