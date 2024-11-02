# EDA
We have the data between July, 1999 and July, 2024. It includes the cargo tonnages on each airline every month in the given period. There are 55,542

## Overview
1 - Line Chart for Cargo Tonnage by Year
<br>
<img src=annual_tonnage.png>
<img src=annual_tonnage_rollavg.png>


<br>
Since 2005, the cargo tonnage dropped significantly for 10 years. Even it barely recovers after 2015, but overall the tonnage trend is trending downward.

<br><br>
2 - Bar Chart for Cargo Tonnage along with Destination by Month

<br>
<img src=monthly_tonnage.png>
<br>
We see the monthly average cargo tonnage is relatively consistent, especially on domestic flights. The international cargo traffic is lower in Q1, but consistent for the reminding of the year. It indicates cargo tonnage is very insensitive to the seasonality effect and international trade is only relatively slow in Q1. 

## Cargo Segmentation
3 - Cargo Type Breakdown

<br>
<img src=percent_cargo.png>
<br>
We saw majority of the cargo traffic is classified as "Cargo", which accounted for 86.6%. For more time-senitive cargo, Mail cargo was accounted for 10.1% and 3.3% for Express cargo of the total cargo traffic.

<br><br>
4 - Aircraft Types

<br>
<img src=aircraft_v_cargo.png>
<br>
It might be a surprise to most people that most of the cargo was transported by passenger flights, about 68% of the cargo tonnage. Only 31% of the cargo traffic was transported by freighter flights. There are very little cargo was transported by Combi fligths, as very few airlines operate combi aircrafts (Such as Alaska Airlines or KLM in the past, but neither of them has operated Combi flights in the last 20 years to SFO).


## Top 5's
5 - Domestic and International Top 5 Cargo Operators
<br><br>
The top 5 domestic cargo operators in SFO are <b>ABX Air</b>, <b>Delta</b>, <b>American</b>, <b>Fedex</b>, and <b>United</b>.
<br>
While the top 5 international cargo operators in SFO are <b>JAL</b>, <b>China Airlines</b>, <b>EVA Air</b>, <b>Korean Airlines</b>, and <b>United</b>.

## Top Operator
6 - ABX Air's Tonnage between 2010 and 2023
<br>
<img src=abx_air_tonnage.png>

<br>
ABX Air's Tonnage steadily grew month-by-month, and does not seem to have an seasonality effect based on the heatmap. The tonnage jumped significantly after 2016. ABX Air seems to receive contract from DHL for US domestic service, the tonnage continues to grow in the future due to the expectation on growth on e-commerce's shipping service.