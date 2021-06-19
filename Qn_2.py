#Program to read a CSV (CSV with n number of columns) and store it in DICT of list.

import csv
file=csv.DictReader(open("D:\\data.csv"))
for j in file:
    print(j)
