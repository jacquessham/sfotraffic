import pandas as pd
import calendar
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error as mse


# Use monthly data
df = pd.read_csv('../Data/sfopax_month.csv')

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['month_abbr'] = df['month'].apply(lambda x: calendar.month_abbr[x])
df['pax_count'] = df['pax_count']/1000000

X_train = df[df['year']<=2015]
X_test = df[df['year']>2015]['pax_count'].tolist()

model = ExponentialSmoothing(X_train['pax_count'], trend='add',
		                     seasonal='add', seasonal_periods=12).fit()

model2 = ExponentialSmoothing(X_train['pax_count'], trend='mul',
		                     seasonal='mul', seasonal_periods=12).fit()

pred = model.forecast(24)
hw_rmse = mse(X_test, pred.tolist())**0.5
print(pred)
print(hw_rmse) # 0.2077

pred2 = model2.forecast(24)
hw_rmse2 = mse(X_test, pred2.tolist())**0.5
print(pred2)
print(hw_rmse2) # 0.1037