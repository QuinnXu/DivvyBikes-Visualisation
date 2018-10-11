import csv

category=[]
for i in range(30,120,5):
    i = i/10
    s = '{}h-{}h'.format(i,i+0.5)
    category.append(s)
print(category)
print(len(category))

sum_sub= 844047
sum_cus= 275764

def prop_sub(l):
    for i in range(len(l)):
        l[i] = round((l[i]*100)/-sum_sub,2) ### + - ###
    print(l)

def prop_cus(l):
    for i in range(len(l)):
        l[i] = round((l[i]*100)/sum_cus,2)
    print(l)

def group(x):

    list_time = []
    for i in range(19):
        list_time.append(0)

    with open(x) as f:
        f_csv = csv.reader(f)
        header =next(f_csv)
        for row in f_csv:
            duration = int(row[1])
            freqency = int(row[2])
            if  duration >= 10800: # from 1h to 3h into 30 groups
                if duration < 43200:
                    list_time[int((duration-10800)/(30 * 60))] += freqency
                else:
                    list_time[-1] += freqency
    return list_time


prop_cus(group('/Users/xuzheran/Desktop/Divvy-viz/statistic_durationplot/customerduration.csv'))
prop_sub(group('/Users/xuzheran/Desktop/Divvy-viz/statistic_durationplot/subscriberduration.csv'))
