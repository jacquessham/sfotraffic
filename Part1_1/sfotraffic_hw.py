import pandas as pd
import calendar
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error as mse


def result_hw(pred_period=24):
    # Use monthly data
    df = pd.read_csv('../Data/sfopax_month.csv')
    # Reformat dataframe
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['month_abbr'] = df['month'].apply(lambda x: calendar.month_abbr[x])
    df['pax_count'] = df['pax_count']/1000000

    # Split train/test
    X_train = df[df['year']<=2015]
    X_test = df[df['year']>2015]

    # Model training
    model_add = ExponentialSmoothing(X_train['pax_count'], trend='add',
                                 seasonal='add', seasonal_periods=12).fit()

    model_mul = ExponentialSmoothing(X_train['pax_count'], trend='mul',
                                 seasonal='mul', seasonal_periods=12).fit()

    # Prepare date list for data frame
    X_test_startdate = X_train['date'].max()+ pd.tseries.offsets.MonthEnd(1)
    X_test_enddate = X_train['date'].max()+ pd.tseries.offsets.MonthEnd(pred_period)
    X_test_date = pd.date_range(X_test_startdate, X_test_enddate, freq='m')

    # Additive Model Prediction
    yhat_add = model_add.forecast(pred_period)
    hw_rmse_add = mse(X_test['pax_count'].tolist(), yhat_add.tolist()[:24])**0.5

    pred_add = pd.DataFrame({'date':X_test_date, 'pred': yhat_add})
    

    # Multiplicative Model Prediction
    yhat_mul = model_mul.forecast(pred_period)
    hw_rmse_mul = mse(X_test['pax_count'].tolist(), yhat_mul.tolist()[:24])**0.5

    pred_mul = pd.DataFrame({'date':X_test_date, 'pred': yhat_mul})
    
    # Save result
    result = {}
    result['X_train'] = X_train[['date','pax_count']]
    result['pred_add'] = pred_add
    result['rmse_add'] = hw_rmse_add
    result['pred_mul'] = pred_mul
    result['rmse_mul'] = hw_rmse_mul

    return result

