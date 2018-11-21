

import time, random


class InternalCore:
    def __init__(self,level):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''         
        self.level = level
        self.tmpLevelSeq = []

        self.levelSeqMaker()

    def levelSeqMaker(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        ''' 
        for i in range(self.level):
            randomColor = random.choice('RYGB')
            self.tmpLevelSeq.append(randomColor)
        return self.tmpLevelSeq

    def curerntLevelList(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''         
        return(self.tmpLevelSeq)

    def resetGame(self,level):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        ''' 
        self.level = level
        self.tmpLevelSeq = []
        return self.tmpLevelSeq

