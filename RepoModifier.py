
import random
import nltk as nl
import subprocess
import os
import math
import time
from nltk.corpus import words


#RepoModifier should NEVER be created, choose one of the subclasses.
class RepoModifier:

    def __init__(self, path, data):
        self.path=path
        self.data=data

    #need to decode the directories and files that exist first. might want to do this in a separate method
    #this is a single-layer version of whatInRepo. maybe helpful for digging at a specific level but
    #mostly rendered obsolete by whatInRepo for our purposes
    def whatInDir(self, dirpath):
        print(dirpath)
        test=subprocess.run(['ls'],cwd=dirpath,capture_output=True)
        og=test.stdout.decode('ascii').split('\n')
        # print('test:',test)
        og.pop(0)#removes the count of files in dir
        for i in og:
            print(i)
        #verify we're in the right location
        subprocess.run('pwd')


    #returns a list of all DIRS and files in the repo, minus the root of the repo. append that after method call.
    def whatInRepo(self,repoPath):
        dirs=[]
        files=[]
        for i in os.scandir(repoPath):
            if (i.is_dir() and (i.name != '.git')):#excluding .git dir
                dirs.append(i.path)#.path? .name?
            if i.is_file():
                files.append(i.path)
        for dirname in list(dirs):
            x,y=RepoModifier.whatInRepo(self,dirname)
            dirs.extend(x)
            files.extend(y)
        return dirs,files

    def containsDupes(self,name):
        name.sort()
        for i in range (0,len(name)-1):
            if name[i]==name[i+1]:
                return True
        return False
    #moves the process to the given directory in path
    def movetoRepo(self,repoPath):
        os.chdir(repoPath)
        #verify we're in the right location
        subprocess.run('pwd')

    #makes a folder named the given name
    def makeFolder(self,path,folderName):
        print ("makeFolder")
        print (path)
        try: 
            subprocess.run(['mkdir', folderName], cwd=path)
            print('ran subprocess')
        except TypeError:
            print("folderName var is not a string! no folder was made")


    #changes an extant file, or creates it if it DNE 
    #abstract method.    
    def alterSpecificFile(self,file):
        pass
    
    #abstract
    def buildName():
        pass

    #abstract
    def buildFileInput():
        pass

#uses chatgpt to make file/folder names and to fill files
#designed for 
    # nonsense given by chatGPT
#currently unimplemented
class ChatModifier(RepoModifier):
    pass

#uses random words to make file/folder names and to fill files
#designed for 
    # random words
class RandomWordModifier(RepoModifier):

    nl.download('words')
    DICTIONARY = words.words()
    DICTLEN = len(DICTIONARY)

    def getRandomWord(self):
        print(self.DICTLEN)
        num=round(self.DICTLEN*random.random())
        #needed for the edge cases. we'll just overflow. I guess we could just do a try/catch?
        if  num == self.DICTLEN:
            num = 0
        return self.DICTIONARY[num]#I guess this still has a chance of causing an issue of the -1 edge

    #builds a random name from 1-4 random words
    def buildName(self):
        builtName=self.getRandomWord()
        i=2
        while i >0:
            if random.random()>0.5:
                builtName+=self.getRandomWord()
            i-=1

        return builtName
    
    def buildFileInput(self,length):
        outputToFile=""
        while length>0:
            outputToFile+=(self.getRandomWord())
            length-=1
        return outputToFile

    #for now we only write
    def alterSpecificFile(self,filePath, stringLen):  
        f=open(filePath,'a')
        return subprocess.run(['echo',self.buildFileInput(stringLen)],stdout=f)

#uses pre-designed groups of text and function blocks to make file/folder names and fill files. 
#designed to make 
    # random pre-designed standard coding structures(?) blocks?
#currently unimplemented
class blockfunctionsModifier(RepoModifier):

    def writeData(self,):
        pass
    def writeLoop(self,):
        pass   

