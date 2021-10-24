import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *
from prophet import Prophet


# To initiate ploty to run offline
init_notebook_mode(connected=True)

# Load dataset
df = pd.read_csv('../Data/sfo2020pax_month.csv')
# Rename columns to fit prophet
X_train = df[['date','pax_count']]
X_train = X_train.rename(columns={'date':'ds', 'pax_count':'y'})

# Declare model object
model = Prophet()
model.fit(X_train)
# Create future dateframe
pred = pd.DataFrame()
pred['ds'] = pd.date_range(start='2021-1-31', periods=12*4, freq='M')
# Predict
pred = model.predict(pred)
pred = pred.rename(columns={'yhat':'y'})
# Add 2020-12-31 data point in order to connect the predicted data
# with historical data
pred = pd.concat([X_train,pred])
pred['ds'] = pd.to_datetime(pred['ds'], format='%Y-%m-%d')
pred = pred[pred['ds']>='2020-12-31']

# Plot Line chart
data = []
data.append(go.Scatter(x=X_train['ds'], y=X_train['y']/1000000,
              mode='lines', name='Historical Monthly Passenger Traffic',
              line=dict(color='rgb(102,178,255)')))
data.append(go.Scatter(x=pred['ds'],y=pred['y']/1000000,
			  mode='lines', name='Predicted Passenger Traffic',
              	  line=dict(color='red')))

## Prepare layout
layout = dict(title={'text':'SFO Month Passenger Traffic Prediction (Facebook Prophet)',
                     'x':0.5},
	          xaxis=dict(title='Date'), 
	          yaxis=dict(title='Passenger (M)', gridcolor='lightgray'),
	          legend=dict(x=0.75, y=1),
	          plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='prophet_pred_line.html')

# Export Prediction
pred[['ds','y']].to_csv('Results/prediction_step1.csv', index=False)
