# Part 2 - Predict Passenger Traffic in SFO after the 2020-2021 Pandemic
Part 2 is the effort to follow up the disruption of 2020-2021 Pandemic to predict the growth pattern of the passenger traffic once the pandemic is over using the latest data available. In this part, I will achieve the goals using Python.

## About the Data Set
The data set is an open source data set obtained from <a href="https://datasf.org/opendata/">Open SF</a>. It consists of 12 columns with 22,869 observations. For the convenience, the data set is cleansed and transformed for this part in the ETL process with <i>etl_2020.py</i>. The ETL process returns 2 csv files, <i>sfo2020pax_eda.csv</i> for EDA and <i>sfo2020pax_month.csv</i> for model training. You may find more detail about the original data set, transformed data sets, and the ETL scripts in the [Data Folder](../Data). The data set is a time series data, and therefore, there are constraints to what we can do as some approches may violate some assumptions on certain algorithms, such as linear regression.

## Assumption
Our assumption of the prediction is that the passenger traffic dropped in 2020 is caused by an extreme demand shock in air traffic due to the restriction on air traffic that is not caused by economic activities. According to the Solow Model learned in Econ 101, we believe the economy is behind the steady state as the Model suggested; it means the economic growth is not in pace with the long-term growth due to the shut down of economic activities, once the economic activities are back to normal, the economic growth will be bounding back to the original pace. Therefore, we believe once air travel is back to normal, the passenger traffic will be bounding back to the 2019 level and continue the long-term growth. 

## Goal
The goal of this part of the project is to utilize the data set to predict the passenger traffic pattern until the passenger traffic level is return to pre-pandemic level (2019) under the assumption backed by the economics theories.


## Plan and Approach
We will first make prediction using traditional time-series statistical learning. The disruption of the passenger traffic comes from an extreme economic shock due to the outbreak of pandemic and believe to be rebounded to pre-pandemic level after the disruption has ended. Traditional time-series models may not make useful prediction as the disruption has been happening long enough that using autoregressive integrate moving average models or any approach heavily rely on 2018-2020 data will not return prediction with rebound momentum. If the prediction is not useful for our goal, we may find different approach to make the prediction to our goal.

## Files
In this part, the folder contains the following files:
<ul>
	<li>prediction_step1.py</li>
	<li>prediction_step2.py</li>
	<li>prediction_step3.py</li>
	<li>prediction_step4.py</li>
	<li>prediction_step5.py</li>
	<li>viz_prediction_step2.py</li>
	<li>viz_prediction_step3.py</li>
	<li>viz_prediction_step4.py</li>
	<li>viz_prediction_step5.py</li>
	<li>viz_prediction_step5_agg.py</li>
	<li>recoverypath_type.py</li>
</ul>

## Data Cleansing
Coming Soon...

## EDA
There are more data available comparing the data set used in Part 1/Part 1.1 because the data set used in this part is downloaded in 3 years after the Part 1 is conducted. You may find the passenger traffic insight between 2005 and 2020 in the <a href="https://github.com/jacquessham/sfotraffic/tree/master/Part2/EDA">EDA folder</a> before learning the prediction model.
<br><br>
<img src=EDA/Images/monthpax_line.png>
<br>
Passenger Traffic in SFO has experienced a steadily growth since 2005 until 2019, a sudden economic shock occur in Q1 2020 due to the outbreak of the coronavirus.

## Model Training and Prediction (Under Construction)
The rumor of an outbreak of coronavirus in a certain Asian country started in Q4 2019 and had developed to a global scale outbreak in Q1 2020. A couple months later, global air travel came to an halt in March, 2020 when effectively all international travels are banned among countries. All counties in the San Francisco Bay Area locked down since mid-March 2020 and passenger traffic has been plunged to the level never seen in the data set since then.
<br>
Our goal is to utilize the data set to predict the passenger traffic pattern until the passenger traffic level is return to pre-pandemic level (2019). Let's assume January, 2021 is the first month the air traffic resume in order to make it simple since our data ends in December, 2020.
<br><br>
### Step 1: Traditional Time-series Approach
The first approach is to use traditional time-series statistical learning to predict the rebounded passenger traffic, to do this, we can use Generalized Additive Model (GMA, Here we are using Facebook Prophet) to predict. As we have mentioned in the EDA phase, we observe the recovering period takes about 4 years: So, we can use the existing data to predict the traffic during 2021-2024. In this phase, we will be using <i>prediction_step1.py</i> to predict and visualize the result.
<br>
<img src=Images/predict_prophet.png>
<br>
As we can see that the passenger traffic bounds significantly in the beginning of 2021 but follow a downward-sloping trend, it is not a useful model because our goal is to find the growth path to recover to the pre-pandemic level; this model is showing us that it violates our assumption the trend is not going back to the pre-pandemic level. The flaw of using GMA is that it heavily rely on previous periods for prediction, so it may not be helpful for our goal. Looking at the result above, the concern is valid: We can see the passenger traffic jumps up dramatically and the trend between 2021-2024 is dropping that the result is against our assumption. 

### Step 2: Scaling the Previous Growth Path
We believe the passenger traffic will spend about 4 years to recover similar to the pace between 2009-2013 as this is the only recover pace we found in EDA. Then, we use <i>recoverypath_type.py</i> to visualize the standardized growth path during these 4 years as we took the Janurary, 2009 as base index to obtain the index of the next 4 years, like below:
<img src=Images/recovery_path.png>
<br>
Having the trend between 2009-2013 convert to index, we can assume the recovery path is similar to this trend and use this trend index as the trend pattern and scale the growth path to predict the passenger traffic between 2021-2024. It means the passenger traffic will recover to December, 2020 level in December, 2024. In this approach, we will take the growth path between 2009-2013 to scale up the magitude of the growth rate in order to grow from the base month of Janurary, 2021 as the base month and December, 2024 as recovered month.
<br>
The formula is the below:<br>
tr_d = Passenger Traffic in month/year d<br>
index_i,j = Passenger Traffic in period i relative to base period of month/year j<br>
index_i,dec20 = index_i,dec09, where 0 =< i =< 47<br>
g_bar = (tr_dec24 - tr_dec20)/(index47,dec09 - index0,dec09), where tr_dec24 = tr_dec19 and index_0,dec09 = 100<br>
tr_d = tr_dec20 + g_bar(index_i,dec20-100), where d between dec,20 and dec,24<br>
<br>
If we apply this method, the prediction will looks like this:
<img src=Images/raw_prediction.png>
<br>
We can see the trend of the recovery path between December,2020 and December,2024 looks fine but the passenger traffic in each month fluctuate with extreme volatility. At the same time, we have multiple months of prediction drop below 0 which is extremly not realistic. We believe the trend capture is fine but we have to smoothen the seasonalilty flucatuation and avoid the predict any number below 0.
<br><br>

### Step 3: Scaling the Previous Growth Path with Moving Average
Our goal of the next step is to improve the model created in the last step and to smoothen the seasonality flucatuation to have the prediction more realistic. One of the useful way to achieve that is to capture the trend using moving average index and seasonality using the difference between actual passenger traffic index and moving average index. The flaw of the model created in the last step comes from the fact that we did not differentiate the calculation of trend and seasonality. In this step, we are going to separate the calculation of trend and seasonality using moving average. The formula is the following:
<br>
The formula is the below:<br>
tr_d = Passenger Traffic in month/year d<br>
tr_d' = Passenger Traffic 12-months Moving Average in month/year d<br>
index_i,j = Passenger Traffic in period i relative to base period of month/year j<br>
index_i,j' = Passenger Traffic 12-months Moving Average in period i relative to base period of month/year j<br>
p_i,j = index_i,j - index_i,j'<br>
index_i,dec20 = index_i,dec09, where 0 =< i =< 47<br>
g_bar = (tr_dec24 - tr_dec20)/(index47,dec09 - index0,dec09), where tr_dec24 = tr_dec19 and index_0,dec09 = 100<br>
tr_d' = tr_dec20 + g_bar(index_i,dec20'-100), where d between dec,20 and dec,24<br>
tr_d = tr_dec20' \* (1 + p_i,j/100)<br>
<br>
If we apply this method, the prediction will looks like this:
<img src=Images/prediction_step3.png>

### Step 4: Scaling the Previous Domestic and International Passenger Growth Path with Moving Average
Coming Soon...
<img src=Images/recovery_path_type.png>
<img src=Images/prediction_step4.png>

### Step 5: Modified Step 4
Coming Soon...
<img src=Images/prediction_step5.png>
<img src=Images/prediction_step5_agg.png>

## Conclusion
Coming Soon...


## Next Step
You may find the cargo tonnage to learn more about air cargo traffic during the pandemic and the prediction in [Part 3 folder](../Part3). Or you may go back to the [Main Page](../) for the other parts of the folder.