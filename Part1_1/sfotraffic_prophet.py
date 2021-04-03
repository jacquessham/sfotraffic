import pandas as pd
import calendar
from sklearn.metrics import mean_squared_error as mse
from prophet import Prophet


# Use monthly data
df = pd.read_csv('../Data/sfopax_month.csv')

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['month_abbr'] = df['month'].apply(lambda x: calendar.month_abbr[x])
df['pax_count'] = df['pax_count']/1000000

X_train = df[df['year']<=2015][['date','pax_count']]
X_test = df[df['year']>2015]

X_train = X_train.rename(columns={'date':'ds', 'pax_count':'y'})
model = Prophet()
model.fit(X_train)

X_test_date = X_test['date']
X_test = X_test.rename(columns={'date':'ds'})

pred = model.predict(X_test)
print(X_test)
print(pred)

fb_rmse = mse(X_test['pax_count'], pred['yhat'])**0.5
print(fb_rmse) #0.2135
