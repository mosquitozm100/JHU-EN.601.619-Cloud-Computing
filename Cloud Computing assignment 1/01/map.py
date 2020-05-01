#!/usr/bin/env python
import sys

numbers = set(['2166849356', '4049345110','5893715037', '9457920329'])
for line in sys.stdin:
    line = line.strip()
    
    tokens = line.split(';')
    if tokens[-2] in numbers:
        print("{token}\t{count}".format(token=tokens[1], count=1))