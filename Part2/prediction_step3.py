import math
import pandas as pd


# Read the file
df = pd.read_csv('../Data/sfo2020pax_month.csv')
# Handle the date and year column
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year

# Calculate Moving Average
df['MA'] = df['pax_count'].rolling(12).mean()

# Set the data in Dec 2008 as index = 100 and calculate the index
paxindex_base = df[df['date']=='2008-12-31']['pax_count'].tolist()[0]
df['paxindex'] = df['pax_count']/paxindex_base*100

maindex_base = df[df['date']=='2008-12-31']['MA'].tolist()[0]
df['maindex'] = df['MA']/maindex_base*100

# Obtain the diff between index and moving average index
df['diffindex'] = df['paxindex'] - df['maindex']

# Find the magitude of each unit of index
pax_recovered = df[df['date']=='2019-12-31']['pax_count'].tolist()[0]
index_recovered = df[df['date']=='2012-12-31']['paxindex'].tolist()[0]
pax_dec2020 = df[df['date']=='2020-12-31']['pax_count'].tolist()[0]
pax_per_index = (pax_recovered-pax_dec2020)/(index_recovered-100)

# Segment the Recover pred_year
df_index_range = df[(df['date']>='2008-12-31') & (df['date']<='2012-12-31')]
# Prepare Prediction Dataframe
df_pred = pd.DataFrame(df_index_range[['maindex','diffindex']])
df_pred['date'] = pd.date_range(start='2020-12-31', periods=12*4+1, freq='M')
df_pred['year'] = df_pred['date'].dt.year
df_pred['month'] = df_pred['date'].dt.month
# Calculate the predicted trend pax count
df_pred['raw_prediction'] = pax_dec2020+(df_pred['maindex']-100)*pax_per_index
# Calculate the final prediction by adjusting with seasonality
df_pred['prediction'] = df_pred['raw_prediction']*(1+df_pred['diffindex']/100)

# Export Result
df_pred.to_csv('Results/prediction_step3.csv',index=False)