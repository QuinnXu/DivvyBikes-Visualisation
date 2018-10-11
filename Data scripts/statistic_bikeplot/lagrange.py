import csv
from scipy.interpolate import lagrange
import numpy as np

x_data=[]
y_data=[]
data=[]
with open('/Users/xuzheran/Desktop/Divvy-viz/statistic_bikeplot/bikeusedfreqency.csv') as f:
    f_csv = csv.reader(f)
    header =next(f_csv)
    for row in f_csv:
        x_data.append(int(row[1]))
        y_data.append(int(row[2]))
        data.append([int(row[1]),int(row[2])])

print(data)


### xm = np.mean(x_data)
#xscale = np.std(x_data)
#ym = np.mean(y_data)
#yscale = np.std(y_data)
#x = (x_data - xm) / xscale
#y = (y_data - ym) / yscale
#poly = lagrange(x, y)
#xx = list(range(0,399,10))
#yy = poly((xx - xm)/xscale)*yscale + ym

