#! /usr/bin/env python3

import numpy as np
print("Start reading in data:")
file = "airquality.csv"

dt = {'names':('measureId', 'measureName','MeasureType' , 'StratificationLevel', 'StateFips', 
    'StateName', 'CountyFips', 'CountyName', 'ReportYear', 'Value', 'Unit', 'UnitName', 'DataOrigin', 'MonitorOnly'),
    'formats':( 'U25','U200','U25','U25','U25','U25',
    'U25','U25','U25','U25','U25','U25','U25','U25')}

npdata = np.loadtxt(file,skiprows=1, dtype=dt, delimiter=',')

def get_measure_columns(measureId):
    idx = np.where(npdata['measureId'] == measureId)
    return npdata[idx]

def get_std_by_state(numpyarray, statename):
    idx = np.where(numpyarray['StateName'] == statename)
    state = numpyarray[idx]
    return np.std(state['Value'].astype(float))

def get_min_by_state(numpyarray, statename):
    idx = np.where(numpyarray['StateName'] == statename)
    state = numpyarray[idx]
    return np.amin(state['Value'].astype(float))

def get_max_by_state(numpyarray, statename):
    idx = np.where(numpyarray['StateName'] == statename)
    state = numpyarray[idx]
    return np.amax(state['Value'].astype(float))


# Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard
days_average_over_standard  = get_measure_columns('83')

# The number of days when monitored concentrations of a criteria pollutant exceed a
# National Ambient Air Quality Standard (NAAQS) is multiplied by the total number of people living in the affected area
# Number of person-days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard
person_days_average_over_standard  = get_measure_columns('84')

# Percent of days with PM2.5 levels over the National Ambient Air Quality Standard (NAAQS)
percent_days_PM_over_standard = get_measure_columns('85')

# Person-days with PM2.5 over the National Ambient Air Quality Standard
person_days_PM_over_standard = get_measure_columns('86')

# Annual average ambient concentrations of PM2.5 in micrograms per cubic meter
# (based on seasonal averages and daily measurement)
annual_average_PM_concentrations = get_measure_columns('87')
print("Reading Complete:")

print("Getting Max Values of Days over Standard")
state_names = ["Alabama",
"Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky",
"Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
"New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont",
"Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

max_over_standard_by_state = {}
std_over_standard_by_state = {}
for x in state_names:
    if not x in max_over_standard_by_state:
        max_over_standard_by_state[x] = get_max_by_state(days_average_over_standard, x)
    if not x in std_over_standard_by_state:
        std_over_standard_by_state[x] = round(get_std_by_state(days_average_over_standard, x),2)

print(std_over_standard_by_state)

