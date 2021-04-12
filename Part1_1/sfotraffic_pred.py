import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import plotly
import plotly.graph_objs as go
from plotly.offline import *

# Use monthly data
df = pd.read_csv('../Data/sfopax_month.csv')
# Reformat dataframe
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['year'] = df['date'].dt.year
df['pax_count'] = df['pax_count']/1000000

# Split train/test
X_train = df[df['year']<=2015][['date','pax_count']]

model = ExponentialSmoothing(X_train['pax_count'], trend='mul',
                             seasonal='mul', seasonal_periods=12).fit()

# Prepare date list for data frame
pred_period = 48 # 2016-2019
X_pred_startdate = X_train['date'].max()+ pd.tseries.offsets.MonthEnd(1)
X_pred_enddate = X_train['date'].max()+ pd.tseries.offsets.MonthEnd(pred_period)
X_pred_date = pd.date_range(X_pred_startdate, X_pred_enddate, freq='m')

# Prediction
yhat = model.forecast(pred_period)
pred = pd.DataFrame({'date':X_pred_date, 'pred': yhat})
pred['year'] = pred['date'].dt.year
pred = pred[pred['year']>2017]


# Plot result
# To initiate ploty to run offline
init_notebook_mode(connected=True)

data = []
data.append(go.Scatter(x=df['date'], y=df['pax_count'],
                       mode='lines', name='Original Data',
                       line=dict(color='rgb(160,160,160)')))

data.append(go.Scatter(x=pred['date'], y=pred['pred'],
                       mode='lines', name='Prediction',
                       line=dict(color='rgb(255,0,0)')))

## Prepare layout
layout = dict(title={'text':'SFO Passenger Traffic Prediction between 2018-2019',
                     'x':0.5},
              xaxis=dict(title='Date'), 
              yaxis=dict(title='Passenger (M)', gridcolor='lightgray'),
              legend=dict(x=0.7, y=1, orientation='h'),
              plot_bgcolor='rgba(0,0,0,0)')
# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
# Plot chart
plotly.offline.plot(fig, filename='sfopred.html')

# Reformat Prediction for csv file
pred['date_str'] = pred['date'].dt.strftime('%b, %Y')
pred['pred'] = pred['pred'].round(2)
# Save result in csv
pred[['date_str','pred']].to_csv('Results/sfopred.csv', index=False)
