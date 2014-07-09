import numpy as np
import csv as csv
import pandas as pd

readdata = csv.reader(open('pop_change.csv', 'r'))
data = []
for row in readdata:
    data.append(row)
Header = data[0]
data.pop(0)

pop2010 = []
for i in range(len(data)):
    pop2010.append(int(data[i][2]))
print "average in 2010: %d " % (np.mean(pop2010))

