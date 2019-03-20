# Self Check circulation dataset processing

## Convert the Self Check XML to aggregated CSV

### Goal 
Process the XML files into a python object
Break out the statistics for each day or hour 

### Purpose 
Provides Hourly and Daily KPIs for the library Self-Check stations

### Methodology 
1. Library staff person downloads appropriate XML file from Bibliotheca web portal on a regular schedule
2. Library staff person saves file to a predetermined folder on \\chfs
3. OD script pulls file from folder, appends to existing file
4. OD process the XML files into a python object 
5. OD loads to ODS and publishes on a regular schedule

### Data Source
Library staff downloads appropriate XML file from Bibliotheca web portal on a regular schedule
file is stored at ```\\chfs\...```
### Output 
A csv file is stored at ```\\chfs\...```
### Transformations
Output is limited to Library Open Hours, which is stored in the code as a Dictionary - library_hours

### Constraints
#### Library Open Hours
Changes to Library Open Hours currently requires a code change.
Suggest creating a CLASS in a common import library to create a single changepoint for building open hours
#### XML structure changes
Changes to the Bibliotheca XML file structure will require remapping the variables.
#### Input/Output Files
Locations of the Input and Output files are included in the code. Suggest parameterizing this information.
#### Libraries Required
This script requires the [untangle](https://untangle.readthedocs.io/en/latest/) library via ```pip3 install untangle``` in the run environment

