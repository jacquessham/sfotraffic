# EDA

We have a data set on SFO traffic between July, 2005 and Decemeber, 2017. It includes the passenger counts on each airline every month in the given period. The data set consists of 12 columns with 17,959 observations, and you may find more detail about the data set in the [Data Folder](../../Data). I have been doing EDA on this data set previously with <a href="https://github.com/chunheisiu">Charles Siu</a>. Some of the EDA visualizations in here is collaboration with him.
<br><br>

## Overview
1 - Line Chart for passenger count by year <br>
![Screenshot](Images/line_annual_pax_count.png)<br>
In the last 10 years, we can see there is a steady growth in passenger traffic in SFO overall.
<br><br>
2 - Bar Chart for passenger count with geo_summ by month<br>
![Screenshot](Images/bar_pax_count.png)<br>
We can see there is about 20% of the passengers in SFO are international travellers (Including passengers from/to Canada) while the remaining proportions are domestic travellers. The passenger traffic has a more consistent pattern, it indicates international flights has less seasonality effection. 

## Passenger Growth
3 - Line Chart for growth rate<br>
![Screenshot](Images/line_growth.png)<br>
The growth rate in the past 10 years remain in the positive terrority, ranging from 0.5% to 8.5% growth. It suggests the passenger traffic growth is less sensitive to economic downturns since we know that there are a couple years some airports experience negative growth in a economic recession.

## Passenger Demographics
4 - Pie Chart for passenger type<br>
![Screenshot](Images/pie_activity.png)<br>
There is no surprise there are roughly 50-50 distribution on departure and arrival. Note that there are 0.3% airplanes are transit flights because of data inconsistency. We do not have any information on the definition of transit flights. However, since the airplane activity does not affect our prediction so we may ignore the discrepancy.
<br><br>
5 - Bar Chart for passenger count for international low cost carrier<br>
![Screenshot](Images/bar_intl_lcc.png)<br>
There is a rapid growth in passenger traffic in international low cost flights, provided by WestJet (Canada), Wow Air (Iceland), and XL Airways France. 
<br><br>
## Terminal Usage
6 - Tree map for terminal traffic<br>
![Screenshot](Images/tree_dom_terminal.png)<br>
This is the distribution of the passenger traffic by terminal and airlines, we can see most of the SFO passengers take the United flights in terminal 3, followed by American Airlines, Southwest Airlines, Delta Airlines.

## Largest Stalkholder
7 - Heatmap for United Passenger count<br>
![Screenshot](Images/heat_map.png)<br>
From the tree map we have seen, we have learnt United Airlines is the largest stalkholder in SFO. Let's drill down the passenger count with United flights: we can see the colour turn from yellow to red in a steady increasingly pace in the last 10 years.

## Prediction
You may go back to the [Part 1 folder](../) to learn more about the prediction model and its result.