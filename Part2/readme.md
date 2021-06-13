# Part 2 - Predict Passenger Traffic in SFO after the 2020-2021 Pandemic
Part 2 is the effort to follow up the disruption of 2020-2021 Pandemic to predict the growth pattern of the passenger traffic once the pandemic is over using the latest data available. In this part, I will achieve the goals using Python.

## About the Data Set
The data set is an open source data set obtained from <a href="https://datasf.org/opendata/">Open SF</a>. It consists of 12 columns with XX,XXX observations. For the convenience, the data set is cleansed and transformed for this part in the ETL process with <i>etl_2020.py</i>. The ETL process returns 2 csv files, <i>sfo2020pax_eda.csv</i> for EDA and <i>sfo2020pax_month.csv</i> for model training. You may find more detail about the original data set, transformed data sets, and the ETL scripts in the [Data Folder](../Data). The data set is a time series data, and therefore, there are constraints to what we can do as some approches may violate some assumptions on certain algorithms, such as linear regression.

## Goal
The goal of this part of the project is to utilize the data set to predict the passenger traffic pattern until the passenger traffic level is return to pre-pandemic level (2019).

## Plan and Approach
Coming Soon...

## Files
In this part, the folder contains the following files:
<ul>
	<li>predict_draft.py</li>
	<li>predict.py</li>
	<li>vis_pred.py</li>
</ul>

## Data Cleansing
Coming Soon...

## EDA
There are more data available comparing the data set used in Part 1/Part 1.1 because the data set used in this part is downloaded in 3 years after the Part 1 is conducted. You may find the passenger traffic insight between 2005 and 2020 in the <a href="https://github.com/jacquessham/sfotraffic/tree/master/Part2/EDA">EDA folder</a> before learning the prediction model.

## Prediction
Coming Soon...

## Next Step
You may find the cargo tonnage to learn more about air cargo traffic during the pandemic and the prediction in [Part 3 folder](../Part3). Or you may go back to the [Main Page](../) for the other parts of the folder.