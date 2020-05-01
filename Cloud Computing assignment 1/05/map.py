#!/usr/bin/env python
import sys

numbers = set(['2166849356', '4049345110','5893715037', '9457920329'])
violate_companies = set('')
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
    if tokens[1] in violate_companies:
        time_in_24 =tokens[0].strip().split(' ')[-1].split(':')[0]
        if int(time_in_24) == 0:
            time = '12 p.m.'
        elif int(time_in_24) <= 12:
            time = str(int(time_in_24)) + ' a.m.'
        else:
            time = str(int(time_in_24) - 12) + ' p.m.'

        print("{token}\t{count}".format(token=time, count=1))