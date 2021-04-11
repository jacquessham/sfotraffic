from sfotraffic_arima import *
from sfotraffic_hw import *
from sfotraffic_prophet import *
from plot_pred import *


result_arima = result_arima()
result_hw = result_hw()
result_fb = result_gam()
print("Box Jerkin's Model Result: ")
print(result_arima['summary'])
print("Box Jerkin's Model: "+str(result_arima['rmse']))
print('HW Add Model: '+str(result_hw['rmse_add']))
print('HW Mul Model: '+str(result_hw['rmse_mul']))
print('Prophet Model: '+str(result_fb['rmse']))

plot_pred(result_arima['X_train'], result_arima['X_test'], result_arima['pred'],
	      'Box-Jerkins Model','boxjerkins_pred.html')
plot_pred(result_hw['X_train'], result_hw['X_test'], result_hw['pred_add'],
	      'Holts-Winter Trend Additive Model','hw_add_pred.html')
plot_pred(result_hw['X_train'], result_hw['X_test'], result_hw['pred_mul'],
	      'Holts-Winter Trend Multiplicative Model','hw_mul_pred.html')
plot_pred(result_fb['X_train'], result_fb['X_test'], result_fb['pred'],
	      'Generalized Additive Model','fb_pred.html')