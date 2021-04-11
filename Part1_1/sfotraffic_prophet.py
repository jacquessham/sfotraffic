import pandas as pd
from sklearn.metrics import mean_squared_error as mse
from prophet import Prophet


def result_gam(pred_period=24):
	# Use monthly data
	df = pd.read_csv('../Data/sfopax_month.csv')
	# Reformat data frame
	df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
	df['year'] = df['date'].dt.year
	df['pax_count'] = df['pax_count']/1000000

	X_train = df[df['year']<=2015][['date','pax_count']]
	X_test = df[df['year']>2015][['date','pax_count']]
	# Save the dataframe for return object
	X_train_org = X_train
	X_test_org = X_test
	# Rename the column names for Prophet
	X_train = X_train.rename(columns={'date':'ds', 'pax_count':'y'})
	X_test = X_test.rename(columns={'date':'ds', 'pax_count':'y'})

	# Train the model and predict
	model = Prophet()
	model.fit(X_train)
	yhat = model.predict(X_test)

	# Get RMSE
	fb_rmse = mse(X_test['y'], yhat['yhat'].tolist()[:24])**0.5

	# Reformat the data frame for result
	yhat = yhat[['ds','yhat']]
	yhat = yhat.rename(columns={'ds':'date', 'yhat':'pred'})

	# Save result and return
	result = {}
	result['X_train'] = X_train_org
	result['X_test'] = X_test_org
	result['pred'] = yhat
	result['rmse'] = fb_rmse

	return result

