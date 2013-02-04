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

questions_answered = 1 
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
    
    answer = str(choices[answer]) if answer in choices else 'wrong'

    stats['percent'] = (stats['correct'] / questions_answered) * 100
 
    if answer == row['answer']:
        stats['correct'] += 1
        status = "CORRECT"
    else:
        stats['incorrect'] += 1
        status = "INCORRECT"

    stats['percent'] = "{0:.0f}%".format( (stats['correct'] / questions_answered) * 100 )
    print "\n**** %s (%s/%s - %s) ****" % (status, stats['correct'], questions_answered, stats['percent'])

    if answer == row['answer']: print "\n", row['hint'] 

    questions_answered += 1
    raw_input()

f.close()
