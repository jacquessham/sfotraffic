# SFO Passenger Traffic Prediction

This is a project to analyze the passenger traffic in San Francisco International Airport (SFO). We are going to drill in the insight of the passenger traffic in SFO and make prediction of the passenger traffic in different period of time. This project was originally conducted in 2019, which is now the Part 1 of this project. Because of the 2020-2021 Pandemic disrupted the global passenger traffic, the prediction is not valid anymore. Therefore, I have restructed this project and start an effort to follow up the project (Part 1) for the passenger traffic after the pandemic is over.

## Data
The data set is an open source data set obtained from <a href="https://datasf.org/opendata/">Open SF</a>. In the [Data Folder](/Data), it consists all original data sets, transformed data sets, and ETL scripts for all parts of this project.

## Part 1
Part 1 was the original work conducted in 2019. The primary goal of this project was to make prediction of passenger traffic between 2018-2019 with 2005-2017 data. Besides that, I have also compared the prediction accuracy between the packages available in R and Facebook Prophet (Which is the newly released time-series statistical-learning package in 2019). You may find more detail in the [Part 1 folder](/Part1).

## Part 1.1
Part 1.1 follows up the Part 1 with updated code in Python. The primary goal is the same to make prediction of passenger traffic between 2018-2019 with 2005-2017 data but using Python only. The EDA is also redone with Python packages instead of ggplot in R. You may find more details in the [Part 1.1 folder](/Part1_1).
<br><br>
I have also used the real world data between 2018-2019 to verify the accuracy of the predictive model built in Part 1.1. The accuracy rate is <b>0.8502</b>. You may find more details in the [Part 1.2 folder](/Part1_2).
<br><br>
In the [Part 1.3 folder](/Part1_3), we will build the production predictive model which takes fresh downloaded data and make prediction. Note that this model will not take the 2020-2022 pandemic into account, the refined model can be found in the [Part 2.2 folder](/Part2_2).

## Part 2
Part 2 is the effort to follow up the disruption of 2020-2022 Pandemic to predict the growth pattern of the passenger traffic once the pandemic is over. You may find more details in the [Part 2 folder](/Part2) to find how does the path of recovering path looks like.
<br><br>
I am going to use the real world data between 2021 and Jun,2022 to verify they accuracy of the predictive model built in Part 2. You may find more details in in the [Part 2.1 folder](/Part2_1).
<br><br>
In the [Part 2.2 folder](/Part2_2), we will revisit the model in Part 2.1 and build the production predictive model which takes fresh downloaded data and make prediction during the recovery and beyond.

## Part 3
In Part 3, we would expand our scope to cargo operation in SFO and predict the cargo traffic. You may find more details in the [Part 3 folder](/Part3). Coming Soon...

## Part 4
In Part 4, we are going to utilize <i>GoodData Cloud Native Community Edition</i> to visualize the insight on all avaiable data. You may find more details in the [Part 4](/Part4). The current solution is sufficient for basic analytics use, but only capcable to ingest data once. The improved version will be available in the future release.