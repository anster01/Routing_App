import json
from shapely.geometry import shape, Point


def FindCrimeRating(routes, node_pos, crime_statistics):
    with open('data/reading.json') as f:
        js = json.load(f)

    crime_rating = [0 for i in range(len(routes))]

    for route in range(len(routes)):
        for node in routes[route]:
            prev_polygon = ''
            point = Point(float(node_pos[node][0]), float(node_pos[node][1]))
            for feature in js['features']:
                polygon = shape(feature['geometry'])
                #if node is in shape
                if polygon.contains(point) and polygon != prev_polygon:
                    prev_polygon = polygon
                    #update the crime rating
                    if crime_statistics['0'][feature['properties']['SQUARE']] >= 11:
                        crime_rating[route] += 5
                    elif crime_statistics['0'][feature['properties']['SQUARE']] <= 10 and crime_statistics['0'][feature['properties']['SQUARE']] >= 9:
                        crime_rating[route] += 4
                    elif crime_statistics['0'][feature['properties']['SQUARE']] <= 8 and crime_statistics['0'][feature['properties']['SQUARE']] >= 7:
                        crime_rating[route] += 3
                    elif crime_statistics['0'][feature['properties']['SQUARE']] <= 6 and crime_statistics['0'][feature['properties']['SQUARE']] >= 4:
                        crime_rating[route] += 2
                    elif crime_statistics['0'][feature['properties']['SQUARE']] <= 3 and crime_statistics['0'][feature['properties']['SQUARE']] >= 2:
                        crime_rating[route] += 1
                    break
                elif polygon.contains(point) and polygon == prev_polygon:
                    break

    return crime_rating
