from operator import itemgetter
import os
import pickle

'''
Pickling stores only one pyhton object at the time, the idea is to be able to store it in an
external file to later be able to restore the variable in the current session.
the external file is not readable but it is easy to use.
'''

class ScoreSheetClass():

    def __init__(self, sheetName='top10scoreSheet'):

        self.sheetName = sheetName

        if not os.path.isfile(self.sheetName): 
            newSheet = []  
            with open(self.sheetName,'wb') as file:
                pickle.dump(newSheet,file)
           
    def resetScoreSheet(self):
        ''' 
            Syfte: Basically overwrites the old score sheet by 
            creating a new empty with the same name.
            Returvärde: -
            Kommentarer: -
        '''
        emptyScoreList = []
        with open(self.sheetName,'wb') as file:
            pickle.dump(emptyScoreList,file)

    def scoreWrite(self ,name, score):
        ''' 
            Syfte: Opens the score sheet and rewrites it sorted by higest score (top 10)
            Returvärde: -
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
            Returvärde: A list of lists for the top 10 scores.
            Kommentarer: 
        '''''
        with open(self.sheetName,'rb') as file:
            self.scoreSheetList = pickle.load(file)
        return self.scoreSheetList    
        
    def printScoreSheet(self):
        ''' 
            Syfte: Prints top 10 scores
            Returvärde: 
            Kommentarer: 
        '''
        pos = 1
        listOfLists = self.getScoreList()
        print('  name : score')
        for miniList in listOfLists:
            name, score = [miniList[0],miniList[1]]
            print(pos,name,':',score)
            pos +=1
