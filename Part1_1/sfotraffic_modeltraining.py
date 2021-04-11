from sfotraffic_arima import *
from sfotraffic_hw import *
from sfotraffic_prophet import *
from plot_pred import *


result_arima = result_arima()
result_hw = result_hw()
result_fb = result_gam()

# Print result on command line
print("Box Jerkin's Model Result: ")
print(result_arima['summary'])
print("Box Jerkin's Model: "+str(result_arima['rmse']))
print('HW Add Model: '+str(result_hw['rmse_add']))
print('HW Mul Model: '+str(result_hw['rmse_mul']))
print('Prophet Model: '+str(result_fb['rmse']))

# Plot prediction for each model
plot_pred(result_arima['X_train'], result_arima['X_test'], result_arima['pred'],
	      'Box-Jerkins Model','boxjerkins_pred.html')
plot_pred(result_hw['X_train'], result_hw['X_test'], result_hw['pred_add'],
	      'Holts-Winter Trend Additive Model','hw_add_pred.html')
plot_pred(result_hw['X_train'], result_hw['X_test'], result_hw['pred_mul'],
	      'Holts-Winter Trend Multiplicative Model','hw_mul_pred.html')
plot_pred(result_fb['X_train'], result_fb['X_test'], result_fb['pred'],
	      'Generalized Additive Model','fb_pred.html')

# Save result in text file
file = open('Results/ModelTrainingResults.txt','w')
file.write('Box Jerkins Model Result\n\n')
file.write(str(result_arima['summary']))
file.write('\n')
file.write("Box Jerkin's Model: "+str(result_arima['rmse']))
file.write('\n')
for i in range(50):
	file.write('-')
file.write('\n')
file.write('Holts-Winter Models Result\n')
file.write('HW Add Model: '+str(result_hw['rmse_add']))
file.write('\n')
file.write('HW Mul Model: '+str(result_hw['rmse_mul']))
file.write('\n')
for i in range(50):
	file.write('-')
file.write('\n')
file.write('Generalized Additive Model\n')
file.write('Prophet Model: '+str(result_fb['rmse']))
file.close()