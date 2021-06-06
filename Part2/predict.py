import math
import pandas as pd


# Read the file
df = pd.read_csv('../Data/sfo2020pax_month.csv')
# Handle the date and year column
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year
# Set the data in Dec 2008 as index = 100
index_base = df[df['date']=='2008-12-31']['pax_count'].tolist()[0]
df['index'] = df['pax_count']/index_base*100


# Segment the Recover pred_year
df_index_range = df[(df['date']>='2008-12-31') & (df['date']<='2012-12-31')]

# Set parameters for trend and seasonality
pax_recovered = df[df['date']=='2012-12-31']['pax_count'].tolist()[0]
index_recovered = df[df['date']=='2012-12-31']['index'].tolist()[0]
pax_dec2020 = df[df['date']=='2020-12-31']['pax_count'].tolist()[0]
annualpax_per_index = (pax_recovered-pax_dec2020)/(index_recovered-100)

params = {}
pred_year = 2021
for year in df_index_range.year.unique():
	if year != 2008:
		params[pred_year] = {}
		base_date = str(year-1)+'-12-31'
		params[pred_year]['base_index'] = df_index_range[df_index_range['date']==base_date]['index'].tolist()[0]
		last_date = str(year)+'-12-31'
		params[pred_year]['last_index'] = df_index_range[df_index_range['date']==last_date]['index'].tolist()[0]
		params[pred_year]['base_pax_count'] = pax_dec2020 + (params[pred_year]['base_index']-100)*annualpax_per_index
		params[pred_year]['last_pax_count'] = pax_dec2020 + (params[pred_year]['last_index']-100)*annualpax_per_index
		params[pred_year]['monthpax_per_index'] = (params[pred_year]['last_pax_count']-params[pred_year]['base_pax_count'])/(params[pred_year]['last_index']-params[pred_year]['base_index'])
		pred_year += 1


def normalize(row):
	if row['year']==2020: return 100
	year = row['year']
	base_index = params[year]['base_index']
	return row['index']/base_index*100

def predict(row, volatility):
	if row['year'] == 2020: return params[2021]['base_pax_count']
	if row['month'] == 12: 
		return params[row['year']]['last_pax_count']
	growth = (row['annual_index']-100)*params[row['year']]['monthpax_per_index']
	growth_mod = growth*volatility
	return params[row['year']]['base_pax_count'] + growth_mod


df_pred = pd.DataFrame(df_index_range['index'])
df_pred['date'] = pd.date_range(start='2020-12-31', periods=12*4+1, freq='M')
df_pred['year'] = df_pred['date'].dt.year
df_pred['month'] = df_pred['date'].dt.month
df_pred['annual_index'] = df_pred.apply(lambda row: normalize(row),axis=1)
df_pred['pax_count'] = df_pred.apply(lambda row: predict(row,0.2),axis=1)
df_pred.to_csv("prediction.csv",index=False)