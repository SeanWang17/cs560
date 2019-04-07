#!/usr/bin/env python
import os
import re
import sys

#works_path = r'works/'

# tokenize function
def tokenize(text):
    min_length = 3   # typically, words with length smaller than 3 is not meaningful
    words = map(lambda word: word.lower(), text.strip().split(' '))  # case insensitive
    p = re.compile('^[a-zA-Z]+$')  # remove the mess up
    filtered_words = list(filter(lambda token: p.match(token) and len(token)>=min_length, words))
    return filtered_words

# get the word + count
for line in sys.stdin:
    words = tokenize(line.decode('utf-8'))
    if words:
        for word in words:
            print('%s\t%s' % (word,1))
