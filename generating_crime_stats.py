import json
from shapely.geometry import shape, Point
import pandas as pd

with open('data/reading_test.json') as f:
    js = json.load(f)

my_dict = {}

for feature in js['features']:
    my_dict[feature['properties']['SQUARE']] = [0]

crimedata = pd.read_csv('data/2018-06/2018-06-thames-valley-street.csv')

for index, row in crimedata.iterrows():
    point = Point(row['Longitude'], row['Latitude'])

    for feature in js['features']:
        polygon = shape(feature['geometry'])
        #if point in shape
        if polygon.contains(point):
            #counting the number of crimes
            my_dict[feature['properties']['SQUARE']][0] += 1

crime_stats = pd.DataFrame.from_dict(my_dict, orient='index')
print(crime_stats)
crime_stats.to_json('crime_stats.json')


