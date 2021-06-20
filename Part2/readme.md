# Part 2 - Predict Passenger Traffic in SFO after the 2020-2021 Pandemic
Part 2 is the effort to follow up the disruption of 2020-2021 Pandemic to predict the growth pattern of the passenger traffic once the pandemic is over using the latest data available. In this part, I will achieve the goals using Python.

## About the Data Set
The data set is an open source data set obtained from <a href="https://datasf.org/opendata/">Open SF</a>. It consists of 12 columns with 22,869 observations. For the convenience, the data set is cleansed and transformed for this part in the ETL process with <i>etl_2020.py</i>. The ETL process returns 2 csv files, <i>sfo2020pax_eda.csv</i> for EDA and <i>sfo2020pax_month.csv</i> for model training. You may find more detail about the original data set, transformed data sets, and the ETL scripts in the [Data Folder](../Data). The data set is a time series data, and therefore, there are constraints to what we can do as some approches may violate some assumptions on certain algorithms, such as linear regression.

## Goal
The goal of this part of the project is to utilize the data set to predict the passenger traffic pattern until the passenger traffic level is return to pre-pandemic level (2019).

## Plan and Approach
We will first make prediction using traditional time-series statistical learning. The disruption of the passenger traffic comes from an extreme economic shock due to the outbreak of pandemic and believe to be rebounded to pre-pandemic level after the disruption has ended. Traditional time-series models may not make useful prediction as the disruption has been happening long enough that using autoregressive integrate moving average models or any approach heavily rely on 2018-2020 data will not return prediction with rebound momentum. If the prediction is not useful for our goal, we may find different approach to make the prediction to our goal.

## Files
In this part, the folder contains the following files:
<ul>
	<li>prophet_predict.py</li>
	<li>predict_draft.py</li>
	<li>predict.py</li>
	<li>vis_pred.py</li>
	<li>draft_vis_pred.py</li>
	<li>multi_vis_pred.py</li>
	<li>multi_vis_pred_v2.py</li>
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
The rumor of an outbreak of coronavirus in a certain Asian country started in Q4 2019 and had developed to a global scale outbreak in Q1 2020. A couple months later, global air travel came to an half in March, 2020 when effectively all international travels are banned among countries. All counties in the San Francisco Bay Area locked down since mid-March 2020 and passenger traffic has been plunged to the level never seen in the data set since then.
<br>
Our goal is to utilize the data set to predict the passenger traffic pattern until the passenger traffic level is return to pre-pandemic level (2019). Let's assume January, 2021 is the first month the air traffic resume in order to make it simple since our data ends in December, 2020. The first approach is to use traditional time-series statistical learning to predict the rebounded passenger traffic, to do this, we can use Generalized Additive Model (GMA, Here we are using Facebook Prophet) to predict. As we have mentioned in the EDA phase, we observe the recovering period takes about 4 years: So, we can use the existing data to predict the traffic during 2021-2024.
<br>
<img src=Images/predict_prophet.png>
<br>
Our assumption of the prediction is that the passenger traffic dropped in 2020 is caused by an extreme demand shock in air traffic due to the restriction on air traffic that is not caused by economic activities. According to the Solow Model learned in Econ 101, we believe the economy is behind the steady state as the Model suggested; it means the economic growth is not in pace with the long-term growth due to the shut down of economic activities, once the economic activities are back to normal, the economic growth will be bounding back to the original pace. Therefore, we believe once air travel is back to normal, the passenger traffic will be bounding back to the 2019 level and continue the long-term growth. 
<br>
The flaw of using GMA is that it heavily rely on previous periods for prediction, so it may not be helpful for our goal. Looking at the result above, the concern is valid: We can see the passenger traffic jumps up dramatically and the trend between 2021-2024 is dropping that the result is against our assumption. 
<br>
We believe the passenger traffic will spend about 4 years to recover similar to the pace between 2009-2013 as this is the only recover pace we found in EDA, we will use this pattern to predict the trend of passenger traffic between 2021-2024. We can take the Janurary, 2009 as base index to obtain the index of the next 4 years, like below:
<img src=Images/recover_path.png>
<br>
Having the trend between 2009-2013 convert to index, we can use this trend index to predict the passenger traffic between 2021-2024. For the prediction, we will set Janurary, 2021 as the base month and December, 2024 as the peak. If we apply this method, the prediction will looks like this:
<img src=predict_raw.png>

## Next Step
You may find the cargo tonnage to learn more about air cargo traffic during the pandemic and the prediction in [Part 3 folder](../Part3). Or you may go back to the [Main Page](../) for the other parts of the folder.