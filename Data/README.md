# Data


## Original Data Set (For Part 1)
The data set is an open source data set obtained from DataSF<br>
<a href="https://datasf.org/opendata/">Open SF</a>

The data set consists of 12 columns,<br>
the columns indicates the destination/origin with passenger counts the airline carry each month.<br>
As well as, the price type and boarding area of the airlines.<br>
<br>
In the given period, there are 17,959 observations.

The columns consists of:
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
The passenger count, the column may be treated as the response variable.

<br>
<br>
When we look at the data set in the previous project, we found that there are entries with inaccurate data or uncleaned data. Such as:<br>
1 - Some entries with United Airlines is recorded as United Airlines - Pre 07/01/2013<br>
2 - Emirates are typed inconsistently, some entries are typed with extra whitespace<br>
3 - Some airlines are recorded as low cost carrier but supposed to be full service ailrine, and the other way around<br>
<br>