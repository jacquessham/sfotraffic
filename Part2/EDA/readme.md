# EDA
This EDA is trying to any insight that may contribute to make prediction in Part 2 using the data set on SFO passenger traffic between July, 2005 and December, 2020.

## Files
Here are the Python scripts to create visualiztions:
<ul>
	<li>AnnualPax2020_Line.py</li>
	<li>AnnualTypePax2020_Bar.py</li>
	<li>AnnualTypePax2020_Line.py</li>
	<li>GrowthRate2020_Line.py</li>
	<li>NormalizeAnnualPax2020_Line.py</li>
	<li>NormalizeGrowthRate2020_Line.py</li>
</ul>

### Package Used
The scripts above used the following packages:
<ul>
	<li>pandas</li>
	<li>plotly</li>
</ul>
pandas is used for data management and Plotly is used for generating the chart. Each script uses plotly.graph_objs to generate the charts and save the chart in html. Once the chart is save and displayed in html, it requires users to download the chart from the html page manually.

## Result
The Pandemic started in March, 2020 as the lockdown of San Francisco Bay Area started in the same month. The passenger traffic has experienced a steady growth between 2017 and 2019. However, the passenger traffic has a obvious drop in February as the passenger traffic has halved between January, 2020 and February, 2020 in the line chart below.
<img src=Images/monthpax_line.png>
<br>
The line chart above has displayed the monthly passenger traffic and the moving average of the monthly passenger traffic by 12 months. The moving average smoothens the seasonality affect and allow us to focus to look at the passenger traffic trend. In order to reference the recovery of passenger traffic, we can observe the growth trend in the last financial crisis. The Great Recession occurs between 2018 Q3 and 2019 Q2, and we can observe the passenger traffic in the nearby period. If we look at the line chart above, the moving average has a negative growth around 2018 Q3 and started to go back to a positive growth path until the peak in 2012 Q4. Since then, there were no negative growth. The trend between 2012-2013 and between 2018-2019 is flat that it is not considered as negative growth. Therefore, we only have 1 recovering period to reference, which takes about 4 years (2009-2013) the passenger traffic trend to grow.
<br>
<img src=Images/monthlygrowth_line.png>
The above chart shows the monthly growth rate of passenger traffic and it is best to show the seasonality of passenger traffic. The growth rate moving average is slightly above 0 and it does not show too much insight about the trend.
<br><br>
When the pandemic started, governments worldwide prohibit international travellers to enter to its border that international passenger traffic plunge significantly.
<br>
<img src=Images/dom_intl_pax_line.png>
Even before the pandemic has started, international travellers only accounts for a small portions of the passenger traffic in SFO, about 20% found in Part 1. In February and March 2020, the international passenger traffic dropped closed to 0, the portion of the international passengers may only account 10% after lockdown in 2020. Beside 1 of the months in 2020, none of the months in 2020 has a monthly passenger traffic more than 1 million, which is never seend in the data set prior to 2020.
<br>
To drill in to the period between 2019-2020 to observe the contrast the passenger traffic pre-pandemic and pandemic period, below is the bar chart:
<img src=Images/dom_intl_pax_bar.png>

## Next Step
You may click [here](../) to learn more about the predictive model and the prediction.