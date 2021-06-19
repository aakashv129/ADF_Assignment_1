import csv
file=csv.DictReader(open("D:\\data.csv"))
for j in file:
    print(j)