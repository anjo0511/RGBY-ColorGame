from tkinter import *

from ScoreSheet import ScoreSheet



class HighScoreFrame():

    def __init__(self,root):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        ''' 
        self.root = root       
        
        self.highscoreFrameLayout()
        self.scoreSheet = ScoreSheet().getString()        
        

    def highscoreFrameLayout(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''           
        self.highScoreFrame = Frame(self.root, bd=4, relief='solid', padx=50)    
        
        self.highScore_var = StringVar()   
        
        self.theonlyLabel=Label(self.highScoreFrame,textvariable=self.highScore_var,bd=1,font='Times 11 bold',padx=10,pady=5)        
        self.theonlyLabel.pack()


    def changeHighscoreFrame(self,textstring):
        self.highScore_var.set(textstring)

    def showFrame(self, bol=None):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''         
        if bol is True:
            self.highScoreFrame.pack()
        elif bol is False:
            self.highScoreFrame.pack_forget() 

