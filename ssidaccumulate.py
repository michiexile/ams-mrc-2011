#!/usr/bin/python -u

import sys, collections, csv

def accumulate():
    readings = collections.defaultdict(dict)
    basis = set()
    matrix = []
    for l in sys.stdin:
        ls = l.split()
        if len(ls) == 3:
            [t,b,v] = ls
            readings[t][b] = v
            basis.add(b)
    
    header = ['timestamp'] + [b for b in basis]
    
    for t in readings:
        row = [t]
        for b in basis:
            if b not in readings[t]:
                row.append(-95) # too silent
            else:
                row.append(readings[t][b])
        matrix.append(row)
        
    csvw = csv.writer(sys.stdout,lineterminator='\n')
    csvw.writerow(header)
    csvw.writerows(matrix)

if __name__ == '__main__':
    accumulate()
