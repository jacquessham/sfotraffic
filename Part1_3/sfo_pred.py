import json
from etl_prod import *
from hw_prod import *
from viz_prod import *


# Load metadata, such as file directory
f = open('params.json')
metadata = json.load(f)
f.close()

# Data Cleansing and Aggregation
df = etl(metadata['file'])

# Make prediction
model, pred = result_hw(df,pred_period=metadata['pred_period'])

# Vizualize the prediction
viz(df, pred)

# Export Prediction in CSV
if metadata['result_export_csv']:
	pred.to_csv('prediction_result.csv',index=False)
