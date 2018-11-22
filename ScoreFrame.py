# -*- coding: utf-8 -*-

from tkinter import *
from ScoreSheet import ScoreSheet

'''
This class is done nothing else needs to be adjusted
'''
class ScoreFrame():

    def __init__(self,root):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        ''' 
        self.root = root       
        self.scoreFrameLayout()
        self.scoreSheet = ScoreSheet()
        

    def scoreFrameLayout(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''           
        self.inputFrame = Frame(self.root, bd=4, relief='solid', padx=50)    
        
        self.entry1 = Entry(self.inputFrame)                  
        self.label_meassage=Label(self.inputFrame,bd=1,font='Times 11 bold',padx=10,pady=5)        
        self.button1 = Button(self.inputFrame,font='Times 12 bold',text='Submit',bg='red',bd=7,relief='raised')
        
        self.button1.bind('<ButtonRelease-1>',self.storeHighScore)

        self.scoreVariable = StringVar()
        spacer1 = Label(self.inputFrame)
        nameLabel = Label(self.inputFrame,text='Name: ',font='Times 12 bold') 
        infoLabel = Label(self.inputFrame,text='Submit your record',font='Times 12 bold',pady=15)
        levelLable = Label(self.inputFrame,textvariable= self.scoreVariable ,font='Times 12 bold',pady=5)
        
        self.chageScoreFrame(' ')              
       
        infoLabel.grid(           row=0, columnspan=2)
        levelLable.grid(          row=1, columnspan=2)
        nameLabel.grid(           row=2, column=0)
        self.entry1.grid(         row=2, column=1)
        spacer1.grid(             row=3, columnspan=2)
        self.button1.grid(        row=4, columnspan=2)
        self.label_meassage.grid( row=5, columnspan=2)
    
    def chageScoreFrame(self,level):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''  
        self.level = level      
        self.scoreVariable.set('Level: '+ str(self.level))
    
    def storeHighScore(self,event):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        name = self.entry1.get()
        if name == '':
            self.label_meassage['text']= 'Submit a name'
            self.label_meassage.after(1000, lambda: self.label_meassage.config(text=''))
            self.entry1['bg']= '#f08080'            
            self.entry1.after(300,lambda: self.entry1.config(bg='white'))
            
        elif not len(name) > 15:

            self.scoreSheet.scoreWrite(name,self.level)
                   
            self.entry1.delete(0,END)

            self.label_meassage['text']= 'Thanks '
            self.label_meassage.after(700, lambda: self.label_meassage.config(text=''))
            self.inputFrame.after(600, lambda: self.inputFrame.pack_forget())
           
        else:
            self.entry1['bg']= '#f08080'            
            self.entry1.after(300,lambda: self.entry1.config(bg='white'))

            self.label_meassage['text']= 'Shorter, less than 15 characters'
            self.label_meassage.after(1000, lambda: self.label_meassage.config(text=''))            

    def showFrame(self, bol=None):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''         
        if bol is True:
            self.inputFrame.pack()
        elif bol is False:
            self.inputFrame.pack_forget()  


