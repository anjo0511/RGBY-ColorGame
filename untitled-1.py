# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
import time, random

from HighscoreFrame import HighScoreFrame
from LabelFrame_S import LabelFrame_S
from ButtonFrame import ButtonFrame
from ScoreFrame import ScoreFrame
from ScoreSheet import ScoreSheet

from HampusCountdown import countdownWindow

'''
dont forget to add the scorewindow when losing
Everything works there is just something wrong with 
reset and restart 
'''

class mainWindow:
    def __init__(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.level = 1
        self.lives = 3
        '''
        self.tmpLevelSeq=[]
        '''

        self.root = Tk()
        self.startingOrder()
        self.root.mainloop()

    def startingOrder(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.mainWinLayout()
        self.highscoreFrame = HighScoreFrame(self.root)
        self.labelFrame = LabelFrame_S(self.root, self.level, self.lives)
        self.buttonFrame = ButtonFrame(self.root)
        self.scoreFrame = ScoreFrame(self.root)
        self.scoresheet = ScoreSheet()
        self.setNewLinksToFrames()

        self.labelFrame.showFrame(True)
        self.buttonFrame.showFrame(True)
        self.scoreFrame.showFrame(False)
        self.highscoreFrame.showFrame(False)


    def mainWinLayout(self):
        ''' 
            Syfte: Center the main window and gives it nice appearence
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.root.title('RGBY-ColorGame 1.0')
        self.root.resizable(width=False, height=False)
        width_of_window = 600
        height_of_window = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width/2-width_of_window/2)
        y_coordinate = (screen_height/2-height_of_window/2)
        self.root.geometry("%dx%d+%d+%d" % (width_of_window,
                                            height_of_window, x_coordinate, y_coordinate))


    def setNewLinksToFrames(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.labelFrame.setLinktoNavButtons(self.navButtons)
        self.buttonFrame.setLinktoButtons(self.colourButtons)


    def navButtons(self, event):
        ''' 
            Syfte: 
            ReturvÃ¤rde: -
            Kommentarer: -
        '''
        whichBotton = event.widget.cget('text')

        if whichBotton == 'Start' and self.lives != 0:
            self.tmpLevelSeq = self.levelSeqMaker(self.level)            
            self.highscoreFrame.showFrame(False)
            self.buttonFrame.showFrame(False)
            countdownWindow(self.root, self.buttonFrame,self.tmpLevelSeq)
            self.buttonFrame.showFrame(True)
            self.setNewLinksToFrames()
            print('Start Button',self.tmpLevelSeq)

        elif whichBotton == 'Highscores':
            highscore_var = self.scoresheet.getString()
            self.highscoreFrame.changeHighscoreFrame(highscore_var)
            self.buttonFrame.showFrame(False)
            self.highscoreFrame.showFrame(True)
            print('Highscores Button')

        elif whichBotton == 'Reset':
            print('Reset Button')
            self.resetButton()

        elif whichBotton == 'Back' and self.lives != 0:
            self.buttonFrame.showFrame(True)
            self.highscoreFrame.showFrame(False)
            print('Back Button')


    def resetButton(self):
        ''' 
                Syfte: Does not start simulaton only restart internals
                ReturvÃ¤rde: 
                Kommentarer: 
        '''
        self.level = 1
        self.lives = 3
        self.tmpLevelSeq = self.levelSeqMaker(self.level)
        self.labelFrame.chageLabelFrame(self.level, self.lives)
        
        messagebox.showinfo('Restar Done',
        'Now you can give it another try, press start whenever you are ready, good luck :)')
        print('........Reseting Done........\n')


    def colourButtons(self, event):
        ''' 
            Syfte: Sends the colour pressed to be compared
            ReturvÃ¤rde: -
            Kommentarer: Prints which colour to display on terminal 
            for easy use.
        '''
        #event.widget.bell(displayof=0)
        whichColour = event.widget.cget('text')       
        self.liveComparison(whichColour)
		
        if whichColour == 'R':
            print('---> user Red')
        elif whichColour == 'G':
            print('---> user Green')
        elif whichColour == 'B':
            print('---> user Blue')
        elif whichColour == 'Y':
            print('---> user Yellow')
		
    def liveComparison(self,colour):
        
        
        print('*********************************************',self.tmpLevelSeq)
        if self.tmpLevelSeq != []:
            cpUcolor = self.tmpLevelSeq.pop(0)
            if cpUcolor != colour:                               
                self.restartLevel()
            elif cpUcolor == colour and self.tmpLevelSeq == []:
                self.nextLevel()
                print('Next level')


    def nextLevel(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        var_0 = "Congratulations, you made it!!\nClick to continue to the next level."

        tmpMsg0 = messagebox.showinfo("Winner", var_0)
        if tmpMsg0 == 'ok':
            self.nextLevelCommands()

    def nextLevelCommands(self):
        ''' 
                Syfte: 
                ReturvÃ¤rde: 
                Kommentarer: 
        '''
        self.buttonFrame.showFrame(False)
        self.level = self.level + 1
        self.labelFrame.chageLabelFrame(self.level, self.lives)
        self.tmpLevelSeq = self.levelSeqMaker(self.level)
        countdownWindow(self.root, self.buttonFrame,self.tmpLevelSeq)
        self.setNewLinksToFrames()
        self.buttonFrame.showFrame(True)

    def restartLevel(self):
        ''' 
                Syfte: 
                ReturvÃ¤rde: 
                Kommentarer: 
        '''
        if self.lives > 1:
            var_2 = "Oops you got it wrong, click to restart level"
            tmpMsg2 = messagebox.showinfo("You lost a live", var_2)
            if tmpMsg2 == 'ok':
                self.restartLevelCommands()

        else:
            var_1 = 'You dont have any lives left, reset the game!'
            tmpMsg1 = messagebox.showwarning("Loser", var_1)
            if tmpMsg1 == 'ok':
                self.buttonFrame.showFrame(False)                
                self.scoreFrame.chageScoreFrame(self.level)
                self.scoreFrame.showFrame(True)
                self.resetButton()

    def restartLevelCommands(self):
        ''' 
                Syfte: 
                ReturvÃ¤rde: 
                Kommentarer: 
        '''
        self.buttonFrame.showFrame(False)
        self.lives = self.lives-1
        self.tmpLevelSeq = self.levelSeqMaker(self.level)
        self.labelFrame.chageLabelFrame(self.level, self.lives)
        countdownWindow(self.root, self.buttonFrame,self.tmpLevelSeq)
        self.setNewLinksToFrames()
        self.buttonFrame.showFrame(True)

    def levelSeqMaker(self,level):
        ''' 
            Syfte: Empties the current level list and randomizes 
                a new one depening on the level.
            ReturvÃ¤rde: 
            Kommentarer: 
        ''' 
        self.tmpLevelSeq = []
        for i in range(level):
            randomColor = random.choice('RYGB')
            self.tmpLevelSeq.append(randomColor)
        return self.tmpLevelSeq

mainWindow()
