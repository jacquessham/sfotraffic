import json
import datetime
from pandas.tseries.offsets import MonthEnd
from etl_prod import *
from prod_prod import *
from viz_prod import *


# Load metadata, such as file directory
f = open('params.json')
metadata = json.load(f)
f.close()

# Check shock_date format is right
# https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat
try:
	shock_date = datetime.date.fromisoformat(metadata['shock_date']) + MonthEnd(0)
except:
	print('Date format incorrect, please revise!')
	quit()

# Data Cleansing and Aggregation
df = etl(metadata['file'])

# Data before shock
df_b4shock = df[df['date']<=shock_date]
print(df_b4shock)


# Make prediction
model, pred = result_hw(df_b4shock,pred_period=metadata['pred_period']+12)
print(pred)

"""
# Vizualize the prediction
viz(df, pred)

# Export Prediction in CSV
if metadata['result_export_csv']:
	pred.to_csv('prediction_result.csv',index=False)
"""