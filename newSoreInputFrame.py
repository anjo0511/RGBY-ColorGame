from tkinter import *
import tkinter.messagebox
import random

from scoreSheetClass import ScoreSheetClass

class ScoreInputFrame():

    def __init__(self,root):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        ''' 
        self.scoreSheet = 'top10scoreSheet'
        self.root =root
        self.frameLayout()

    def showFrame(self, bol=None):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        '''         
        if bol is True:
            self.scoreInputFrame.pack()
        elif bol is False:
            self.scoreInputFrame.pack_forget()  

    def frameLayout(self):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        '''         
        self.scoreInputFrame = Frame(self.root,bd=4,relief='solid',height=180, width=250)

        
        nameLabel = Label(self.scoreInputFrame,text='Name: ',font='Times 12 bold') 
        self.label_meassage=Label(self.scoreInputFrame,bd=1,font='Times 11 bold',padx=10,pady=5,bg='red')

        self.entry1 = Entry(self.scoreInputFrame)

        spacer1 = Label(self.scoreInputFrame,bg='red')
        infoLabel = Label(self.scoreInputFrame,pady=4,text='Submit highscore',font='Times 12 bold')
        
        button1 = Button(self.scoreInputFrame,font='Times 12 bold',text='Submit',bg='red',bd=7,relief='raised',command = self.storeHighScore)
       
        infoLabel.grid(           row=0, columnspan=2)
        nameLabel.grid(           row=1, column=0)
        self.entry1.grid(         row=1, column=1)
        spacer1.grid(             row=2, columnspan=2)
        button1.grid(             row=3, columnspan=2)
        self.label_meassage.grid( row=4, columnspan=2)

    def storeHighScore(self):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        '''        
        if not self.entry1.get() == '':
            ###This random seq needs to be removed to allow users to enter their scores
            self.random_score = random.randint(100,2682)
            print(self.entry1.get(),self.random_score)
            
            ScoreSheetClass(self.scoreSheet).scoreWrite(self.entry1.get(),self.random_score)
            ScoreSheetClass(self.scoreSheet).printScoreSheet()

            self.entry1.get()
            self.entry1.delete(0, 'end')

            self.label_meassage['text']= 'Thanks '
            self.label_meassage.after(700, lambda: self.label_meassage.config(text=''))
            self.scoreInputFrame.after(600, lambda: self.scoreInputFrame.pack_forget())
           
        else:
            self.label_meassage['text']= 'Submit a name'
            self.label_meassage.after(1000, lambda: self.label_meassage.config(text=''))
            print('Submit a name')






root =Tk()

x=ScoreInputFrame(root)

ans = input('Ska jag visa spel inputFramen?: ')
if ans == 'y':
    x.showFrame(True)
    ans2 = input('Igen?: ')
    if ans == 'y':
        x.showFrame(True)
        
root.mainloop()