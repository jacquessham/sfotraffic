# Part 2 - Predict Passenger Traffic in SFO after the 2020-2021 Pandemic
Part 2 is the effort to follow up the disruption of 2020-2021 Pandemic to predict the growth pattern of the passenger traffic once the pandemic is over using the latest data available. In this part, I will achieve the goals using Python.

## About the dataset
The dataset is an open source dataset obtained from <a href="https://datasf.org/opendata/">Open SF</a>. It consists of 12 columns with 22,869 observations. For the convenience, the dataset is cleansed and transformed for this part in the ETL process with <i>etl_2020.py</i>. The ETL process returns 2 csv files, <i>sfo2020pax_eda.csv</i> for EDA and <i>sfo2020pax_month.csv</i> for model training. You may find more detail about the original dataset, transformed datasets, and the ETL scripts in the [Data Folder](../Data). The dataset is a time series data, and therefore, there are constraints to what we can do as some approches may violate some assumptions on certain algorithms, such as linear regression.

## Assumption
Our assumption of the prediction is that the passenger traffic dropped in 2020 is caused by an extreme demand shock in air traffic due to the restriction on air traffic that is not caused by economic activities. According to the Solow Model learned in Econ 101, we believe the economy is behind the steady state as the Model suggested; it means the economic growth is not in pace with the long-term growth due to the shut down of economic activities, once the economic activities are back to normal, the economic growth will be bounding back to the original pace. Therefore, we believe once air travel is back to normal, the passenger traffic will be bounding back to the 2019 level and continue the long-term growth. 

## Goal
The goal of this part of the project is to utilize the dataset to predict the passenger traffic pattern until the passenger traffic level is return to pre-pandemic level (2019) under the assumption backed by the economics theories.


## Plan and Approach
We will first make prediction using traditional time-series statistical learning. The disruption of the passenger traffic comes from an extreme economic shock due to the outbreak of pandemic and believe to be rebounded to pre-pandemic level after the disruption has ended. 
<br>
Our predictive model has to satisfy the following requirement:
<ul>
	<li>Do not violate the time-series-related assumption</li>
	<li>The passenger traffic rebound to pre-pandemic level once air travel is back to normal as passenger traffic return to its steady state suggested by the Slow Model</li>
</ul>
<br>
Traditional time-series models may not make useful prediction as the disruption has been happening long enough that using autoregressive integrate moving average models or any approach heavily rely on 2018-2020 data will not return prediction with rebound momentum. If the prediction is not useful for our goal, we may find different approach to make the prediction to our goal.

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
The data cleansing part is identical to the data cleansing done in Part 1.1. If you are interested what has done to improve the data quality, you may find more details in the [Data Folder](../Data) and [Part 1.1 ETL Folder](../Data/ETL_part1_1). 


## EDA
There are more data available comparing the dataset used in Part 1/Part 1.1 because the dataset used in this part is downloaded in 3 years after the Part 1 is conducted. You may find the passenger traffic insight between 2005 and 2020 in the <a href="https://github.com/jacquessham/sfotraffic/tree/master/Part2/EDA">EDA folder</a> before learning the prediction model. The dataset we are using consists of observation between 2005 and 2020. To answer our curious of how the passenger traffic in SFO dropped significantly visually, below is the line chart: 
<br><br>
<img src=EDA/Images/monthpax_line.png>
<br>
Passenger Traffic in SFO has experienced a steadily growth since 2005 until 2019, a sudden economic shock occur in Q1 2020 due to the outbreak of the coronavirus. We can see that the passenger traffic halted in the beginning of 2020 and maintain in a fraction of pre-pandemic level. It means it is hard for us to predict a rebound with traditional time-series statistical learning since we have insufficient amount of data to recover in an extreme rapid pace from an extreme low level to the pre-pandemic level.
<br>
We know that there is a great economic recession in 2008. If we focus on that period, we can see the passenger traffic moving average dropped betwee late 2008 and late 2009. Then, the moving average rebound in 2009 and grow until it leveled out in 2013. Since then, we see the moving average flatted out in 2013 and 2019 for a short period time but never ever dropped again. As we have also confirmed in the EDA phase, the trend experiences about 4 years grow after its drop. So, we can use the rebound period between 2009-2013, or 4 years in total, as reference to help us to make prediction of rebound in passenger traffic.

## Model Training and Prediction
The rumor of an outbreak of coronavirus in a certain Asian country started in Q4 2019 and had developed to a global scale outbreak in Q1 2020. A couple months later, global air travel came to an halt in March, 2020 when effectively all international travels are banned among countries. All counties in the San Francisco Bay Area locked down since mid-March 2020 and passenger traffic has been plunged to the level never seen in the dataset since then.
<br>
Our goal is to utilize the dataset to predict the passenger traffic pattern until the passenger traffic level is return to pre-pandemic level (2019). Let's assume January, 2021 is the first month the air traffic resume in order to make it simple since our data ends in December, 2020.
<br><br>
### Step 1: Traditional Time-series Approach
The first approach is to use traditional time-series statistical learning to predict the rebounded passenger traffic for our benchmark model. To do this, we can use <a href="https://en.wikipedia.org/wiki/Generalized_additive_model">Generalized Additive Model</a> (GMA, Here we are using Facebook Prophet) to predict. This is simple statiscts additive model to predict based on smooth functions of predictor variables. As we have mentioned in the EDA phase, we observe the recovering period takes about 4 years: So, we can use the existing data to predict the traffic during 2021-2024. In this phase, we will be using <i>prediction_step1.py</i> to predict and visualize the result. Below is the result:
<br>
<img src=Images/predict_prophet.png>
<br>
As we can see that the passenger traffic bounds significantly in the beginning of 2021 but follow a downward-sloping trend, it is not a useful model because our goal is to find the growth path to recover to the pre-pandemic level, not a sustainably shrink; this model is showing us that it violates our assumption the trend is not going back to the pre-pandemic level. The passenger traffic jumps up dramatically and the trend between 2021-2024 is dropping that the result is against our assumption. The flaw of using GMA is that it heavily rely on previous periods for prediction (2021 prediction relies on 2020 data), so it may not be helpful for our goal because the prediction relied on an abnormal economic state. Since other time-series algorithms, such as Holt-Winters and Box-Jenkins methods, also relies on last period observations to make prediction, so it will behave similarly tothe GMA model and we shall not build a predictive model with those algorithms. 

### Step 2: Scaling the Previous Recovery Trend
After training the model with GMA algorithm, we can conclude the traditional time-series statistical learning methods are not useful to build a predictive model to serve our goal because the prediction relies heavily with last period data that return a result of sudden jumps in passenger traffic in 2021 and drop sustainably which violates our assumption that passenger traffic would rebound to pre-pandemic level. 
<br>
Besides GMA algorithm, we may look at other algorithms and see whether it can help us. Linear regression will not be suitable in our exercise, because the dataset's autocorrelation characteristic violates one of the linear regression assumption. In the case of decision tree, random forest, gradient boosting are not suitable as well because we do not have the data that allow us to train a model to have a rapid recovery from 2020 level back to 2019 level that satisfies our promise from the Solow Model.
<br>
We believe the passenger traffic will spend about 4 years to recover similar to the pace between 2009-2013 as this is the recover pace reference we found in EDA. It means the passenger traffic will recover to pre-pandmic level in December, 2024 starting in December, 2020 (The recovery period is between 2021-2024). Then, we use <i>viz_recoverypath_type.py</i> to visualize the standardized growth path during these 4 years as we took the Janurary, 2009 as base index to obtain the index of the next 4 years, like below:
<img src=Images/recovery_path.png>
<br>
Scaling the previous recovery trend means we need map the recovery trend to the prediction periods and up-scale the growth rate.  We will first convert passenger traffic to index with base period of December, 2008 to capture the trend between 2009-2013. Then, we will find the growth rate by finding the difference pre-pandemic level (December, 2019) and pandemic level (December, 2020) divided by the index difference between the beginning and ending recovery trend (December, 2008 and December, 2013). By doing that, we will scale up the magnitude the growth rate relative to the trend between 2009-2013 to increase the momentum to jump back to the steady state. Since we have map the recovery trend to the prediction periods, each month in the prediction periods has the identical passenger traffic index as the recovery trend between 2009-2013 (For example, Jan 2021 index is same as Jan 2009...etc). We will deduct 100 by the index of each month for the additive index above the base month (December, 2020) and multiple by the growth rate to obtain the monthly passenger traffic addition to base month. At last, we will finalize the prediction by adding the base month passenger traffic with the monthly passenger traffic addition to base month. In other words, we will multiple the difference between the monthly passenger traffic index and 100 and multiplying the manitude of growth rate and add the base month passenger traffic while December, 2020 is the base month.
<br>
The formula is the below:<br>
tr_d = Passenger Traffic in month/year d<br>
index_i,j = Passenger Traffic in period i relative to base period of month/year j<br>
index_i,dec20 = index_i,dec09, where 0 =< i =< 47<br>
g_bar = (tr_dec24 - tr_dec20)/(index47,dec09 - index0,dec09), where tr_dec24 = tr_dec19 and index_0,dec09 = 100<br>
tr_d = tr_dec20 + g_bar(index_i,dec20-100), where d between dec,20 and dec,24<br>
<br>
In this phase, we will be using <i>prediction_step2.py</i> to predict and <i>viz_prediction_step2.py</i> to visualize the result. If we apply this method, the prediction will looks like this:
<img src=Images/raw_prediction.png>
<br>
We can see the trend of the recovery path between December,2020 and December,2024 looks fine but the passenger traffic in each month fluctuates with extreme volatility. At the same time, we have multiple months of prediction drop below 0 which is extremly not realistic. We believe the trend capture is fine but we have to smoothen the seasonalilty fluctuation and avoid predicting any number below 0.
<br><br>

### Step 3: Scaling the Previous Recovery Trend with Moving Average
Our goal of this step is to improve the model created in the last step and to smoothen the seasonality fluctuation to make the prediction more realistic. The flaw of the model created in the last step comes from the fact that we did not differentiate the calculation of trend and seasonality. One of the useful ways to achieve that is to capture the trend using moving average index and seasonality using the difference between actual passenger traffic index and moving average index. In this step, we are going to separate the calculation of trend and seasonality using moving average. We will first predict the trend with moving average and scale up the magnitude first to predict the trend like we did in the last step. Then, we will add the seasonality fluctuation by finding the difference between actual passenger traffic and moving average in percentage between 2009-2013. At last, we will finalize our prediction by combining the predicted trend and predicted seasonality fluculation. In order words, the finalized prediction is a trend prediction mulitple by one plus seasonality flucation in percentage. The formula is the following:
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
In this phase, we will be using <i>prediction_step3.py</i> to predict and <i>viz_prediction_step3.py</i> to visualize the result. If we apply this method, the prediction will looks like this:
<img src=Images/prediction_step3.png>
<br><br>
With this approach, we can see the seasonality fluctuation is moderate and never go below 0. Although we can see there is some rapid growth in 2024, this model satisfies our assumptions and is more useful to predict the passenger traffic.

### Step 4: Scaling the Previous Domestic and International Passenger Recovery Trend with Moving Average
In the mid-2021, we see that domestic travel is starting to recover in a moderate rate, but, in contrast, international travel is still in halt. Therefore, it may be useful to separate the recovery path between domestic traffic and international traffic. If we do so, the recovery path look something like below:
<img src=Images/recovery_path_type.png>
<br>
We can see the passenger traffic for domestic travel recover about 5-10% faster during the recovery period relative to international travel. We can use the same algorithm in step 3 to develop two different models for domestic and international travels. The formula for both models are the same, but for the seek of clarity formula is the following:<br>
tr_d,type = Passenger Traffic of either Domestic or International Travel in month/year d, where type = dos/intl<br>
tr_d,type' = Passenger Traffic 12-months Moving Average of either Domestic or International Travel in month/year d, where type = dos/intl<br>
index_i,j,type = Passenger Traffic of either Domestic or International Travel in period i relative to base period of month/year j, where type = dos/intl<br>
index_i,j,type' = Passenger Traffic 12-months Moving Average of either Domestic or International Travel in period i relative to base period of month/year j, where type = dos/intl<br>
p_i,j,type = index_i,j,type - index_i,j,type', where type = dos/intl<br>
index_i,dec20,type = index_i,dec09,type, where 0 =< i =< 47, type = dos/intl<br>
g_bar,type = (tr_dec24,type - tr_dec20,type)/(index47,dec09,type - index0,dec09,type), where tr_dec24,type = tr_dec19,type and index_0,dec09,type = 100, type = dos/intl<br>
tr_d,type' = tr_dec20,type + g_bar(index_i,dec20,type'-100), where d between dec,20 and dec,24, type = dos/intl<br>
tr_d = tr_dec20,type' \* (1 + p_i,j,type/100), where type = dos/intl<br>
<br>
In this phase, we will be using <i>prediction_step4.py</i> to predict and <i>viz_prediction_step4.py</i> to visualize the result. After the calculation, the result looks something like:
<img src=Images/prediction_step4.png>
<br>
We can see the flaw of this model is that the prediction of international passenger traffic goes below 0 for about 12-15 months while the domestic passenger traffic prediction is fine. Therefore, we need to address this problem in the next step.

### Step 5: Modified Step 4
The goal of this step is to fix the flaw of the model trained in step 4 to prevent any prediction go below 0. The reason why the international passenger traffic prediction drop below 0 because the base number in period 0, or Decemeber, 2020, was too low and we deduct with a large magititude when the index drop below 100 (Which is the index of period 0). Let's take a step back to review the situtation of international travel: As mentioned, the international travel is in halt; the passengers who are travelling internationally are essential and unavoidable. Therefore, there is no way the passenger traffic drop too much in trend but only seasonal flucation in 2021 until the borders are reopened. The data captured during the time with no irregular travel restriction, unlike during the pandemic, so the pattern in the dataset may not be accuate and we need to come up with some adjustment to reflect the situation unique in the pandemic. We can see the time that the index drop below 100 are mostly in the beginning of the passenger traffic recovery path. In reality, we do not see the borders may open up in the first two years, 2021-2022 of the recovery path due to new virus variants and vaccines rollout schedule in various country. So, we can add an additional assumption that the international travel cannot drop significantly because the international travels occur in the recovery period are essential and unavoidable (Aviodable business trips and leisure travels have been excluded in the statistics, so there is not any factor to international passenger traffic drop in trend). We can adjust the calculation of international travel to eliminate the trend effect when index drop below 100. The formula is the following:<br>
Coming Soon...
<br><br>
In this phase, we will be using <i>prediction_step5.py</i> to predict and <i>viz_prediction_step5.py</i> to visualize the result. After the calculation, the result looks something like:
<img src=Images/prediction_step5.png>
<br>
If we combine the prediction between domestic and international passenger traffic, the results become:
<img src=Images/prediction_step5_agg.png>
<br>
After we modified the model to adjust the new assumption for international passenger traffic prediction, we can see the passenger traffic is very flat between 2021 and 2023 and jumps significantly in 2024. The result for international passenger traffic prediction is not satisfing becuase we are expecting the growth should  recovery smoothly rather than all happened in one year in 2024 considing with logistic challenges the airlines and airports around the globe would have faced to up-scale the flight schedules. However, we do not know whether international travel is still restricted in 2022 and 2023 and we cannot say the result is absolutely as the reality might be it takes a year to have travellers be confident to travel internationally. Perhaps it is not a best model to forecast the combined passenger traffic between 2021 and 2024 but it could be a good reference to view when the international passenger traffic to pick up in the recovery period.

## Conclusion
I would say we have two satisfying models to predict the passenger traffic between 2021 and 2024 from step 3 and step 5. However, we have added additional assumption to prevent predict drop below 0 that add some inconsistency to Model 5. I am more confident to use Model 3 to make prediction on the SFO passenger traffic count between 2021 and 2024. Another important note, it is best not to switch back to the model trained in Part 1.1 to predict the passenger traffic in 2025 immediately because the prediction in 2025 relies on data in 2024 which is still a recovery period. The best way to do so is to predict 2025 passenger traffic using the same model in Model 3 but grab an extra year of growth pattern (Trend and seasonality between 2009-2014) and switch back to the Model trained in Part 1.1. The reason to include an additional year pattern because the Part 1.1 model prediction relies on trend and seasonality for the previous 12 months.

## Next Step
You may find the cargo tonnage to learn more about air cargo traffic during the pandemic and the prediction in [Part 3 folder](../Part3). Or you may go back to the [Main Page](../) for the other parts of the folder.