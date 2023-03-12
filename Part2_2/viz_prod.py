import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


def viz(y_plot, y_hat):
	# Add the last row of y_plot to y_hat to prevent disconnected line
	y_plot_last_row = y_plot.tail(1)
	y_plot_last_row['pred'] = y_plot_last_row['pax_count']
	y_hat = pd.concat([y_plot_last_row, y_hat])

	# Create graph
	## Prepare Graph
	data = []
	data.append(go.Scatter(x=y_plot['date'], y=y_plot['pax_count'],
	              mode='lines', name='Monthly Passenger Traffic',
	              line=dict(color='rgb(102,178,255)')))
	data.append(go.Scatter(x=y_hat['date'],y=y_hat['pred'],
				  mode='lines', name='Predicted Passenger Traffic',
	              	  line=dict(color='red')))


	## Prepare layout
	layout = dict(title={'text':'SFO Month Passenger Traffic Prediction',
	                     'x':0.5},
		          xaxis=dict(title='Date'), 
		          yaxis=dict(title='Passenger (M)', gridcolor='lightgray'),
		          legend=dict(x=0.6, y=1, orientation='h'),
		          plot_bgcolor='rgba(0,0,0,0)')

	# Plot and fix layout
	fig = go.Figure(data=data, layout=layout)
	plotly.offline.plot(fig, filename='sfopax_prediction_refinedmodel.html')

def viz_diff(y_plot, y_hat_recovery, y_hat):
	# Add the last row of each dataframe prevent disconnected line
	y_plot_last_row = y_plot.tail(1)
	y_plot_last_row['pred'] = y_plot_last_row['pax_count']
	y_hat_recovery = pd.concat([y_plot_last_row, y_hat_recovery])
	y_hat_recovery_last_row = y_hat_recovery.tail(1)
	y_hat = pd.concat([y_hat_recovery_last_row, y_hat])

	# Create graph
	## Prepare Graph
	data = []
	data.append(go.Scatter(x=y_plot['date'], y=y_plot['pax_count'],
	            mode='lines', name='Monthly Passenger Traffic',
	            line=dict(color='rgb(102,178,255)')))
	data.append(go.Scatter(x=y_hat_recovery['date'],y=y_hat_recovery['pred'],
				mode='lines', name='Predicted Recovery Passenger Traffic',
	            line=dict(color='pink')))
	data.append(go.Scatter(x=y_hat['date'],y=y_hat['pred'],
				mode='lines', name='Predicted Passenger Traffic',
	            line=dict(color='red')))


	## Prepare layout
	layout = dict(title={'text':'SFO Month Passenger Traffic Prediction',
	                     'x':0.5},
		          xaxis=dict(title='Date'), 
		          yaxis=dict(title='Passenger (M)', gridcolor='lightgray'),
		          legend=dict(x=0.6, y=1, orientation='h'),
		          plot_bgcolor='rgba(0,0,0,0)')

	# Plot and fix layout
	fig = go.Figure(data=data, layout=layout)
	plotly.offline.plot(fig, filename='sfopax_prediction_refinedmodel.html')
