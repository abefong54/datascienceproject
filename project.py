#! /usr/bin/env python3

import numpy as np
print("Start reading in data:")
file = "airquality.csv"

dt = {'names':('measureId', 'measureName','MeasureType' , 'StratificationLevel', 'StateFips', 
    'StateName', 'CountyFips', 'CountyName', 'ReportYear', 'Value', 'Unit', 'UnitName', 'DataOrigin', 'MonitorOnly'),
    'formats':( 'U25','U200','U25','U25','U25','U25',
    'U25','U25','U25','U25','U25','U25','U25','U25')}


npdata = np.loadtxt(file,skiprows=1, dtype=dt, delimiter=',')

def getMeasureColumns(measureId):
    idx = np.where(npdata['measureId'] == measureId)
    return npdata[idx]

def getMaxInState(numpyarray, statename):
    idx = np.where(numpyarray['StateName'] == statename)
    state = numpyarray[idx]
    return np.amax(state['Value'].astype(float))


# Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard
days_average_over_standard  = getMeasureColumns('83')

# The number of days when monitored concentrations of a criteria pollutant exceed a
# National Ambient Air Quality Standard (NAAQS) is multiplied by the total number of people living in the affected area
# Number of person-days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard
person_days_average_over_standard  = getMeasureColumns('84')

# Percent of days with PM2.5 levels over the National Ambient Air Quality Standard (NAAQS)
percent_days_PM_over_standard = getMeasureColumns('85')

# Person-days with PM2.5 over the National Ambient Air Quality Standard
person_days_PM_over_standard = getMeasureColumns('86')

# Annual average ambient concentrations of PM2.5 in micrograms per cubic meter
# (based on seasonal averages and daily measurement)
annual_average_PM_concentrations = getMeasureColumns('87')
print("Reading Complete:")




print("Getting Max Values of Days over Standard")
state_names = ['Alabama','Alaska','Arkansas']
max_over_standard = {}
for x in state_names:
    if not x in max_over_standard:
        max_over_standard[x] = getMaxInState(days_average_over_standard, x)

print(max_over_standard)


