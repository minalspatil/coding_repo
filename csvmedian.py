import csv
import numpy as np
reader = csv.DictReader(open('salaries.csv', 'rb'))
rows = sorted(reader)
a = {}
for i in xrange(len(rows)):
    if rows[i].values()[2] == 'Plumbers':
        a[rows[i].values()[1]]=rows[i].values()[0]
t = [i for i in sorted(a, key=lambda key:a[key], reverse=True)]
p = a.values()
p.sort()
p.reverse()
for i in xrange(len(a)):
    print t[i]+","+p[i]
print 'median is %d' % (np.median(p))

