#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# IMPORTANT:
# This script must be run with root rights.
#
# sudo -s
# python ssidcollect_linux.py
#
# by Daniel Müllner, muellner@math.stanford.edu
from subprocess import Popen, PIPE, STDOUT
from time import time
from re import search, finditer, MULTILINE
import sys

while True:
    process = Popen(['iwlist','scan'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    timestamp = time()
    match = finditer('Address: (..:..:..:..:..:..).*\n.*\n.*\n.*Signal level=([-0-9]*) dBm', stdout, MULTILINE)
    for f in match:
        print '{0} {1} {2}'.format(timestamp, f.group(1), f.group(2))
    sys.stdout.flush()
