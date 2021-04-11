# Part 1.1 SFO Passenger Traffic Prediction (2018-2019)/Version 2

Part 1.1 follows up the Part 1 with updated code in Python. We have a data set on SFO traffic between July, 2005 and Decemeber, 2017. It includes the passenger counts on each airline every month in the given period. I have two goals for this project:
<ol>
	<li>Visualize the data set for EDA purpose</li>
	<li>Predict the passenger traffic and growth rate in 2018 and 2019</li>
</ol>
<br>
This part differs with Part 1 is to make prediction of passenger traffic between 2018-2019 with 2005-2017 data but using Python only. The EDA is also redone with Python packages instead of ggplot in R. 

## About the data set
The data set is an open source data set obtained from <a href="https://datasf.org/opendata/">Open SF</a>. It consists of 12 columns with 17,959 observations. For the convenience, the data set is cleansed and transformed for this part in the ETL process. The ETL process returns 2 csv files, 1 for EDA and 1 for model training. You may find more detail about the original data set, transformed data sets, and the ETL scripts in the [Data Folder](../Data). The data set is a time series data, and therefore, there are constraints to what we can do as some approches may violate some assumptions on certain algorithms, such as linear regression.

## Goal and Plan
The goal of this part of the project is to utilize the data set to predict the passenger traffic between 2018-2019 in SFO. In order to do this, we will take the following steps to achieve our goal:<br>
<ol>
	<li>Data Cleansing</li>
	<li>EDA</li>
	<li>Model Training</li>
	<li>Model Validation</li>
	<li>Prediction</li>
</ol>

## Files
In this part, the folder contains the following files:
<ul>
	<li>sfotraffic_arima.py</li>
	<li>sfotraffic_hw.py</li>
	<li>sfotraffic_prophet.py</li>
	<li>sfotraffic_report.py</li>
</ul>

## Data Cleansing and ETL Process
The data cleansing part was done to keep entry records be more consistent. For example, some of the Continental Airlines entries was recorded "United Airlines - Pre 2013"; and some of the full service airlines were labeled as low cost carriers, while some low cost carriers were labeled as full cost carrier. For the convienence for both EDA and model training phases, the ETL process transformed the original data set to 2 different data set, <i>sfopax_eda.csv</i> and <i>sfopax_month.csv</i>. If you are interested what has done to improve the data quality, you may find more details in the [Data Folder](../Data) and [ETL Folder](../Data/ETL_part1_1). 

## EDA
The data set consists of data between 2005 and 2017. Before we build the predictive model, we shall understand more about the insights about the data set. You may learn more about the data set in the <a href="https://github.com/jacquessham/sfotraffic/tree/master/Part1_1/EDA">EDA folder</a>. The EDA process used <i>sfopax_eda.csv</i> as the data set contains more detail about the flights regards on airlines, destinations, and other details.

## Model Training and Model Validation
### Strategy
The problem to times-series data is the each data point is highly correlated with data point(s) to the previous period(s), known as autocorrelation. It violates the assumption of linear regression. The best way to make prediction is to use time-series statistical learning methods like Box-Jerkins Method, Holt-Winters Method, and General Additive Model. There are 3 packages available in Python that I would use for the purpose:
<ul>
	<li><i>pmdarima</i> for Box-Jerkins Method</li>
	<li><i>statsmodels.tsa.holtwinters</i> for Holts-Winters Method</li>
	<li><i>Facebook Prophet</i> for General Additive Model</li>
</ul>
I would use <i>sfopax_month.csv</i> in the [Data Folder](../Data), which the data set is aggregated to monthly passenger count, to train the predictive models using the above packages in Python and validate which predictive models is the most accurated.
<br>
The data set would be splited to roughly 80:20 split for training and validating data set. The training set is roughly 10 years between 2005-2015; the remaining data from 2016-2017 is the validation set. RMSE would be used for model evaluation, whichever the model has the lowest RMSE is the most accurated model. We would choose that model to predict the passenger traffic between 2018-2019. 
<br>
<b><li>sfotraffic_report.py</li> is the script of driver script for model training, model validation, and prediction. (More description about this script is coming soon...)</b>

### Approach 1: Box-Jerkins Method
Box-Jenkins Method is an autoregressive integrated moving average model which is learned by converting the data set into stationary. In this project, we use ARIMA and SARIMA models. The difference between the two is that ARIMA is non-seasonal while SARIMA is seasonal. <i>pmdarima</i>is a Python package similar to the <i>auto.arima()</i> in R's <i>forecast</i> package. Convienently, you may import <i>pmdarima</i> and use the same syntax <i>auto.arima()</i> to achieve the same goal in Python to find the best hyperparameters for your Box-Jerkins model.
<br>
The pmdarima package follows R style and syntax. The syntax is very similar to the forecast package in R but pmdarima only takes the responsive variable column, in our case, the pax_count column. The <i>auto.arima()</i> takes the the pax_count column, the range (minimum and maximum) of hyperparameters including: p, q, d, P, Q, D, m, then the <i>auto.arima()</i> would find the best model using Box-Jerkins methods (Both ARIMA and SARIMA while setting seasonal=True, turn off if seasonality is not a concern, so that SARIMA model is ignored).
<br>
<i>sfotraffic_arima.py</i> is the file that used this method to train the model. The file imports the following packages:
<ul>
	<li>pandas</li>
	<li>calendar</li>
	<li>pmdarima</li>
	<li>mean_squared_error from sklearn.metrics</li>
</ul>
<i>pandas</i> is used for data managerment. <i>calendar</i> is used for date format. <i>pmdarima</i> is for model training. <i>mean_squared_error</i> is used for calculating RMSE.
<br>
The script has a function of <i>arima_model()</i> first imported the data from <i>sfopax_month.csv</i> and split the data to training and testing data set. Then, use <i>auto.arima()</i> to grid search the best model with the following hyperparameters:
<ul>
	<li>p (Trend autoregression order) between 1-6</li>
	<li>q (Trend moving average order) between 1-6</li>
	<li>P (Seasonal autoregression order) between 1-6</li>
	<li>Q (Seasonal moving average order) between 1-6</li>
	<li>d (Trend difference order) between 1-6</li>
	<li>D (Seaonal differece order) between 1-6</li>
	<li>m = 12 (Indicates a yearly seasonal cycle)</li>
	<li>seasonal = True (Indicates seasonality exist)</li>
	<li>trace = True</li>
	<li>stepwise = True</li>
</ul>
<i>auto.arima()</i> would return the best model in an object from the grid search, you may use .summary() to obtain the parameters of the model. Once the best Box-Jerkins model is found for this data set, the scripts predicts the passenger traffic between 2016-2017 and calculates the RMSE. Note that the RMSE is calculated based on passenger count in millions. The scripts would finally declare a dictionary and return the following:
<ul>
	<li>Model summary</li>
	<li>Training data set</li>
	<li>Prediction between 2016-2017 with dates</li>
	<li>RMSE</li>
</ul>
<br>
This function is called in <i>sfotraffic_report.py</i> for model training phases.


### Approach 2: Holts-Winters Method

### Approach 3: General Additive Model

