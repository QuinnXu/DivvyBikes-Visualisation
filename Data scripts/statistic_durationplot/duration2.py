import csv

category=[]
for i in range(0,60,2):
    s = '{}-{}'.format(i,i+2)
    category.append(s)
print(category)
categories =  ['0-2', '2-4', '4-6', '6-8', '8-10', '10-12', '12-14', '14-16', '16-18', '18-20', '20-22', '22-24', '24-26', '26-28', '28-30', '30-32', '32-34', '34-36', '36-38', '38-40', '40-42', '42-44', '44-46', '46-48', '48-50', '50-52', '52-54', '54-56', '56-58', '58-60']

# for i in range(0,60,6):
#    s = '1h {}-{}min'.format(i,i+6)
#    category.append(s)
# category = category + ['2h 0-30min','2h 0-60min','3-6h','6-12h','12h +']
# category = ['0-3min', '3-6min', '6-9min', '9-12min', '12-15min', '15-18min', '18-21min', '21-24min', '24-27min', '27-30min', '30-33min', '33-36min', '36-39min', '39-42min', '42-45min', '45-48min', '48-51min', '51-54min', '54-57min', '57-60min', '1h 0-6min', '1h 6-12min', '1h 12-18min', '1h 18-24min', '1h 24-30min', '1h 30-36min', '1h 36-42min', '1h 42-48min', '1h 48-54min', '1h 54-60min', '2h 0-30min', '2h 0-60min', '3-6h', '6-12h', '12h +']


# ['0-3min', '3-6min', '6-9min',
# '9-12min', '12-15min', '15-18min',
# '18-21min', '21-24min', '24-27min',
# '27-30min', '30-33min', '33-36min',
#  '36-39min', '39-42min', '42-45min',
# '45-48min', '48-51min', '51-54min',
# '54-57min', '57-60min',
# 3min 20

# '1h 0-6min', '1h 6-12min', '1h 12-18min', '1h 18-24min',
#  '1h 24-30min', '1h 30-36min', '1h 36-42min',
# '1h 42-48min', '1h 48-54min', '1h 54-60min',
# 6min 10

# '2h 0-30min', '2h 0-60min',
# 30min 2

# '3-6h', '6-12h', '12h +']  3



# calculate proportion

sum_sub= 844047
sum_cus= 275764
def prop_sub(l):
    for i in range(len(l)):
        l[i] = round((l[i]*100)/-sum_sub,2) # -
    print(l)

def prop_cus(l):
    for i in range(len(l)):
        l[i] = round((l[i]*100)/sum_cus,2) # +
    print(l)

# group into time sequence
def group(x):
    list_time = []
    for i in range(30):
        list_time.append(0)

    with open(x) as f:
        f_csv = csv.reader(f)
        header =next(f_csv)
        for row in f_csv:
            duration = int(row[1])
            freqency = int(row[2])
            if  duration < 3600: # 1hour into 30 groups
                list_time[int(duration/(2 * 60))] += freqency # sum (t/2mins) by sequence
    return list_time




prop_cus(group('/Users/xuzheran/Desktop/Divvy-viz/statistic_durationplot/customerduration.csv'))
prop_sub(group('/Users/xuzheran/Desktop/Divvy-viz/statistic_durationplot/subscriberduration.csv'))