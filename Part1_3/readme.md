# Part 1.3 Finalize SFO Passenger Traffic Prediction Model for Production
Part 1.3 will finalize the scripts in order to make prediction after downloading a dataset from <a href="https://data.sfgov.org/Transportation/Air-Traffic-Passenger-Statistics/rkru-6vcg">OpenSF</a>. The scripts will clean the dataset and display the prediction without any manual after input the required parameters.

## Instruction
After downloading the dataset from OpenSF, fill in the file directory and the desire prediction period in month in <i>params.json</i>. An example is:

```
{
	"file":"../Data/Air_Traffic_Passenger_Statistics.csv",
	"pred_period":36,
	"result_export_csv":true
}
```
<br>
By inputing the above example, the script will predict the passenger traffic 36 months after the last provided month/year provided in the dataset. The script only make monthly prediction. Please also refer to the <i>Files</i> section for instruction on filling out the <i>params.json</i> file.
<br><br>
Once <i>params.json</i> is filled, run

```
python sfo_pred.py
```

and the script will make the prediction and visualize automatically. The prediction will also be saved in your current directory if you indicate to export the prediction.
<br><br>
The visualization of this example looks like this:
<img src=result_example.png>

## Files
### params.json
This JSON file provides the inputs of how the program would run. You must fill in the following inputs:
<ul>
	<li>file: The dataset directory, only use the dataset downloaded from the OpenSF link</li>
	<li>pred_period: Months of prediction you want to make. You must enter an integer here.</li>
	<li>result_export_csv: Indicate whether if you want to export the prediction in CSV. If so, enter <i>true</i></li>
</ul>

### sfo_pred.py
The driver script to trigger the data cleaning phase, prediction phase, and the visualization phase. Each phase will call functions from <i>etl_prod.py</i>,<i>hw_prod.py</i>,<i>viz_prod.py</i>, respectively.

### etl_prod.py
This script is response to read the dataset, clean the dataset, and transform to the format for prediction phase.

### hw_prod.py
This script takes the transformed data to train the predictive model with Holts-Winter method (Multiplicative Model), which is the model picked in [Part 1.1](../Part1_1). You have to indicate the <i>pred_period</i> to indicate the months of prediction you want to make. <b>The recommended period is 24 months</b> and the model becomes less accurate when the predictive period is getting longer.
<br><br>
Note: This script does not take in any economic shock into account, such as The 2020-2022 Pandemic. 

### viz_prod.py
This script visualize the dataset downloaded from OpenSF and the prediction.

## Limitations
### Not Handling the 2020-2022 Pandmic Shock
The scripts do not take account of any ecoomic shock into account, such as The 2020-2022 Pandemic. Any sudden dramatic drop in passenger count would disrupt the predictive model. The model does not take account of long-term steady state nor rapid recovery. In order to have the prediction fix this flaw, please find the solution in [Part 2.2 folder](../Part2_2).
