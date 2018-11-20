# -*- coding: utf-8 -*-
from tkinter import *

'''
This class build up both level and level Frame
Note we do not keep track of the score here,
the method changeScoreFrame takes in two integer,
representing the lives and levels

'''

class ScoreFrame():
    
    def __init__(self,root):

        self.root = root
        self.scoreFrame = Frame(
                                self.root,
                                bd=2,
                                relief='solid',
                                height=100,
                                width=600,
                                pady=20,
                                padx=200)
        self.baseLabels()

    def showFrame(self, bol=None):
        if bol is True:
            self.scoreFrame.pack()
        elif bol is False:
            self.scoreFrame.pack_forget()  

    def baseLabels(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.levelLable = StringVar()
        level_Label = Label(self.scoreFrame,textvariable=self.levelLable, font= 'Times 18')
        level_Label.pack()

        self.livesLable= StringVar()
        lives_Label = Label(self.scoreFrame,textvariable=self.livesLable,font= 'Times 18')    
        lives_Label.pack()

        self.levelLable.set('Level 1')
        self.livesLable.set('Lives 3')

    def chageScoreFrame(self,lives,level):

        self.levelLable.set('Level '+str(level))
        self.livesLable.set('Lives '+str(lives))



root = Tk()

x = ScoreFrame(root)

ans = input('Ska jag visa pÃ¥ng tavlan planet?: ')
if ans == 'y':
    x.showFrame(True)
    ans2 = input('Ska jag Ã¤ndra pÃ¥ scoreSheet?')
    if ans2 == 'y':
        x.chageScoreFrame(30,123)
        

root.mainloop()
