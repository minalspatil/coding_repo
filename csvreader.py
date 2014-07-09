import csv
reader = csv.DictReader(open('salaries.csv', 'rb'))
#rows = sorted(Reader)
for row in reader:
    print row

reader = csv.reader(open('salaries.csv', 'rb'))
for row1 in reader:
    print row1
