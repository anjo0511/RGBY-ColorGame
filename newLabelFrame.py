# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from newButtonFrame import ButtonFrame
from scoreSheetClass import ScoreSheetClass
'''
This class build up both level and level Frame
Note we do not keep track of the score here,
the method changeScoreFrame takes in two integer,
representing the lives and levels

'''

class ScoreFrame():
    
    def __init__(self,root):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
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
        self.navegationButtons()

    def navegationButtons(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''        
        self.navBotton = Button(self.scoreFrame,text='Start', padx=5,pady=5,activebackground='blue')
        self.navBotton2 = Button(self.scoreFrame,text='Restart', padx=5,pady=5,activebackground='blue')
        self.navBotton3 = Button(self.scoreFrame,text='Highscore Board', padx=5,pady=5,activebackground='blue')
                
        self.navBotton.pack(side=LEFT)
        self.navBotton2.pack(side=LEFT)
        self.navBotton3.pack(side=LEFT)
        
        self.navBotton.bind('<ButtonRelease-1>', self.navEvent)
        self.navBotton2.bind('<ButtonRelease-1>', self.navEvent)
        self.navBotton3.bind('<ButtonRelease-1>', self.navEvent)
        
    def navEvent(self,event):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''        
        self.whichBotton = event.widget.cget('text')         

        if self.whichBotton == 'Highscore Board':            
            messagebox.showinfo("Highscore Board", "Here is the shit")
            print('showing highscore')
    
        elif self.whichBotton == 'Restart':
            print('Restart')
            
        elif self.whichBotton == 'Start':
            #self.startSimulation()
            print('Start')            
            
    def showFrame(self, bol=None):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
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
        level_Label = Label(self.scoreFrame,textvariable=self.levelLable, font= 'Times 18',pady=5)
        level_Label.pack()

        self.livesLable= StringVar()
        lives_Label = Label(self.scoreFrame,textvariable=self.livesLable,font= 'Times 18',pady=15)    
        lives_Label.pack()

        self.levelLable.set('Level 1')
        self.livesLable.set('Lives 3')        

        
    def startSimulation(self,buttons=None):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''        
        if self.whichBotton == 'Start':
            return True
        else:   
            return False        
    

    def chageScoreFrame(self,lives,level):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.levelLable.set('Level '+str(level))
        self.livesLable.set('Lives '+str(lives))


