#!/usr/bin/env python
import sys

numbers = set(['2166849356', '4049345110','5893715037', '9457920329'])
violate_companies = set('')
calculated_phones = set('')
lines = []
for line in sys.stdin:
    line = line.strip()
    lines.append(line)
    
    tokens = line.split(';')
    if tokens[-2] in numbers:
        violate_companies.add(tokens[1])
        #print("{token}\t{count}".format(token=tokens[1], count=1))


for line in lines:
    line = line.strip()
    
    tokens = line.split(';')
    if tokens[1] in violate_companies and tokens[2] not in calculated_phones:
        calculated_phones.add(tokens[2])
        print("{token}\t{count}".format(token=tokens[1], count=1))