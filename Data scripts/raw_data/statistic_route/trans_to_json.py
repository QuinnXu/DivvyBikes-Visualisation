import csv
import json



stationsinfo=[]
with open('/Users/xuzheran/Desktop/Divvy-viz/station_totalinfo.csv') as f:
    f_csv = csv.reader(f)
    header =next(f_csv)
    for row in f_csv:
        dict={
                "type": "Feature",
                "properties": {
                    "name": row[1],
                    "city": row[2],
                    "online time": row[6],
                    "capacity": int(row[5]),
                    "trips": int(row[7])
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        float(row[4]),
                        float(row[3])
                    ]
                }
        }
   #     dict={
    #            "name": row[1],
    #            "city": row[2],
   #             "lat": float(row[3]),
    #            "lon": float(row[4]),
    #            "online time": row[6],
    #            "capacity": int(row[5]),
    #            "trips": int(row[7])

        stationsinfo.append(dict)

stationsinfojson = json.dumps(stationsinfo,sort_keys=True,indent=4)
fileObject = open('station-total-info.geo.json', 'w')
fileObject.write(stationsinfojson)
fileObject.close()
