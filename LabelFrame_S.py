# -*- coding: utf-8 -*-

from tkinter import *


class LabelFrame_S:
    
    def __init__(self,root,level,lives):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.level=level
        self.lives=lives

        self.root = root
        self.scoreFrame = Frame(
                                self.root,
                                bd=2,
                                relief='solid',
                                height=100,
                                width=600,
                                pady=20,
                                padx=200)
        self.topLabels()
        self.navegationButtons()

    def navegationButtons(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''        
        self.navBotton = Button(self.scoreFrame,text='Start', padx=5,pady=5,activebackground='blue')
        self.navBotton2 = Button(self.scoreFrame,text='Reset', padx=5,pady=5,activebackground='blue')
        self.navBotton3 = Button(self.scoreFrame,text='Highscores', padx=5,pady=5,activebackground='blue')
        self.navBotton4 = Button(self.scoreFrame,text='Back', padx=5,pady=5,activebackground='blue')
                
        self.navBotton.pack()
        self.navBotton2.pack(side=LEFT)
        self.navBotton3.pack(side=LEFT)
        self.navBotton4.pack(side=LEFT)


    def setLinktoNavButtons(self,function):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.function = function
        self.navBotton.bind('<ButtonRelease-1>', self.function)
        self.navBotton2.bind('<ButtonRelease-1>', self.function)
        self.navBotton3.bind('<ButtonRelease-1>', self.function)
        self.navBotton4.bind('<ButtonRelease-1>', self.function)
                

    def topLabels(self):
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

        self.chageLabelFrame(self.level,self.lives)
   
    def chageLabelFrame(self,level,lives):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.levelLable.set('Level: '+str(level))
        self.livesLable.set('Lives: '+str(lives))


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
     

