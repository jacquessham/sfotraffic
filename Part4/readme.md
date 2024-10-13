# Part 4 - SFO Insight Dashboard
The goal of Part 4 is to conduct SFO traffic analytics through display statistics and trends on GoodData dashboard. The dashboard will be provide the necessary data, data pipeline, and dashboard solution.

<br><br>
The current version only provide a one-time-data-full-load upload scripts. The improvement will be coming soon...

## Tools
Here are the tools are required to run the dashboard.
<ul>
	<li>Docker</li>
	<li>Postgres Database, v14.2</li>
	<li>GoodData Cloud Native Community Edition (>v2.0), the setup will install the latest version</li>
	<li>Python</li>
</ul>


## Instruction
### Initiation
First, initiate GoodData.CN and Postgres database via Docker with the following command (The defintion is defined at <i>docker-compose.yml</i>):

```
sh initate.sh
```

<br>
GoodData.CN may take some time to set up. Once GoodData.CN and Postgres are setup,
run the following command:

```
sh setup_sfodb.sh
```

<br>
By running this script, it will automatically set up the data pipeline ingest, load, and transform the data to the output stage, and set up the workspace in GoodData. Once it is done, you may get to GoodData.CN's <i>SFO Staistics</i> workspace.


### Data Refresh
Currently the pipeline is only able to initiate the database and an one-time-data-full-load. The feature of the data pipeline on data refresh will be developed in the future version. Stay tuned!


## Data Model
The data model used in the workspace look like this:
<img src=gooddata/ldm.png>

<br><br>
There are 3 core fact tables on Passenger Traffic, Cargo Traffic, and Landing Traffic, and dimsional tables with shared attributes. As the data of 3 datasets came from 3 denormalized files, the transformation would have done in the Postgres database.

### Data Pipelines
Currently the pipeline is only able to initiate the database and an one-time-data-full-load. The data pipeline for data refresh is still in progress. 
<br><br>
You should fill out <i>elt_params.json</i> before running the initiation. There are 2 required columns:
<ul>
	<li>upload_file</li>
	<li>dataset</li>
</ul>
<br>
Both columns are arrays. In both columns, you may state the location of the dataset and the dataset type. It is expecting 3 dataset and <i>dataset</i> is expecting 3 following elements:
<ul>
	<li>pax (Passenger)</li>
	<li>cargo (Cargo)</li>
	<li>landing (Landing)</li>
</ul>
<br>
You are expected to state the location and dataset type in the same position in both array. The example is:

```
{
	"upload_file":["../../Data/Air_Traffic_Passenger_Statistics_2022.csv","../../Data/Air_Traffic_Cargo_Statistics_2020.csv","../../Data/Air_Traffic_Landings_Statistics_2020.csv"],
	"dataset":["pax","cargo","landing"]
}
```
<br>
The column <i>upload_tag</i> is optional and it is now not used in the data pipeline but you may expect it can be utilize in the future.


## Gallery
<img src=gooddata/dashboard1.png>
<img src=gooddata/dashboard2.png>
