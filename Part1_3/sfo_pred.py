import json
from etl_prod import *
from hw_prod import *


# Load metadata, such as file directory
f = open('params.json')
metadata = json.load(f)
f.close()

# Data Cleansing and Aggregation
df = etl(metadata['file'])

# Make prediction
model, pred = result_hw(df) # Use default pred_period for now
