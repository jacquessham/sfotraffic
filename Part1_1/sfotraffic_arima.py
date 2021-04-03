import pandas as pd
import calendar
import pmdarima as pm
from sklearn.metrics import mean_squared_error as mse


# Use monthly data
df = pd.read_csv('../Data/sfopax_month.csv')

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['month_abbr'] = df['month'].apply(lambda x: calendar.month_abbr[x])
df['pax_count'] = df['pax_count']/1000000

X_train = df[df['year']<=2015]['pax_count']
X_test = df[df['year']>2015]['pax_count'].tolist()
print(X_train)

model = pm.auto_arima(X_train, start_p=1, start_q=1,
                             max_p=6, max_q=6, m=12,
                             max_P=6, max_Q=6, seasonal=True,
                             d=1, D=1, max_d=6, max_D=6, trace=True,
                             error_action='ignore',
                             suppress_warnings=True,
                             stepwise=True)
print(model.summary())
pred = model.predict(24)
pm_rmse = mse(X_test, pred)**0.5
print(pred)
print(pm_rmse) # 0.1340
