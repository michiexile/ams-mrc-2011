#!/usr/bin/python -u

import sys, collections, csv

def accumulate():
    min_strength = 0

    readings = collections.defaultdict(dict)
    basis = set()
    matrix = []
    for l in sys.stdin:
        ls = l.split()
        if len(ls) == 3:
            [t,b,v] = ls
            readings[t][b] = v
            min_strength = min(min_strength, int(v))
            basis.add(b)

    header = ['timestamp'] + [b for b in basis]

    timestamps = readings.keys()
    timestamps.sort(key=lambda x: float(x))

    for t in timestamps:
        row = [t]
        for b in basis:
            if b not in readings[t]:
                row.append(min_strength-1) # too silent
            else:
                row.append(readings[t][b])
        matrix.append(row)

    csvw = csv.writer(sys.stdout,lineterminator='\n')
    csvw.writerow(header)
    csvw.writerows(matrix)

if __name__ == '__main__':
    accumulate()
