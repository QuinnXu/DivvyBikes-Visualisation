import csv
import json

from route_osrm import calRoutes

l = {"type": "FeatureCollection","features": []}

stations_location={}
with open('/Users/xuzheran/Desktop/Divvy-viz/Divvy_Stations_2017_Q1Q2.csv') as f:
    f_csv = csv.reader(f)
    header =next(f_csv)
    for row in f_csv:
        stations_location[int(row[0])] = [float(row[4]),float(row[3])]
        l["features"].append({"type": "Feature", "properties": {}, "geometry": {"type": "Point", "coordinates": [float(row[4]),float(row[3])]}})


locationjson = json.dumps(l,sort_keys=True,indent=4)
fileObject = open('location.json', 'w')
fileObject.write(locationjson)
fileObject.close()

r={
  "features": [],
  "type": "FeatureCollection"
}

with open('Divvy_Trips_2017_Q2.csv') as f:
    f_csv = csv.reader(f)
    header =next(f_csv)
    for row in f_csv:
        s=stations_location[int(row[5])]
        e=stations_location[int(row[7])]
        start=str(s[0])+','+str(s[1])
        stop = str(e[0]) + ',' + str(e[1])
        routes = calRoutes(start, stop)
        r["features"].append({"properties": {"prop0": "value0"},"id": "{feature_id}","type": "Feature","geometry":routes})
        print(routes)
        routesline = json.dumps(r, sort_keys=True, indent=4)
        fileObject = open('routesline.json', 'w')
        fileObject.write(routesline)
        fileObject.close()

