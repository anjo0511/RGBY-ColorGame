# -*- coding: utf-8 -*-

from tkinter import *
from scoreSheetClass import ScoreSheetClass
from tkinter import messagebox

class ScoreInputFrame():

    def __init__(self,root):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        ''' 
        self.level = 10
        self.scoreSheet = 'top10scoreSheet'
        self.root =root
        self.frameLayout()

    def showFrame(self, bol=None):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''         
        if bol is True:
            self.scoreInputFrame.pack()
        elif bol is False:
            self.scoreInputFrame.pack_forget()  

    def frameLayout(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''         
        self.scoreInputFrame = Frame(self.root,bd=4,relief='solid',padx=50)    
        
        nameLabel = Label(self.scoreInputFrame,text='Name: ',font='Times 12 bold') 
        self.label_meassage=Label(self.scoreInputFrame,bd=1,font='Times 11 bold',padx=10,pady=5)

        self.entry1 = Entry(self.scoreInputFrame)

        spacer1 = Label(self.scoreInputFrame)
        infoLabel = Label(self.scoreInputFrame,text='Submit your record',font='Times 12 bold',pady=15)
        
        self.levelHighscore = StringVar()
        levelLable = Label(self.scoreInputFrame,textvariable= self.levelHighscore ,font='Times 12 bold',pady=5)
        self.levelHighscore.set('Level: 1')
        
        button1 = Button(self.scoreInputFrame,font='Times 12 bold',text='Submit',bg='red',bd=7,relief='raised',command = self.storeHighScore)
       
        infoLabel.grid(           row=0, columnspan=2)
        levelLable.grid(      row=1, columnspan=2)
        nameLabel.grid(           row=2, column=0)
        self.entry1.grid(         row=2, column=1)
        spacer1.grid(             row=3, columnspan=2)
        button1.grid(             row=4, columnspan=2)
        self.label_meassage.grid( row=5, columnspan=2)
    
    def chageScoreFrame(self,level):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.level = level
        self.levelHighscore.set('Level: '+ str(self.level))
    

    def storeHighScore(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''        
        if not self.entry1.get() == '':
            ScoreSheetClass(self.scoreSheet).scoreWrite(self.entry1.get(),self.level)
            ScoreSheetClass(self.scoreSheet).printScoreSheet()
            x = ScoreSheetClass(self.scoreSheet).getScoreList()
            messagebox.showinfo("Highscore Board", x)

            self.entry1.get()
            self.entry1.delete(0, 'end')

            self.label_meassage['text']= 'Thanks '
            self.label_meassage.after(700, lambda: self.label_meassage.config(text=''))
            self.scoreInputFrame.after(600, lambda: self.scoreInputFrame.pack_forget())
           
        else:
            self.label_meassage['text']= 'Submit a name'
            self.label_meassage.after(1000, lambda: self.label_meassage.config(text=''))
            print('Submit a name')



root = Tk()
root.geometry('500x500')
x = ScoreInputFrame(root)
x.showFrame(True)
for i in range(5):
    x.chageScoreFrame(i)

mainloop()

