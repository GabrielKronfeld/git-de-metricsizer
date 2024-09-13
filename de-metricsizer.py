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

 we can write random words
 we can build standard forms of programming blocks, such as
    variable creation,
    loops
    changing variables
    outputting data


Steps:  move to nonsense machine
        make changes
        commit changes to git
        exit
'''

#!usr/env/bin python

import random
import nltk as nl
import subprocess
import os
from nltk.corpus import words

nl.download('words')

#return a  name built from 1-3 random words
#todo: verify edge case of having an identical name in dir. very unlikely but rigor is good practice.
def buildName():
    builtName=getRandomWord()
    i=2
    while i >0:
        if random.random()>0.5:
            buildName+=getRandomWord()

    return builtName

#need to decode the directories and files that exist first. might want to do this in a separate method

def whatinDir(dirpath):

    test=subprocess.run(['ls','-l'],cwd=dirpath,capture_output=True)
    og=test.stdout.decode('ascii').split('\n')
    # print('test:',test)
    og.pop(0)#removes the count of files in dir
    for i in og:
        print(i)
    #verify we're in the right location
    subprocess.run('pwd')

def movetoRepo(repoPath):
    os.chdir(repoPath)
    test=subprocess.run(['ls','-l'],cwd='/',capture_output=True)
    og=test.stdout.decode('ascii')
    print('test:',test)
    print(type(og))
    #verify we're in the right location
    subprocess.run('pwd')

def getRandomWord():
    return DICTIONARY[round(DICTLEN*random.random())]#returns a random word

def makeFolder(folderName):
    try: subprocess.run(['mkdir', folderName])
    except TypeError:
        print("folderName var is not a string! no folder was made")

def makeFile(name):
    subprocess.run(['touch', str(name)])
    
    pass
def changeFile(file):
    #we can cat the file, push it to a string, manip the string then push the string back to the file
    pass

def writeData():
    pass

def writeLoop():
    return("")    

#we add some variance to make some days have fewer, and some have more commits, to give a more human contribution page. this can be removed at your preference
if (random.random() < 0.25):
    print('we do dont do stuff this time')
    exit()
DICTIONARY = words.words()
print('we are doing stuff this time!')
DICTLEN = len(DICTIONARY)
repoPath = '/Users/gabrielkronfeld/programming/python/The Nonsense Machine'
print(getRandomWord())


makeFile(5)
whatinDir('/')