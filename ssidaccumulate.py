#!/usr/bin/python

import sys, collections, csv

def accumulate():
    readings = collections.defaultdict(dict)
    basis = set()
    matrix = []
    for l in sys.stdin:
        ls = l.split()
        readings[ls[0]][ls[1]] = ls[2]
        basis.add(ls[1])
    
    for t in readings:
        row = []
        for b in basis:
            if b not in readings[t]:
                v = 0
            else:
                v = readings[t][b]
            row.append(v)
        matrix.append(row)

    csvw = csv.writer(sys.stdout)
    csvw.writerows(matrix)

if __name__ == '__main__':
    accumulate()

