import csv


list_age =[]
cus=275767
sub=844047
unknow = 102
Female=217074
Male=626871

total =cus+sub


for i in range(11):
    list_age.append(0)

def prop(f):
    prop=round(f*100/total,2)
    return prop

def group(x):
    with open(x) as f:
        f_csv = csv.reader(f)
        header =next(f_csv)
        for row in f_csv:
            year = int(row[1])
            freqency = int(row[2])
            if year >= 1997:
                list_age[0] += freqency
            elif 1997 > year >= 1987:
                list_age[1] += freqency
            elif 1987 > year >= 1977:
                list_age[2] += freqency
            elif 1977 > year >= 1967:
                list_age[3] += freqency
            elif 1967 > year >= 1957:
                list_age[4] += freqency
            elif 1957 > year >= 1947:
                list_age[5] += freqency
            elif 1947 > year >= 1937:
                list_age[6] += freqency
            elif 1937 > year >= 1927:
                list_age[7] += freqency
            elif 1927 > year >= 1917:
                list_age[8] += freqency
            elif 1917 > year >= 1907:
                list_age[9] += freqency
            elif 1907 > year:
                list_age[10] += freqency

    for i in range(len(list_age)):
        list_age[i] = prop(list_age[i])

    print(list_age)

print('Sub')
print(prop(sub))

print('Cus')
print(prop(cus))

print('unknow:')
print(prop(unknow))

print('Female')
print(prop(Female))

print('Male')
print(prop(Male))

print('female:')
group('/Users/xuzheran/Desktop/Divvy-viz/statistic_userinfoplot/female.csv')
print('male:')
group('/Users/xuzheran/Desktop/Divvy-viz/statistic_userinfoplot/male.csv')