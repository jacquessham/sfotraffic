import pandas as pd
import datetime
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Read the file
df = pd.read_csv('../Data/sfo2020pax_month_type.csv')
# Handle the date and year column
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year

# Split data set into domestic and international
df_domestic = df[df['geo_type']=='Domestic']
df_intl = df[df['geo_type']=='International']

# Calculate Moving Average
df_domestic['MA'] = df_domestic['pax_count'].rolling(12).mean()
df_intl['MA'] = df_intl['pax_count'].rolling(12).mean()


# Set the data in Dec 2008 as index = 100 and calculate the index
## Calculate the index for domestic first 
## Calculate passenger index
domestic_paxindex_base = df_domestic[df_domestic['date']=='2008-12-31']['pax_count'].tolist()[0]
df_domestic['paxindex'] = df_domestic['pax_count']/domestic_paxindex_base*100
## Calculate moving average index
domestic_maindex_base = df_domestic[df_domestic['date']=='2008-12-31']['MA'].tolist()[0]
df_domestic['maindex'] = df_domestic['MA']/domestic_maindex_base*100
## Obtain the diff between index and moving average index
df_domestic['diffindex'] = df_domestic['paxindex'] - df_domestic['maindex']

## Now calculate the index for international 
## Calculate passenger index
intl_paxindex_base = df_intl[df_intl['date']=='2008-12-31']['pax_count'].tolist()[0]
df_intl['paxindex'] = df_intl['pax_count']/intl_paxindex_base*100
## Calculate moving average index
intl_maindex_base = df_intl[df_intl['date']=='2008-12-31']['MA'].tolist()[0]
df_intl['maindex'] = df_intl['MA']/intl_maindex_base*100
## Obtain the diff between index and moving average index
df_intl['diffindex'] = df_intl['paxindex'] - df_intl['maindex']

# Calculate Recovery path
df_domestic['recovery_path'] = df_domestic['maindex']*(1+df_domestic['diffindex']/100)
df_intl['recovery_path'] = df_intl['maindex']*(1+df_intl['diffindex']/100)

# Filter the needed date range
df_domestic = df_domestic[(df_domestic['date']>='2008-12-31') & (df_domestic['date']<='2012-12-31')]
df_intl = df_intl[(df_intl['date']>='2008-12-31') & (df_intl['date']<='2012-12-31')]

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
df_domestic['row_index'] = range(len(df_domestic))
df_intl['row_index'] = range(len(df_intl))
df_domestic['date_str'] = df_domestic.apply(lambda row: date2str(row), axis=1)
df_intl['date_str'] = df_intl.apply(lambda row: date2str(row), axis=1)

# Create graph
data = []
data.append(go.Scatter(x=df_domestic['date_str'], y=df_domestic['recovery_path'],
              mode='lines', name='Domestic Passenger Traffic Index',
              line=dict(color='rgb(0,128,255)')))
data.append(go.Scatter(x=df_intl['date_str'], y=df_intl['recovery_path'],
              mode='lines', name='International Passenger Traffic Index',
              line=dict(color='rgb(160,160,160)')))

## Prepare layout
layout = dict(title={'text':'SFO Monthly Passenger Traffic Recovery Path',
                     'x':0.5},
	          xaxis=dict(title='Date',dtick=6), 
	          yaxis=dict(title='Index', gridcolor='lightgray'),
	          legend=dict(x=0.1, y=1, orientation='h'),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename='recovery_path.html')
