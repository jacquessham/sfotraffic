# Part 1.2 SFO Passenger Traffic Prediction Result Verification
The goal of Part 1.2 is to compare the result of the prediction made in Part 1.1 with the real world data. Since Part 1.1 only focus on the result between 2018-2019, the model has no data disruption caused by the pandemic.

## About the Data set
We have excluded the data beyond 2019 as this is the goal was to predict the passenger traffic rate in 2018-2019, as stated in Part 1.1. Therefore, the predictive model is not disrupted by the 2020-2022 pandemic. 


## The Result
The R-square score is 0.8502.
<br><br>
<img src=result_part1_1.png>
<br><br>
It turns out the result is very accurate in terms of R-square socre as it explains 85% of the observed data. If we look at the visualization of the prediction vs real world data, we can conclude the 1st year prediction is very accurate and the accuracy rate starts to fall in the 2nd year. We can say that this is a very good predictive model.

## The Next Step
In [Part 1.3](../Part1_3), we will write the production script which can ingest new data downloaded from OpenSF and make prediction based on this predictive model (Without taking the pandemic shock in account, it will be done in [Part 2.2](../Part2_2)).

