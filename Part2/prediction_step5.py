import math
import pandas as pd


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
## Find the magitude of each unit of index
domestic_pax_recovered = df_domestic[df_domestic['date']=='2019-12-31']['pax_count'].tolist()[0]
domestic_index_recovered = df_domestic[df_domestic['date']=='2012-12-31']['maindex'].tolist()[0]
domestic_pax_dec2020 = df_domestic[df_domestic['date']=='2020-12-31']['pax_count'].tolist()[0]
domestic_pax_per_index = (domestic_pax_recovered-domestic_pax_dec2020)/(domestic_index_recovered-100)

# Set the data in Dec 2008 as index = 100 and calculate the index
## Now calculate the index for international 
## Calculate passenger index
intl_paxindex_base = df_intl[df_intl['date']=='2008-12-31']['pax_count'].tolist()[0]
df_intl['paxindex'] = df_intl['pax_count']/intl_paxindex_base*100
## Calculate moving average index
intl_maindex_base = df_intl[df_intl['date']=='2008-12-31']['MA'].tolist()[0]
df_intl['maindex'] = df_intl['MA']/intl_maindex_base*100
## Obtain the diff between index and moving average index
df_intl['diffindex'] = df_intl['paxindex'] - df_intl['maindex']
## Find the magitude of each unit of index
intl_pax_recovered = df_intl[df_intl['date']=='2019-12-31']['pax_count'].tolist()[0]
intl_index_recovered = df_intl[df_intl['date']=='2012-12-31']['maindex'].tolist()[0]
intl_pax_dec2020 = df_intl[df_intl['date']=='2020-12-31']['pax_count'].tolist()[0]
intl_pax_per_index = (intl_pax_recovered-intl_pax_dec2020)/(intl_index_recovered-100)

# Find the magitude of each unit of index
## Domestic
domestic_pax_recovered = df_domestic[df_domestic['date']=='2019-12-31']['pax_count'].tolist()[0]
domestic_index_recovered = df_domestic[df_domestic['date']=='2012-12-31']['maindex'].tolist()[0]
domestic_pax_dec2020 = df_domestic[df_domestic['date']=='2020-12-31']['pax_count'].tolist()[0]
domestic_pax_per_index = (domestic_pax_recovered-domestic_pax_dec2020)/(domestic_index_recovered-100)
## International
intl_pax_recovered = df_intl[df_intl['date']=='2019-12-31']['pax_count'].tolist()[0]
intl_index_recovered = df_intl[df_intl['date']=='2012-12-31']['maindex'].tolist()[0]
intl_pax_dec2020 = df_intl[df_intl['date']=='2020-12-31']['pax_count'].tolist()[0]
intl_pax_per_index = (intl_pax_recovered-intl_pax_dec2020)/(intl_index_recovered-100)

# Segment the Recover pred_year
df_domestic_index_range = df_domestic[(df_domestic['date']>='2008-12-31') & (df_domestic['date']<='2012-12-31')]
df_intl_index_range = df_intl[(df_intl['date']>='2008-12-31') & (df_intl['date']<='2012-12-31')]
# Prepare Prediction Dataframe
df_pred = pd.DataFrame(df_domestic_index_range[['date','maindex','diffindex']].rename(columns={'maindex':'domestic_maindex','diffindex':'domestic_diffindex'}))
df_pred = pd.merge(df_pred, df_intl_index_range[['date','maindex','diffindex']].rename(columns={'maindex':'intl_maindex','diffindex':'intl_diffindex'}), how='left', on='date')
df_pred['date'] = pd.date_range(start='2020-12-31', periods=12*4+1, freq='M')
df_pred['year'] = df_pred['date'].dt.year
df_pred['month'] = df_pred['date'].dt.month

# Calculate the predicted trend pax count
## Domestic
df_pred['domestic_raw_prediction'] = domestic_pax_dec2020+(df_pred['domestic_maindex']-100)*domestic_pax_per_index
## International
df_pred['intl_raw_prediction'] = intl_pax_dec2020
for i in range(1,len(df_pred)):
	if df_pred['intl_maindex'].iloc[i] < 100:
		df_pred['intl_raw_prediction'].iloc[i] = intl_pax_dec2020
	else:
		df_pred['intl_raw_prediction'].iloc[i] = intl_pax_dec2020+(df_pred['intl_maindex'].iloc[i]-100)*intl_pax_per_index
# Calculate the final prediction by adjusting with seasonality
## Domestic
df_pred['domestic_prediction'] = df_pred['domestic_raw_prediction']*(1+df_pred['domestic_diffindex']/100)
## International
df_pred['intl_prediction'] = df_pred['intl_raw_prediction']*(1+df_pred['intl_diffindex']/100)

# Export Result
df_pred.to_csv('Results/prediction_step5.csv',index=False)
