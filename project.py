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


# Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard
measure_83 = getMeasureColumns('83')
# Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard 
# (monitor and modeled data)
measure_292 = getMeasureColumns('292')


# Number of person-days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard
measure_84 = getMeasureColumns('84')
# Number of person-days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard 
# (monitor and modeled data)
measure_293 = getMeasureColumns('293')


# Percent of days with PM2.5 levels over the National Ambient Air Quality Standard (NAAQS)
measure_85 = getMeasureColumns('85')
# Percent of days with PM2.5 levels over the National Ambient Air Quality Standard (monitor and modeled data)
measure_294 = getMeasureColumns('294')


# Person-days with PM2.5 over the National Ambient Air Quality Standard
measure_86 = getMeasureColumns('86')
# Number of person-days with PM2.5 over the National Ambient Air Quality Standard (monitor and modeled data)
measure_295 = getMeasureColumns('295')

# Annual average ambient concentrations of PM2.5 in micrograms per cubic meter 
# (based on seasonal averages and daily measurement)
measure_87 = getMeasureColumns('87')
# "Annual average ambient concentrations of PM 2.5 in micrograms per cubic meter based on seasonal averages 
# and daily measurement (monitor and modeled data)"
measure_296 = getMeasureColumns('296')


# TODO CHANGE VALUE TO FLOAT SO WE CAN GET MEAN AND OTHER SUCH THINGS
print("Change to Float:")
measure_84['Value'] = measure_84['Value'].astype(np.float)


print("Reading Complete:")
# print(np.argmin(measure_84["Value"].astype(np.float)))
# print(np.argmax(measure_84["Value"].astype(np.float)))


unique_a, counts_a = np.unique(measure_84['StateName'], return_counts=True)

print(unique_a)
print(counts_a)
# states = {
#     "Alabama": {
#             1999: {
#                 "max":100,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#     },
#     'Alaska':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Arizona':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Arkansas':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'California':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Colorado':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Connecticut':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Delaware':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'District of Columbia':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Florida':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Georgia':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Hawaii':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Idaho':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Illinois':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Indiana':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Iowa':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Kansas':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Kentucky':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Louisiana':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Maine':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Maryland':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Massachusetts':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Michigan':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Minnesota':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Mississippi':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Missouri':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Montana':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Nebraska':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Nevada':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'New Hampshire':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'New Jersey':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'New Mexico':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'New York':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'North Carolina':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'North Dakota':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Ohio':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Oklahoma':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Oregon':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Pennsylvania':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Rhode Island':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'South Carolina':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'South Dakota':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Tennessee':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Texas':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Utah':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Vermont':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Virginia':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Washington':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'West Virginia':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Wisconsin':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
# },
#     'Wyoming':{
#             1999: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2000: {
#                 "max":0,
#                 "min":0,
#                 "std":0,
#                 "median":0,
#                 "mode":0
#             },
#             2001: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2002: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2003: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2004: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2005: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2006: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2007: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2008: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2009: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2010: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2011: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2012: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             },
#             2013: {
#                 "max": 0,
#                 "min": 0,
#                 "std": 0,
#                 "median": 0,
#                 "mode": 0
#             }
#
#     }
#
#
}
# print(round(np.std(measure_84["Value"].astype(np.float)),2))

# print(states['Alabama'][1999]['max'])