import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import plotly.offline as py


# Load file and rename period and passenger count columns
sfo = pd.read_csv('Air_Traffic_Passenger_Statistics.csv')
sfo.rename(index=str, columns={'Activity Period': 'period', 'Passenger Count':
                               'pax_count'}, inplace=True)
# Sum the passenger count per month and convert back to pandas dataframe
sfo_pax = sfo.groupby('period').pax_count.agg('sum')
sfo_pax = pd.DataFrame(sfo_pax)
sfo_pax['period'] = sfo_pax.index

# Convert to period to datetime type
sfo_pax['date'] = pd.to_datetime(sfo_pax['period'], format='%Y%m')
# sfo_pax = sfo_pax[sfo_pax['date']>datetime(2005,12,31)]

# The date is being datetrunc, convert each month to the last day
sfo_pax['date'] = sfo_pax['date'].apply(lambda x: x + relativedelta(day=31))
sfo_pax = sfo_pax.drop('period', axis = 1)

# Declare Prophet model object
model = Prophet()

# Convert date and pax_count column to ds and y as FB Prophet required
sfo_pax.rename(index=str, columns={'date': 'ds', 'pax_count': 'y'}, inplace=True)

# Divide y by 1 million
sfo_pax['y'] = sfo_pax['y']/1000000

# Split to training and test set
train = sfo_pax[sfo_pax['ds']<datetime(2016,1,1)].reset_index()
test = sfo_pax[sfo_pax['ds']>=datetime(2016,1,1)].reset_index()

# Fit the model
model.fit(train)

# Predict
future = [datetime(2016, 1, 1) + relativedelta(months=i, day=31)
          for i in range(24)]
future = pd.DataFrame(data=future, columns=['ds'])
prediction = model.predict(future)

# Valiadtion
df_val = pd.concat([test, prediction[['ds','yhat']]], axis=1)
df_val['y'] = df_val['y']
df_val['yhat'] = df_val['yhat']
df_val['se'] = (df_val['yhat'] - df_val['y'])**2
rmse = df_val['se'].sum()**(1/2)

# Validation Result
prediction[['ds','yhat']].to_csv('fbprophet_validation.csv', index=False)
print(rmse)

# Plot validation result
fig = plot_plotly(model, prediction)
py.plot(fig, filename='fbprophet_plot.html')

# Predict 2018-2019
future_beyond = [datetime(2016, 1, 1) + relativedelta(months=i, day=31)
                 for i in range(48)]
future_beyond = pd.DataFrame(data=future_beyond, columns=['ds'])
prediction_result = model.predict(future_beyond)
prediction_result[['ds','yhat']].to_csv('fbprophet_result.csv', index=False)
