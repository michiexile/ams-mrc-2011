#!/usr/bin/python

import sys, os, re, time

ssidRE = "\s+([^ ]{2,32})\s+([0-9a-f:]*)\s(-?\d+)"

airport = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s"

def collect():
    t = time.time()
    f = os.popen(airport)
    for l in f:
        m = re.match(ssidRE, l)
        if m == None:
            continue
        print t, m.group(2), m.group(3)
    f.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        for i in range(n):
            collect()
        exit(0)
    while True:
        collect()
