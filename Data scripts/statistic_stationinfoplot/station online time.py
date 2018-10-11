import csv
import json

l=[]
l_=[]

def city(x):
    if x == "Chicago":
        return 0
    elif x == "Oak Park":
        return 1
    elif x == "Evanston":
        return 2

with open('/Users/xuzheran/Desktop/Divvy-viz/statistic_stationinfoplot/onlinetime.csv') as f:
    f_csv = csv.reader(f)
    header =next(f_csv)
    for row in f_csv:
        dict = {'x': int(row[-2])*1000, 'y': int(row[-1]), 'z': int(row[-3]), 'name': row[2], 'city': row[3]}
        l.append(dict)
        
        list = [int(row[-2])*1000,city(row[3]),int(row[-1]),int(row[-3])]
        l_.append(list)

fileObject = open('parallel.json', 'w')
fileObject.write(json.dumps(l_))
fileObject.close()
