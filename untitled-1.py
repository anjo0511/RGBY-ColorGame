# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
import time

from HighscoreFrame import HighScoreFrame
from InternalCore import InternalCore
from LabelFrame_S import LabelFrame_S
from ButtonFrame import ButtonFrame
from ScoreFrame import ScoreFrame
from ScoreSheet import ScoreSheet

from HampusCountdown import countdownWindow


class mainWindow:
    def __init__(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        self.level = 1
        self.lives = 3

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
        self.internalCore = InternalCore(self.level)
        self.highscoreFrame = HighScoreFrame(self.root)
        self.labelFrame = LabelFrame_S(self.root, self.level, self.lives)
        self.buttonFrame = ButtonFrame(self.root)
        self.scoreFrame = ScoreFrame(self.root, self.level)
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
            self.highscoreFrame.showFrame(False)
            self.tmp = self.internalCore.curerntLevelList()
            self.buttonFrame.showFrame(False)
            countdownWindow(self.root, self.buttonFrame, self.tmp)
            self.buttonFrame.showFrame(True)
            print('Start Button')

        elif whichBotton == 'Highscores':
            tmp = self.scoresheet.getString()
            self.highscoreFrame.changeHighscoreFrame(tmp)
            self.buttonFrame.showFrame(False)
            self.highscoreFrame.showFrame(True)
            print('Highscores Button')

        elif whichBotton == 'Reset':
            self.reset()
            messagebox.showinfo(
                'Restart the Game', 'Now you are able to give it another try, good luck')
            print('Reset Button')

        elif whichBotton == 'Back' and self.lives != 0:
            self.buttonFrame.showFrame(True)
            self.highscoreFrame.showFrame(False)
            print('Back Button')

    def reset(self):
        ''' 
                Syfte: Does not start simulaton only restart internals
                ReturvÃ¤rde: 
                Kommentarer: 
        '''
        self.level = 1
        self.lives = 3
        self.labelFrame.chageLabelFrame(self.level, self.lives)
        self.internalCore.resetGame(self.level)
        self.internalCore.levelSeqMaker()

        print('\nReseting...')
        print('new seq: ', self.internalCore.curerntLevelList())
        print('Press start when you are ready!')

    def colourButtons(self, event):
        ''' 
            Syfte: 
            ReturvÃ¤rde: -
            Kommentarer: -
        '''
        #event.widget.bell(displayof=0)
        whichColour = event.widget.cget('text')       
        self.liveComparison(whichColour)

		
    def liveComparison(self,colour):
        
        if len(self.tmp) != 0:
            cpUcolor = self.tmp.pop(0)
        if cpUcolor != colour:
            self.restartLevel()
            print('Restarting, Wrong Color')
        else:
            self.nextLevel()
            print('Next level')


    def nextLevel(self):
        ''' 
            Syfte: 
            ReturvÃ¤rde: 
            Kommentarer: 
        '''
        grats = "Congratulations, you made it!!\nPress the button to continue to the next level."

        x = messagebox.showinfo("Winner", grats)
        if x == 'ok':
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
        self.internalCore = InternalCore(self.level)
        self.tmp = self.internalCore.curerntLevelList()
        countdownWindow(self.root, self.buttonFrame, self.tmp)
        self.buttonFrame.showFrame(True)

    def restartLevel(self):
        ''' 
                Syfte: 
                ReturvÃ¤rde: 
                Kommentarer: 
        '''
        if self.lives == 0:
            sorry2 = 'You dont have eonugh lives, reset the game'
            x = messagebox.showwarning("Loser", sorry2)
            if x == 'ok':
                self.buttonFrame.showFrame(False)

        else:
            sorry = "You failed, you have one life less. Press the button below to continue"
            x = messagebox.showinfo("Loser", sorry)
            if x == 'ok':
                self.restartLevelCommands()

    def restartLevelCommands(self):
        ''' 
                Syfte: 
                ReturvÃ¤rde: 
                Kommentarer: 
        '''
        self.buttonFrame.showFrame(False)
        self.lives = self.lives - 1
        self.labelFrame.chageLabelFrame(self.level, self.lives)
        self.tmp = self.internalCore.curerntLevelList()
        countdownWindow(self.root, self.buttonFrame, self.tmp)
        self.buttonFrame.showFrame(True)


mainWindow()
