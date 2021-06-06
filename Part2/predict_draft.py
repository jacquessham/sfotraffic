import pandas as pd


df = pd.read_csv('../Data/sfo2020pax_month.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
index_base = df[df['date']=='2008-12-31']['pax_count'].tolist()[0]
df['index'] = df['pax_count']/index_base*100
df.to_csv("temp.csv",index=False)


df_index_range = df[(df['date']>='2008-12-31') & (df['date']<='2012-12-31')]

index_peak = df[df['date']=='2012-12-31']['index'].tolist()[0]
pax_peak = df[df['date']=='2019-12-31']['pax_count'].tolist()[0]
print(index_peak,pax_peak)
pax_last = df[df['date']=='2020-12-31']['pax_count'].tolist()[0]
pax_per_index = (pax_peak-pax_last)/(index_peak-100)


df_pred = pd.DataFrame(df_index_range['index'])
df_pred['date'] = pd.date_range(start='2020-12-31', periods=12*4+1, freq='M')
df_pred['pax_count'] = pax_last+(df_pred['index']-100)*pax_per_index
df_pred.to_csv("prediction.csv", index=False)
print(df[df['date']=='2020-12-31'])