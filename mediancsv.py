from StringIO import StringIO
import sqlite3
import csv
import operator
data = open('salaries.csv', 'r').read()
string = join(data)
f = StringIO(string)
reader = csv.reader(f)
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''create table data(City text, Job text, Salary real)''')
conn.commit()
count = 0
for e in reader:
    if count == 0:
    print ""
    else:
        e[0] = str(e[0])
        e[1] = str(e[1])
        e[2] = float(e[2])
        c.execute("""insert into data values(?,?,?)""",e)
        count = count+1
con.commit()
label = []
count = []
count = 0
c.execute(""select count(Salary),Job from data group by Job"")
for row in c:
    for i in row:
        if count == 0:
            counts.append(i)
            count = count + 1
        else:
            count = 0
    labels.append(i)
c.execute("" select Salary, Job from data order by Job "")
count = 1
count1 = 1
temp = 0
pri = 0
lis = []
for row in c:
    lis.append(row)
for cons in counts:
    if cons%2==0:
        pri = cons/2
    else:
        pri = (cons+1)/2
    if count1==1:
        for li in lis:
            if count == pri:
                print "Median is", li
            count = count + 1
            count = 0
            temp = pri+cons
    else:
        for li in lis:
            if count == temp:
                print 'Median is',li
                count = count + 1
                count = 0
                temp = temp + pri
        count1 = count1 + 1


