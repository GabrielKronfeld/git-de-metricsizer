'''
Automatic git commits
aka: the git commit de-analyticsizer (name not decided)
we have a cron job that calls the file to be run, and does this 4 times a day.

we then randomly (call it 3/4 of the time) execute the following commands. otherwise, we do nothing.


IF we don't have a folder system, we make one (called the nonsense machine)
we we don't have a file in the folder, we make one.
we randomly choose to: make a new folder, make a new file, or edit a new file
we take a file or folder system. 
we ask chatgpt to make a project given the code in the file(pass the file)

folder called the nonsense machine. 
we make changes to the nonsense machine based on probabilities (either we make a new file or we randomly add to an extant one)
we then run 
git add * , 
git commit -m "adding to the nonsense machine"
git push origin master (pass git login params?)
can we run the git commands in a py script?
use import subprocess


TEMPORARY (HAH!)
 we will instead just pull a random word from a dictionary and append it to the file we choose, if we choose to make a file. 

 things to consider: what permissions will the executing file have? will it have write permissions? I hope so!
'''

#!usr/env/bin python

import random 
import nltk as nl

#we add some variance to make some days have fewer, and some have more commits, to give a more human contribution page. this can be removed at your preference
if random.random <0.25:
    print('we do dont do stuff this time')
    exit()

print('we are doing stuff this time!')


