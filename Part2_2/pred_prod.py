import pandas as pd
from pandas.tseries.offsets import MonthEnd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def result_hw(df, model=None, pred_period=24,trend_mode='mul',seasonal_mode='mul'):
    # The stats model cannot handle huge number, must divide by 1M
    def model_training(df,trend_mode,seasonal_mode):
        model = ExponentialSmoothing(df['pax_count'], trend=trend_mode,
                                     seasonal=seasonal_mode, seasonal_periods=12).fit()
        return model
    if model is None:
        model = model_training(df,trend_mode,seasonal_mode)
    pred_startdate = df['date'].max()+ pd.tseries.offsets.MonthEnd(1)
    pred_enddate = df['date'].max()+ pd.tseries.offsets.MonthEnd(pred_period)
    pred_date = pd.date_range(pred_startdate, pred_enddate, freq='m')
    yhat = model.forecast(pred_period)
    pred = pd.DataFrame({'date':pred_date, 'pred': yhat})

    return model, pred

def recovery_path(df, pred, shock_date, recovery_reference, recovery_duration, seasonality_mod=1):
    # Calculate Moving Average
    df['MA'] = df['pax_count'].rolling(12).mean()
    
    # Set the data on recover_reference as index = 100 and calculate the index
    paxindex_base = df[df['date'].dt.date==recovery_reference]['pax_count'].tolist()[0]
    df['paxindex'] = df['pax_count']/paxindex_base*100
    maindex_base = df[df['date'].dt.date==recovery_reference]['MA'].tolist()[0]
    df['maindex'] = df['MA']/maindex_base*100
    
    # Obtain the diff between index and moving average index
    df['diffindex'] = df['paxindex'] - df['maindex']

    # Find the magitude of each unit of index
    pax_recovered = pred.head(1)['pred'].tolist()[0]
    index_recovered = df[df['date'].dt.date==recovery_reference+MonthEnd(recovery_duration)]['maindex'].tolist()[0]
    pax_shock = df[df['date'].dt.date==shock_date]['pax_count'].tolist()[0]
    pax_per_index = (pax_recovered-pax_shock)/(index_recovered-100)

    # Segment the Recover pred_year
    df_index_range = df[(df['date'].dt.date>recovery_reference) & (df['date'].dt.date<=(recovery_reference+MonthEnd(recovery_duration)))]
    # Prepare Prediction Dataframe
    pred_recovery = pd.DataFrame(df_index_range[['maindex','diffindex']])
    pred_recovery['date'] = pd.date_range(start=shock_date, periods=recovery_duration, freq='M')
    pred_recovery = pred_recovery.iloc[1:-1,:]
    pred_recovery['year'] = pred_recovery['date'].dt.year
    pred_recovery['month'] = pred_recovery['date'].dt.month
    # Calculate the predicted trend pax count
    pred_recovery['raw_prediction'] = pax_shock+(pred_recovery['maindex']-100)*pax_per_index
    # Calculate the final prediction by adjusting with seasonality
    pred_recovery['pred'] = pred_recovery['raw_prediction']*(1+(pred_recovery['diffindex']*seasonality_mod/100))

    return pred_recovery[['date','pred']]
