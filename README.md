# SFO Traffic

We have a data set on SFO traffic between July, 2005 and Decemeber, 2017. It includes the passenger counts on each airline every month in the given period. I have two goals:<br>
1 - Visualize the data set for EDA purpose<br>
2 - Predict the passenger traffic in 2018 and 2019 <br>

In this project, I will use R because I would like to demonstrate the functionality of ggplot and R has a better package for time series model.<br>

Noted that I have been doing EDA on this data set previously with Charles Siu. Some of the visualizations here is collaborative with him. 

## About the data set
The data set is an open source data set obtained from DataSF<br>
<a href="https://datasf.org/opendata/">Open SF</a>

The data set consists of 12 columns,<br>
the columns indicates the destination/origin with passenger counts the airline carry each month.<br>
As well as, the price type and boarding area of the airlines.<br>
<br>
In the given period, there are 17,959 observations.

## Data Cleansing
Before doing EDA, we shall change the column names for our convenience.<br>
After that, the columns we have are:<br>
1 - date<br>
2 - op_airlines<br>
3 - op_code<br>
4 - pub_airlines<br>
5 - pub_code<br>
6 - geo_summ<br>
7 - geo_region<br>
8 - type<br>
9 - price<br>
10 - terminal<br>
11 - boarding_area<br>
12 - pax_count<br>
<br>
#### Date
The date in the data set is in the format of YYYYMM, the first thing we should do is to split the year and month into two columns. That would append two more columns to the dataframe. Be sure to convert year in integer for convenience for modeling later.

#### op_airlines, op_code, pub_airlines, pub_code
Someties airlines may outsource the airplane operations to other airlines. For example, some region flights of United Airlines are operated by Skywest Airlines. While United Airlines is called published airlines, Skywest Airlines is called operation airlines. In this data set, the row for such flight, we would have Skywest Airlines in op_airlines and United Airlines in pub_airlines. op_code and pub_code are simply the IATA of operation and publish airlines.

#### geo_summ
The column indicates whether the flight is domestic or international. Flights from/to Canada are counted as international.

#### geo_region
The column indicates the region the flight is from/to.

#### type
Enplaned - Departure<br>
Deplaned - Arrival<br>
Thru/Transit - Transit flights

#### price
Low Fare or not. If the airline is not a low cost carrier, the data set indicates as "Other". We will change this to "Full Service" which is the proper term for airline contrast with low cost carrier

#### terminal
SFO has 3 domestic terminals, denoted as Terminal 1, 2, 3, and 1 international terminal, denoted as International.

#### boarding_area
The boarding_area the flight is embarked. In SFO, each terminal may have more than 1 boarding area but the boarding area code do not duplicated in other terminals.

#### pax_count
The passenger count, we can treat this as the response variable.

<br>
<br>
When we look at the data set in the previous project, we found that there are entries with inaccurate data or uncleaned data. Such as:<br>
1 - Some entries with United Airlines is recorded as United Airlines - Pre 07/01/2013<br>
2 - Emirates are typed inconsistently, some entries are typed with extra whitespace<br>
3 - Some airlines are recorded as low cost carrier but supposed to be full service ailrine, and the other way around<br>
<br>

# EDA
We have did some EDA for the data set, we have visualized:<br>
1 - Line Chart for passenger count by year <br>
2 - Bar Chart for passenger count with geo_summ by month<br>
3 - Line Chart for growth rate<br>
4 - Pie Chart for passenger type<br>
5 - Found the top 5 airlines in passenger counts by domestic and international<br>
6 - Line Chart for passenger count for domestic and international low cost carrier<br>
7 - Tree map for terminal traffic<br>
8 - Heatmap for United Passenger count<br>

# Predict the passenger traffic in 2018 and 2019
#### Problem on time series data
Autocorrelation occurs in the data set, it means that a given data point is highly correlated with data point(s) from previous period. It violates one of the assumption of linear regression, so we need to predict in other approach. In this project, I will demostrate 3 approaches.

## Approach 1: Holt-Winters
Holt-Winters Methods predicts by using exponential smoothing techniques, in other words, the model is learned by taking an exponentially weighted moving average and do not need any assumption. <br>

The model plot is learned as follow:<br>
![Screenshot](hw_plot.png)