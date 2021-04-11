import pandas as pd
import calendar
import pmdarima as pm
from sklearn.metrics import mean_squared_error as mse

def result_arima(pred_period=24):
    # Use monthly data
    df = pd.read_csv('../Data/sfopax_month.csv')

    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['month_abbr'] = df['month'].apply(lambda x: calendar.month_abbr[x])
    df['pax_count'] = df['pax_count']/1000000

    # Split train/test
    X_train = df[df['year']<=2015][['date','pax_count']]
    X_test = df[df['year']>2015]['pax_count'].tolist()

    model = pm.auto_arima(X_train['pax_count'], start_p=1, start_q=1,
                                 max_p=6, max_q=6, m=12,
                                 max_P=6, max_Q=6, seasonal=True,
                                 d=1, D=1, max_d=6, max_D=6, trace=True,
                                 error_action='ignore',
                                 suppress_warnings=True,
                                 stepwise=True)
    # Prepare result
    result = {}
    # Save model summary
    result['summary'] = model.summary() 
    # Save X_train (pax_count in numbers, instead of millions)
    df['pax_count'] = df['pax_count']*1000000
    result['X_train'] = X_train
    # Prediction, dynamic for further prediction beyond X_test dates
    yhat = model.predict(pred_period)
    X_test_startdate = X_train['date'].max()+ pd.tseries.offsets.MonthEnd(1)
    X_test_enddate = X_train['date'].max()+ pd.tseries.offsets.MonthEnd(pred_period)
    X_test_date = pd.date_range(X_test_startdate, X_test_enddate, freq='m')
    pred = pd.DataFrame({'date':X_test_date, 'pred': yhat})
    result['pred'] = pred

    # rmse can only be using first 24 periods
    pm_rmse = mse(X_test, yhat[:24])**0.5
    result['rmse'] = pm_rmse

    return result
