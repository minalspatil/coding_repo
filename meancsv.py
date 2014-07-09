import csv
import numpy as np
reader = csv.DictReader(open('salaries.csv', 'r'))
rows = sorted(reader)
a = {}
for i in xrange(len(rows)):
    if rows[i].values()[2] == 'Lawyers':
        a[rows[i].values()[1]]=rows[i].values()[0]
t = [i for i in sorted(a, key=lambda key:a[key], reverse=True)]

p=a.values()

p.sort()

p.reverse()

data1 = []
for row in p:
    data1.append(row)
law = []
for i in range(len(data1)):
    law.append(int(data1[i][2]))
print data1
a = np.asarray(data1)
a = map(int, a)
print a
print "median: %d  " % (np.median(a))

#print "median %d : " % (np.median(law))
#for i in xrange(len(a)):
#    print t[i]+","+p[i]

