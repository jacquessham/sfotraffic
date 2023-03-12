import math
import json
import datetime
from pandas.tseries.offsets import MonthEnd
from etl_prod import *
from pred_prod import *
from viz_prod import *


# Load metadata, such as file directory
f = open('params.json')
metadata = json.load(f)
f.close()

# Check shock_date format is right
## https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat
try:
    shock_date = datetime.date.fromisoformat(metadata['shock_date']) + MonthEnd(0)
    recovery_reference = datetime.date.fromisoformat(metadata['recovery_reference'])
except:
    print('Date format incorrect, please revise!')
    quit()

# Data Cleansing and Aggregation
df = etl(metadata['file'])

# Data before shock
normality_before_shock = shock_date - MonthEnd(int(metadata['normality_before_shock']))
df_b4shock = df[df['date']<=normality_before_shock]

# Make prediction (After Recovery)
model, pred = result_hw(df_b4shock,pred_period=metadata['pred_period']+12,
                        trend_mode=metadata['trend_mode'],
                        seasonal_mode=metadata['seasonal_mode'])

## Adjust prediction date
adjust_seasonality = metadata['shock_recovery']%12
adjust_year = metadata['shock_recovery']//12
pred['date'] = pred['date'] + MonthEnd(adjust_year*12)
pred = pred.iloc[adjust_seasonality:adjust_seasonality+metadata['pred_period'],:]

# Predict Recovery path
pred_recovery = recovery_path(df, pred, shock_date, recovery_reference, metadata['shock_recovery'], metadata['seasonality_mod'])

# Vizualize the prediction
if metadata['diff_pred']:
    viz_diff(df[df['date']<=shock_date], pred_recovery, pred)
else:
    viz(df[df['date']<=shock_date], pd.concat([pred_recovery, pred]))

# Export Prediction in CSV
if metadata['result_export_csv']:
    pd.concat([pred_recovery, pred]).to_csv('prediction_result.csv',index=False)
