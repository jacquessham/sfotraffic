import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

def plot_pred(X_train, X_test, yhat, model_name, html_filename):
    data = []
    data.append(go.Scatter(x=X_train['date'], y=X_train['pax_count'],
                           mode='lines', name='Training Data',
                           line=dict(color='rgb(160,160,160)')))
    data.append(go.Scatter(x=X_test['date'], y=X_test['pax_count'],
                           mode='lines', name='Testing Data',
                           line=dict(color='rgb(102,178,255)')))
    data.append(go.Scatter(x=yhat['date'], y=yhat['pred'],
                           mode='lines', name='Prediction',
                           line=dict(color='rgb(255,0,0)')))

    ## Prepare layout
    layout = dict(title={'text':model_name,
                         'x':0.5},
                  xaxis=dict(title='Date'), 
                  yaxis=dict(title='Passenger (M)', gridcolor='lightgray'),
                  legend=dict(x=0.7, y=1, orientation='h'),
                  plot_bgcolor='rgba(0,0,0,0)')
    # Plot and fix layout
    fig = go.Figure(data=data, layout=layout)
    # Plot chart
    plotly.offline.plot(fig, filename=html_filename)