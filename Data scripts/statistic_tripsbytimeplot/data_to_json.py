import csv
import json

l=[]
with open('/Users/xuzheran/Desktop/Divvy-viz/statistic_tripsbytimeplot/tripsbyhour.csv') as f:
    f_csv = csv.reader(f)
    header =next(f_csv)
    for row in f_csv:
        list=[int(float(row[1])*1000),int(row[2])]
        l.append(list)

ljson = json.dumps(l,sort_keys=True,indent=4)
fileObject = open('tripsbytime.json', 'w')
fileObject.write(ljson)
fileObject.close()