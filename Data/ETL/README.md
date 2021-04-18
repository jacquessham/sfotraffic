# ETL folder
The purpose of the ETL script is to transform the original data sets to 2 data sets for EDA and predictive model training as the original data is a transactional data set. 

## Files
This folder contains the following scripts:
<ul>
	<li>etl_original.py</li>
	<li>etl_2020.py</li>
</ul>

The file <i>etl_original.py</i> transforms the original data in <i>Air_Traffic_Passenger_Statistics.csv</i> into <i>sfopax_eda.csv</i> and <i>sfopax_month.csv</i>, which is the data sets for EDA and predictive model training in Part 1.1, respectively, in the [Data folder](../).
<br><br>
The file <i>etl_2020.py</i> transforms the original data in <i>Air_Traffic_Passenger_Statistics_2020.csv</i> into <i>sfo2020pax_eda.csv</i> and <i>sfo2020pax_month.csv</i> in the [Data folder](../).

## Transformation
### etl_original.py
The transformation is drove by <i>etl_original.py</i> which relies on <i>pandas</i>. The script first load the [original data set](../Air_Traffic_Passenger_Statistics.csv) and rename the column names like in [Part 1](../../Part1), but since operating airlines columns are not utilized, so we have dropped 2 columns related to that. The columns is the same as we have used in Part 1, as follows:
<ul>
<li>date</li>
<li>pub_airlines</li>
<li>pub_code</li>
<li>geo_summ</li>
<li>geo_region</li>
<li>type</li>
<li>price</li>
<li>terminal</li>
<li>boarding_area</li>
<li>pax_count</li>
</ul>
<br>
Note that <i>op_airlines</i> and <i>op_code</i> are the columns dropped in this script. You may find about the columns in the [Data folder](../).

<br><br>
As mentioned in [Part 1](../../Part1), there are inconsistency or inaccurated data in the original data set:
<ol>
<li>Some entries with United Airlines is recorded as United Airlines - Pre 07/01/2013</li>
<li>Emirates are typed inconsistently, some entries are typed with extra whitespace</li>
<li>Some airlines are recorded as low cost carrier but supposed to be full service ailrine, and the other way around.</li>
</ol>
<br>
The script would cleanse the data by doing the following:
<ol>
	<li>Unify the <i>United Airlines</i> entries, make any entry related to United Airlines to have a consistent record in the airline columns.</li>
	<li>Omit the extra whitespace in any <i>Emirates</i> entry in the airline columns.</li>
	<li>Reclassify the wrongly identified airlines in the price categories</li>
</ol>
<br><br>
Once the data cleansing steps have been taken, the script would convert the date column from the <i>YYYYMM</i> format to <i>YYYY-MM-DD</i> and set the date entry to the last day of the month. For instance, if the entry is August, 2016, then it would convert to 2016-08-31. This format would be convenient for storing and visualization.
<br><br>
After all the steps have been processed, the script would save the file to <i>sfopax_eda.csv</i> which is the file is for EDA but not for the model training.
<br>
The script would take extra step to aggregate passenger count by month/year and save the file to <i>sfopax_month.csv</i> for predictive model training.

### etl_2020.py
<i>etl_2020.py</i> has the same function as <i>etl_original.py</i> to transform <i>Air_Traffic_Passenger_Statistics_2020.csv</i> into <i>sfo2020pax_eda.csv</i> and <i>sfo2020pax_month.csv</i>, except it contains the extra transformation as below:
<ol>
	<li>Unify the <i>Icelandair</i> entries, make any entry related to Icelandair to have a consistent record</li>
	<li>Unify the <i>Delta Air Lines</i> entries, make any entry related to Delta Air Lines to have a consistent record</li>
	<li>Reclassify <i>Norwegian Air</i> to low cost carrier</li>
</ol>

## Part 1.1
Once the data sets are prepared and saved in the [Data Folder](../). We may explore the data set in the [Part 1.1 EDA folder](../Part1_1/EDA/) or the prediction in the [Part 1.1 folder](../Part1_1/).

