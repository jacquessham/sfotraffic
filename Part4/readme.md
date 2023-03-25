# Part 4 - SFO Insight Dashboard
Coming soon...

## Tools
<ul>
	<li>Postgres Database</li>
	<li>GoodData Cloud Native Community Edition (>v2.0)</li>
	<li>Python</li>
</ul>

<br>
Coming soon...

## Instruction
### Initiation
First, initiate GoodData.CN and Postgres database via Docker with the following command:

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
<br><br>
Coming soon...

### Data Refresh
Coming soon...



## Data Model
The data model used in the workspace look like this:
<img src=gooddata/ldm.png>

<br><br>
There are 3 core fact tables on Passenger Traffic, Cargo Traffic, and Landing Traffic, and dimsional tables with shared attributes. As the data of 3 datasets came from 3 denormalized files, the transformation would have done in the Postgres database.

### Data Pipelines
Coming soon...

## Gallery
<img src=gooddata/dashbaord1.png>
<img src=gooddata/dashboard2.png>
