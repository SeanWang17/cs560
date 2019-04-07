#!/usr/bin/env python
import os
import re
import sys


# tokenize function
def tokenize(text):
    min_length = 3   # typically, words with length smaller than 3 is not meaningful
    words = map(lambda word: word.lower(), text.strip().split(' '))  # case insensitive
    p = re.compile('^[a-zA-Z]+$')  # remove the mess up
    filtered_words  = list(filter(lambda token: p.match(token) and len(token)>=min_length, words))
    return filtered_words

# get the nonstopwords
word_list =[]
with open("stopwords.txt", 'r') as f:
    for line in f:
        word, count = line.strip().split('\t')
	word_list.append(word)

# get the word+line
fname = None

for line in sys.stdin:
	#get the mapper input filename
    filename = os.getenv('mapreduce_map_input_file')  
    if filename != fname:
        doc = filename.split('/')[-1][:-4]
        lc = 0
        fname = filename
    lc += 1
    words = tokenize(line.decode('utf-8'))
    if words:
        for word in words:
            if word not in word_list:
                print('%s\t%s\t%s' % (word,doc,lc))
