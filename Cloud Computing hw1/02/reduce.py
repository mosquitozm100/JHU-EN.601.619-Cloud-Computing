#!/usr/bin/env python
import sys
def emit(token, count):
    print('{token}\t{count}'.format(token=token, count=count))

previous = None
token = ''
total = 0
for line in sys.stdin:
    line = line.strip()

    token, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if previous == token:
        total = total + count
    else:
        if previous:
            emit(previous, total)
        
        previous = token
        total = count

emit(token, total)
