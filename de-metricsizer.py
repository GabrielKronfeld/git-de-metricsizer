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
import RepoModifier

#all actual modification and navigation functionality will be kept in a separate class.
#we add some variance to make some days have fewer, and some have more commits, to give a more human contribution page. this can be removed at your preference
if (random.random() < 0.0):
    print('we do dont do stuff this time')
    exit()

repoPath = '/Users/gabrielkronfeld/programming/python/The Nonsense Machine'
print('we are doing stuff this time!')
modifier = RepoModifier.RandomWordModifier(repoPath,"no data")

#traverse repo, see what files and folders exist. 
    #make list of files and folders?
dirs,files=modifier.whatInRepo(repoPath)
#dirs.append(repoPath)

print(dirs,files)
if (modifier.containsDupes(files) or modifier.containsDupes(dirs)):
    print("duplicate exists! might be a copied file somewhere")


#get random name (random string)
#get random directory
name=modifier.buildName()
path=dirs[random.randint(0,len(dirs)-1)]
randomText=int(random.random()*10)
print(name,path)

##we can definitely clean up the logic. it's ugly.


# take a 1/3n(?) chance to make a new dir, where n is #dirs.
if random.random()<(1/(3*len(dirs))):
    #make the new folder
    modifier.makeFolder(path,name)
    path=path+'/'+str(name)
    fileName=modifier.buildName()+'.nonsense'
    #make a new file in the directory, and then write to it.
    print('making a new file named ',fileName, 'in new dir: ',path)
    modifier.alterSpecificFile(path,fileName,randomText)

#we can randomly select a dir to append a new dir into
# ELSE IF, take a 1/n chance to make a new file in a given dir,
#we can randomly select a dir to add a new file into
elif (random.random()<(1/(len(dirs)))):

    print('making a new file named ',name, 'in extant dir: ',path)
    modifier.alterSpecificFile(path+'/'+name+'.nonsense',randomText)
    #if the file already exists, we just write to it. edge case avoided!
#ELSE, modify an extant file. 
    #we can randomly select an extant file
else: 
    path=files[random.randint(0,len(files)-1)]
    modifier.alterSpecificFile(path,randomText)
    #I would LOVE to write a way to weigh the creation in a manner to resemble real repos, but I suppose I would need some data for that. maybe later. 
