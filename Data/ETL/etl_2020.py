import pandas as pd
from pandas.tseries.offsets import MonthEnd


# Load Data and rename columns
df = pd.read_csv('../Air_Traffic_Passenger_Statistics_2020.csv')
df = df.drop(['Operating Airline','Operating Airline IATA Code'],axis=1)
df = df.rename(columns={'Activity Period':'date',
                        'Published Airline':'pub_airlines',
                        'Published Airline IATA Code':'pub_code',
                        'GEO Summary':'geo_summ', 'GEO Region': 'geo_region',
                        'Activity Type Code':'type',
                        'Price Category Code':'price', 'Terminal': 'terminal',
                        'Boarding Area': 'boarding_area',
                        'Passenger Count': 'pax_count'})

# Data Cleansing
## Inaccurate/uncleaned data need to be fixed
df['pub_airlines'] = df['pub_airlines'].replace('United Airlines - Pre 07/01/2013','United Airlines')
df['pub_airlines'] = df['pub_airlines'].replace('Emirates ','Emirates')
df['pub_airlines'] = df['pub_airlines'].replace('Icelandair (Inactive)','Icelandair')
df['pub_airlines'] = df['pub_airlines'].replace('Icelandair EHF','Icelandair')
df['pub_airlines'] = df['pub_airlines'].replace('Northwest Airlines (became Delta)','Delta Air Lines')
df['price'] = df['price'].replace('Other', 'Full Service')

## Some airlines are wrongly identify in price columns
full_airlines = ['Air China', 'Air India Limited', 'Air New Zealand', 
                 'Air Pacific Limited dba Fiji Airways',
                 'Emirates', 'United Airlines', 'Virgin America', 
                 'Volaris Airlines', 'Delta Air Lines',
                 'US Airways']

for airline in full_airlines:
    df.loc[df.pub_airlines==airline, 'price'] = 'Full Service'

lcc_airlines = ['XL Airways France', 'WOW Air', 'WestJet Airlines', 'Norwegian Air Shuttle ASA']
for airline in lcc_airlines:
    df.loc[df.pub_airlines==airline, 'price'] = 'Low Fare'

## Convert date column to datetime type
df['date'] = pd.to_datetime(df['date'], format='%Y%m') + MonthEnd(1)

# Save the data frame for EDA
df.to_csv('../sfo2020pax_eda.csv', index=False)

# Transform data set to monthly data
df_monthly = df.groupby(['date']).sum().reset_index()
# Change column names
df_monthly = df_monthly.rename(columns={'count':'pax_count'})
df_monthly.to_csv('../sfo2020pax_month.csv', index=False)
