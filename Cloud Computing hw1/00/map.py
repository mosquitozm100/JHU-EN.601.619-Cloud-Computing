#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    
    tokens = line.split()

    for token in tokens:
        print("{token}\t{count}".format(token=token, count=1))