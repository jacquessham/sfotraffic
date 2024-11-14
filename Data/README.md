# Data

In this folder consists of the original data sets, tranformed data sets, and ETL scripts for all parts of this project. The following is the list of data files contained in this folder:
<ul>
	<li>Air_Traffic_Passenger_Statistics.csv</li>
	<li>sfopax_eda.csv</li>
	<li>sfopax_month.csv</li>
	<li>Air_Traffic_Passenger_Statistics_2020.csv</li>
	<li>Air_Traffic_Cargo_Statistics_2020.csv</li>
	<li>Air_Traffic_Cargo_Statistics_2024.csv</li>
	<li>Air_Traffic_Landings_Statistics_2020.csv</li>
</ul>

## Raw Passenger Traffic Data Set
The following files are categorized as raw data set as they are in the original format from the source:
<ul>
	<li>Air_Traffic_Passenger_Statistics.csv</li>
	<li>Air_Traffic_Passenger_Statistics_2020.csv</li>
</ul>

The data sets are open source data set obtained from <a href="https://datasf.org/opendata/">Open SF</a> and the page about this data may be found in this <a href="https://data.sfgov.org/Transportation/Air-Traffic-Passenger-Statistics/rkru-6vcg">page</a>. <i>Air_Traffic_Passenger_Statistics.csv</i> is used for Part 1 without ETL process but both <i>Air_Traffic_Passenger_Statistics.csv</i> and <i>Air_Traffic_Passenger_Statistics_2020.csv</i> has been transformed for Part 1.1.

The data set consists of 12 columns, the columns indicates the destination/origin with passenger counts the airline carry each month, and the price type and boarding area of the airlines. 

<br><br>
<i>Air_Traffic_Passenger_Statistics.csv</i> was downloaded in 2018 and contains 17,959 observations between May, 2005 and December, 2017. <i>Air_Traffic_Passenger_Statistics_2020.csv</i> was downloaded in 2021 and contains 22,869 observations between May, 2005 and December 2020.

The columns consists of:
<ul>
	<li>Activity Period</li>
	<li>Operating Airline</li>
	<li>Operating Airline IATA Code</li>
	<li>Published Airline</li>
	<li>Published Airline IATA Code</li>
	<li>GEO Summary</li>
	<li>Activity Type</li>
	<li>Price Category</li>
	<li>Terminal</li>
	<li>Boarding Area</li>
	<li>Passenger Count</li>
</ul>
<br>
In Part 1, in both EDA and model training R script have converted the column names to the following column names, respectively:
<br><br>

<ul>
<li>date</li>
<li>op_airlines</li>
<li>op_code</li>
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

### Columns explanations
#### Date
The date in the data set is in the format of YYYYMM.

#### op_airlines, op_code, pub_airlines, pub_code
Sometimes airlines may outsource the airplane operations to other airlines. For example, some region flights of United Airlines are operated by Skywest Airlines. While United Airlines is called published airlines, Skywest Airlines is called operation airlines. In this data set, the row for such flight, we would have Skywest Airlines in op_airlines and United Airlines in pub_airlines. op_code and pub_code are simply the IATA of operation and publish airlines.

#### geo_summ
The column indicates whether the flight is domestic or international. Flights from/to Canada are counted as international.

#### geo_region
The column indicates the region the flight is from/to.

#### type
Enplaned - Departure<br>
Deplaned - Arrival<br>
Thru/Transit - Transit flights<br>
<br>
Note that Thru/Transit is not used consistently.

#### price
Low Fare or not. If the airline is not a low cost carrier, the data set indicates as "Other". We will change this to "Full Service" which is the proper term for airline contrast with low cost carrier

#### terminal
SFO has 3 domestic terminals, denoted as Terminal 1, 2, 3, and 1 international terminal, denoted as International.

#### boarding_area
The boarding_area the flight is embarked. In SFO, each terminal may have more than 1 boarding area but the boarding area code do not duplicated in other terminals.

#### pax_count
The passenger count, the column may be treated as the response variable.


## Transformed Passenger Traffic Data Set
The following files are categorized as Transformed Passenger Traffic data set as they have been transformed and cleansed:
<ul>
	<li>sfopax_eda.csv</li>
	<li>sfo2020pax_month.csv</li>
	<li>sfopax_eda.csv</li>
	<li>sfo2020pax_month.csv</li>
</ul>
Part 1.1 used the same data set as Part 1 except we have transform the original Part 1 data set to an aggregated version. You may find the ETL code in the <a href="https://github.com/jacquessham/sfotraffic/tree/master/Data/ETL">ETL folder</a>. By transforming the original data set, the Part 1.1 model training script need not to aggregate the raw data set for model training. The ETL code in the ETL folder transform <i>Air_Traffic_Passenger_Statistics.csv</i> to <i>sfopax_eda.csv</i> and <i>sfopax_month.csv</i>.
<br><br>
Likewise, the ETL code in the ETL folder transform <i>Air_Traffic_Passenger_Statistics_2020.csv</i> to <i>sfo2020pax_eda.csv</i> and <i>sfo2020pax_month.csv</i>. You may find the ETL code in the <a href="https://github.com/jacquessham/sfotraffic/tree/master/Data/ETL">ETL folder</a>.


## Cargo Data Set
The data set is an open source data set obtained from <a href="https://datasf.org/opendata/">Open SF</a> and the page about this data may be found in this <a href="https://data.sfgov.org/Transportation/Air-Traffic-Cargo-Statistics/u397-j8nr">page</a>. The data set is intended to be used for Part 3.

## Air Traffic Landings Data Set
The data set is an open source data set obtained from <a href="https://datasf.org/opendata/">Open SF</a> and the page about this data may be found in this <a href="https://data.sfgov.org/Transportation/Air-Traffic-Landings-Statistics/fpux-q53t">page</a>. The data set is intended to be used for future data visualization purpose.