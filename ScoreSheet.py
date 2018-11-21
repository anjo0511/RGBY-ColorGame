# -*- coding: utf-8 -*-
from operator import itemgetter
import os
import pickle

'''
Pickling stores only one pyhton object at the time, the idea is to be able to store it in an
external file to later be able to restore the variable in the current session.
the external file is not readable but it is easy to use.
'''

class ScoreSheet():

    def __init__(self):

        self.sheetName = 'top10scoreSheet'

        if not os.path.isfile(self.sheetName): 
            newSheet = []  
            with open(self.sheetName,'wb') as file:
                pickle.dump(newSheet,file)
           
    def resetScoreSheet(self):
        ''' 
            Syfte: Basically overwrites the old score sheet by 
            creating a new empty with the same name.
            ReturvÃ¤rde: -
            Kommentarer: -
        '''
        emptyScoreList = []
        with open(self.sheetName,'wb') as file:
            pickle.dump(emptyScoreList,file)

    def scoreWrite(self ,name, score):
        ''' 
            Syfte: Opens the score sheet and rewrites it sorted by higest score (top 10)
            ReturvÃ¤rde: -
            Kommentarer: if the score given does not belong to the top 10, it wont show
        '''
        # unpickle
        self.name=name
        self.score=score
        self.scoreSheetList = self.getScoreList()
        self.scoreSheetList.append([self.name,self.score])
        self.scoreSheetList = sorted(self.scoreSheetList, key=itemgetter(1), reverse=True)[:10]
        # pickle
        with open(self.sheetName,'wb') as file:
            pickle.dump(self.scoreSheetList,file)

    def getScoreList(self):
        ''' 
            Syfte: Opens the score sheet and stores it in a variable
            ReturvÃ¤rde: A list of lists for the top 10 scores.
            Kommentarer: 
        '''''
        with open(self.sheetName,'rb') as file:
            self.scoreSheetList = pickle.load(file)
        return self.scoreSheetList    
        
    def getString(self):
        ''' 
            Syfte: Prints top 10 scores
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        pos = 1
        eachrow =''

        listOfLists = self.getScoreList()
        print('nb name'+' '*7+'level')
        for eachname in listOfLists:
            name,level = eachname
                       
            avst = 15 - len(name)
            avst = str(avst*' ')
            eachrow += str(pos)+'  '+name+avst+level+'\n'
            pos+=1
        
        return eachrow
        

