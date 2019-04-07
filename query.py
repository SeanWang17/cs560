#!/usr/bin/env python

path = r'index/part-00000'

user_input = raw_input("Please input the words you want to query, seperate by space: ")

words = user_input.split(" ")
flag = 0 # check if the word can be found
with open(path, 'r') as f:
    for line in f:
        word, count, location = line.strip().split('\t')
        if word in words:
            print("The number of occurence of %s: %s" % (word, count))
            print("The location of occurence of %s: %s" % (word, location))
            flag = 1
if flag == 0:
    print("Sorry, the words you are querying cannot be found!")
