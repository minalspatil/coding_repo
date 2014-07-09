import numpy as np
import csv as csv
import pandas as pd

readdata = csv.reader(open('salaries.csv', 'r'))
data = []
for row in readdata:
    data.append(row)
Header = data[0]
data.pop(0)
salary = []
for i in range(len(data)):
    salary.append(int(data[i][2]))
print "median is : %d " % (np.median(salary))
print "standard dev is : %d " % (np.std(salary))

