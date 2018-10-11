import csv



categories = ['0-5min', '5-10min', '10-15min', '15-20min',
    '20-25min', '25-30min', '30-35min', '35-40min', '40-45 min',
    '45-50min', '50-55min', '55mins-1h', #12
              '1h-1h10mins', '1h10mins-1h20min','1h20min-1h30min', #3
              '1h30min-1h45min', '1h45min-2h', #2
              '2h-2h30min', '2h30min-3h', #2
    '3h-6h', '6h-12h','12h+']  #3

def prop(l):
    sum = 0
    for i in l:
        sum += i
    for i in range(len(l)):
        l[i] = round((-l[i]*100)/sum,2)


def group(x):

    list_time = []
    for i in range(22):
        list_time.append(0)

    with open(x) as f:
        f_csv = csv.reader(f)
        header =next(f_csv)
        for row in f_csv:
            duration = int(row[1])
            freqency = int(row[2])
            if  duration < 3600: # 1h 12
                list_time[int(duration/(5 * 60))] += freqency

            elif 3600 <= duration < 5400: # 1h-1.5h 3
                list_time[12+int((duration-3600) / (10 * 60))] += freqency

            elif 5400 <= duration < 7200: # 1.5h-2h 2
                list_time[15+int((duration-5400) / (15 * 60))] += freqency

            elif 7200 <= duration < 10800: # 2h-3h 2
                list_time[17+int((duration-7200) / (30 * 60))] += freqency

            elif 10800 <= duration < 21600: # 3h-6h 1
                list_time[-3] += freqency

            elif 21600 <= duration < 53200: # 6h-12h 1
                list_time[-2] += freqency

            elif 53200 <= duration: # 12h- 1
                list_time[-1] += freqency

    prop(list_time)
    print(x)
    print(list_time)


group('/Users/xuzheran/Desktop/Divvy-viz/statistic_durationplot/customerduration.csv')
group('/Users/xuzheran/Desktop/Divvy-viz/statistic_durationplot/subscriberduration.csv')