from sfotraffic_arima import *
from sfotraffic_hw import *
from sfotraffic_prophet import *


result_arima = result_arima()
result_hw = result_hw()
result_fb = result_gam()
print("Box Jerkin's Model Result: ")
print(result_arima['summary'])
print("Box Jerkin's Model: "+str(result_arima['rmse']))
print('HW Add Model: '+str(result_hw['rmse_add']))
print('HW Mul Model: '+str(result_hw['rmse_mul']))
print('Prophet Model: '+str(result_fb['rmse']))