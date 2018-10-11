import csv
import json
import os
from route_osrm import calRoutes

l = {"type": "FeatureCollection","features": []}

stations_location={}

with open('/Users/xuzheran/Desktop/Divvy-viz/Divvy_Stations_2017_Q1Q2.csv') as f:
    f_csv = csv.reader(f)
    header =next(f_csv)
    for row in f_csv:
        stations_location[int(row[0])] = [float(row[4]),float(row[3])]
        l["features"].append({"type": "Feature", "properties": {}, "geometry": {"type": "Point", "coordinates": [float(row[4]),float(row[3])]}})


list=[]

#,'L_0_6.csv'，'L_18_24.csv','L_12_18.csv','L_18_24.csv'，'M_0_6.csv','M_6_12.csv','M_12_18.csv','M_18_24.csv','S_0_6.csv','S_6_12.csv','S_12_18.csv','S_18_24.csv']


r={
  "features": [],
  "type": "FeatureCollection"
}

for i in list:
    with open('/Users/xuzheran/Desktop/Divvy-viz/Q2_Route/'+i) as f:
        f_csv = csv.reader(f)
        header =next(f_csv)
        for row in f_csv:
            s=stations_location[int(row[6])]
            e=stations_location[int(row[8])]
            start=str(s[0])+','+str(s[1])
            stop = str(e[0]) + ',' + str(e[1])
            routes = calRoutes(start, stop)
            r["features"].append({"properties": {"prop0": "value0"},"id": "{feature_id}","type": "Feature","geometry":routes})
            print(routes)
            routesline = json.dumps(r, sort_keys=True, indent=4)
            fileObject = open(i+'e.json', 'w')
            fileObject.write(routesline)
            fileObject.close()

