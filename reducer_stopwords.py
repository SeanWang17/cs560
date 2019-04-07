#!/usr/bin/env python
import sys
from os import system

previous = None
wc_list = {}
sum = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    key, value = line.split('\t',1)
    # by key (here: word) before it is passed to the reducer
    if key == previous:
        sum += int(value)
    else:
        if previous:
            wc_list[previous] = sum
        sum = int(value)
        previous = key
if previous == key:  # the last word
    wc_list[previous] = sum
sorted_wc_list = sorted(wc_list.items(),key=lambda (k,v):v)
# output stop words (count > 150)
for key,value in sorted_wc_list:
	if value > 1500:
		print key + '\t' + str(value)

