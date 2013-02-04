from __future__ import division
import json
import csv
from random import randint
from os import system
import time
import re

f = open('data.csv', 'rb')

fieldnames = ['category', 'question', 'option1', 'option2', 'option3', 'option4', 'answer', 'hint']
reader = csv.DictReader(f, fieldnames=fieldnames)

rows = list(reader)
total_rows = len(rows)

stats = {"correct": 0, "incorrect": 0, "percent": 0}

for i in range(total_rows):
    r = randint(0, total_rows-1)
    row = rows[r]

    print "----------------------------------------"
    print row['question'], "\n"
    print '  a: %s' % row['option1']
    print '  b: %s' % row['option2']
    print '  c: %s' % row['option3']
    print '  d: %s' % row['option4']

    choices = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
    answer = raw_input("\nYour Answer: ")
    
    if answer in choices:
        answer = str(choices[answer])
    else:
        answer = 'wrong'
 
    if answer == row['answer']:
        stats['correct'] += 1
        stats['percent'] = (stats['correct'] / stats['incorrect']) * 100
        print "\n**** CORRECT (%s/%s - %s%%) ****" % (stats['correct'], stats['incorrect'], stats['percent'])
                
    else:
        stats['incorrect'] += 1
        print "\n**** INCORRECT (%s/%s - %s%%) ****" % (stats['correct'], stats['incorrect'], stats['percent'])
        print "\n", row['hint'] 

    raw_input()

f.close()
