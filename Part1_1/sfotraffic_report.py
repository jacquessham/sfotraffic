from sfotraffic_arima import *
from sfotraffic_hw import *
from sfotraffic_prophet import *


result_arima = arima_model(36)
print(result_arima['pred'])