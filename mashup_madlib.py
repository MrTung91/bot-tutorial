#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mad Lib Maker!

# This script will generate mad-libs based off of a William Carlos
# Williams poem, 'The Red Wheelbarrow.' Each poem will then be
# tweeted by your bot account. 

# Housekeeping: do not edit
import json, io, tweepy, time, urllib2
from random import randint
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# Housekeeping: opening JSON files
# Find more item lists at https://github.com/dariusk/corpora/tree/master/data
# Click "Raw" button, copy URL
objectfile = urllib2.urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/objects/objects.json')
objectlist = objectfile.read()

foodsfile = urllib2.urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/menuItems.json')
foodslist = foodsfile.read()

# Create Python-readable lists of items in JSON files
objs = json.loads(objectlist)['objects']
foods = json.loads(foodslist)['menuItems']


# Repeatable poem-generator
poemlist = []
counter = 0

while counter < 2: # Change 2 to however many poems you want to produce
    
    # Pick random numbers
    objnum = randint(0, len(objs) - 1)
    foodnum = randint(0, len(foods) - 1)

    # Choose random items from each list using random numbers
    first = objs[objnum] # Syntax: list[number]
    second = foods[foodnum].lower()
    third = objs[objnum + 1] + 's'

    # Fill in the blanks of the poem
    poem = 'so much depends\nupon\n\na\n%s\n\nglazed with\n%s\n\nbeside the\n%s\n\n' \
           % (first, second, third)

    print poem
    poemlist.append(poem) #add to long list of poems
    counter = counter + 1


# Line up tweets for bot

for line in poemlist: 
    api.update_status(line)
    #print line
    time.sleep(15) # Sleep for 15 seconds


print '[All done!]'

