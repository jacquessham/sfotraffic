suppressMessages(library(tidyverse))
suppressMessages(library(magrittr))
suppressMessages(library(tseries))
suppressMessages(library(forecast))
library(ggplot2)


path <- # Your path
setwd(path)
# Load Data into dataframe
airtraffic <- read.csv("Air_Traffic_Passenger_Statistics.csv")
# Change the column names for the convenience
colnames(airtraffic) <- c("date","op_airlines","op_code","pub_airlines",
                          "pub_code","geo_summ","geo_region","type",
                          "price","terminal","boarding_area","pax_count")

# Notice that date is written in YYYYMM, we need to split into two columns
airtraffic$year <- substr(airtraffic$date, 1, 4)
airtraffic$month <- substr(airtraffic$date, 5, 6)

# We need to aggregate the passenger counts for time series analysis
summ <- airtraffic %>% group_by(year,month) %>% summarise(sumpax = sum(pax_count))
# Build a index column for the convenient for line graph
summ$index <- 1:nrow(summ)
summ$sumpax_m <- summ$sumpax/1000000

# Let's visualize the data into line chart
summ %>% 
  ggplot() + geom_line(aes(x = index, y = sumpax_m, group = 1, color = "red")) +
  ggtitle("SFO Passenger Count between 2005 and 2017") +
  theme_minimal() + theme(legend.position="none") +
  scale_x_continuous(name = "Index") +
  scale_y_continuous(name = "Passengers (Millions)")

# Let's split the data into training and validation sets
# In 80:20 split, training set is roughly 10 years
# Training set is between 2005 and 2015
# Validation set is 2016 and 2017
train_pax <- ts(summ$sumpax_m[1:126], start = c(2005,7), frequency = 12)
valid_pax <- ts(summ$sumpax_m[127:150], start = c(2016,1), frequency = 12)

############# Holt-Winters#############
# Holt-Winters Additive Model
model_hw_add <- HoltWinters(x = train_pax, seasonal = "additive")
# Visualize the result
plot(model_hw_add, main="Holt-Winters Model for SFO Traffic", xlab="Year",
     ylab="Passengers (Millions)")
legend("bottomright", legend = c("Observed", "Predicted"),
       lty = 1, col = c("black", "red"), cex = 0.5)
model_hw_add_pred <- forecast(model_hw_add, h=24, level=0.95)
plot(model_hw_add_pred)
points(valid_pax, type='l', col="red")
# Calculate RMSE
sqrt(mean((valid_pax - model_hw_add_pred$mean[1:24])**2))


# Then look at the "multiplicative"
model_hw_mult <- HoltWinters(x = train_pax, seasonal = "multiplicative")
plot(model_hw_mult)
model_hw_mult_pred <- forecast(model_hw_mult, h=24, level=0.95)
plot(model_hw_mult_pred)
legend("bottomright", legend = c("Observed", "Predicted"),
       lty = 1, col = c("black", "red"), cex = 0.5)
points(valid_pax, type='l', col="red")
sqrt(mean((valid_pax - model_hw_mult_pred$mean[1:24])**2))


############# ARIMA ###############
# First look at ACF plot
acf(train_pax)
# Perform a more formal test
adf.test(train_pax)
# We reject the alternative that the data set is stationary

# Instead of manually find hyperparameters, have R to do it
auto.arima(train_pax, seasonal=FALSE)
# We found that ARIMA(0,1,0) is the best fit
model_arima <- arima(train_pax, order=c(0,1,0))
fitted_arima <- train_pax - model_arima$residuals
plot(train_pax, type="l", main="ARIMA (0,1,0) Model for SFO Traffic",
     xlab="Time", ylab="Passengers (Millions)")
points(fitted_arima, type = "l", col = "red")
legend("topleft", legend = c("Observed", "Predicted"),
       lty = 1, col = c("black", "red"), cex = 0.5)
# Forecast 2017 and 2018
plot(forecast(object = model_arima, h = 24, level = 0.95))
# Calculate RMSE
sqrt(mean((valid_pax - unlist(forecast(object = model_arima, h = 24, level = 0.95)[4]))**2))

############# SARIMA ##############
auto.arima(train_pax)
# We found that SARIMA(1,0,1)(0,1,1)[12] is the best fit
model_sarima <- arima(train_pax, order=c(1,0,1), seasonal=list(order=c(0,1,1), period=12))
model_sarima
fitted_sarima <- train_pax - model_sarima$residuals
plot(train_pax, type="l", main="ARIMA (0,1,0) Model for SFO Traffic",
     xlab="Time", ylab="Passengers (Millions)")
points(fitted_sarima, type = "l", col = "red")
legend("topleft", legend = c("Observed", "Predicted"),
       lty = 1, col = c("black", "red"), cex = 0.5)
# Forecast 2017 and 2018
plot(forecast(object = model_sarima, h = 24, level = 0.95))
# Calculate RMSE
sqrt(mean((valid_pax - unlist(forecast(object = model_sarima, h = 24, level = 0.95)[4]))**2))


########### Result ##################
# We found that multiplicative Holt-Winters is best on prediction
# Use this model to predict 2018 and 2019
pred <- forecast(model_hw_mult, h=48, level=0.95)
plot(pred)
# Result of 2018 and 2019
unname(unlist(pred[4]))[25:48]
