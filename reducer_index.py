#!/usr/bin/env python
import sys

previous = None
wc = 0
count = 1
doclist = []
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    key, doc, lc = line.split('\t')
    # by key (here: word) before it is passed to the reducer
    if key == previous:
        count+=1
        doclist.append((doc,lc))
    else:
        if previous:
            print(previous + '\t' + str(count) + "\t" + str(doclist))
            doclist = []
        count=1
        previous = key
        doclist.append((doc,lc))
if previous == key:
    print(previous + '\t' + str(count) + "\t" + str(doclist))
