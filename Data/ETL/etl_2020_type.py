import pandas as pd
from pandas.tseries.offsets import MonthEnd


df = pd.read_csv('../Air_Traffic_Passenger_Statistics_2020.csv')
df = df.drop(['Operating Airline','Operating Airline IATA Code'],axis=1)
df = df.rename(columns={'Activity Period':'date',
                        'Published Airline':'pub_airlines',
                        'Published Airline IATA Code':'pub_code',
                        'GEO Summary':'geo_type', 'GEO Region': 'geo_region',
                        'Activity Type Code':'type',
                        'Price Category Code':'price', 'Terminal': 'terminal',
                        'Boarding Area': 'boarding_area',
                        'Passenger Count': 'pax_count'})

## Convert date column to datetime type
df['date'] = pd.to_datetime(df['date'], format='%Y%m') + MonthEnd(1)

df = df.groupby(['date','geo_type']).sum().reset_index()

df.to_csv('../sfo2020pax_month_type.csv', index=False)
