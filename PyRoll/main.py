import os
import csv
import collections as ct

pyroll_csv = os.path.join("pyroll.csv")

with open(pyroll_csv, newline="") as csvfile:
    votes=ct.Counter()
    header=next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        candidate=row[-1]
        votes[candidate] += 1
    
    print(votes)
    print(votes.most_common(1))