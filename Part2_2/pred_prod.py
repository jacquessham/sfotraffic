import pandas as pd
from pandas.tseries.offsets import MonthEnd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def result_hw(df, model=None, pred_period=24):
    # The stats model cannot handle huge number, must divide by 1M
    def model_training(df):
        model = ExponentialSmoothing(df['pax_count'], trend='mul',
                                     seasonal='mul', seasonal_periods=12).fit()
        return model
    if model is None:
        model = model_training(df)
    pred_startdate = df['date'].max()+ pd.tseries.offsets.MonthEnd(1)
    pred_enddate = df['date'].max()+ pd.tseries.offsets.MonthEnd(pred_period)
    pred_date = pd.date_range(pred_startdate, pred_enddate, freq='m')
    yhat = model.forecast(pred_period)
    pred = pd.DataFrame({'date':pred_date, 'pred': yhat})

    return model, pred

def recovery_path(df, shock_bottom, recovery_duration):
    return
