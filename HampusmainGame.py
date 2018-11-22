# -*- coding: utf-8 -*-

from tkinter import *
import time

from HighscoreFrame import HighScoreFrame
from InternalCore import InternalCore
from LabelFrame_S import LabelFrame_S
from ButtonFrame import ButtonFrame
from ScoreFrame import ScoreFrame
from ScoreSheet import ScoreSheet
from HampusCountdown import countdownWindow
'''
restart() method needs to call on cuntdown and later on 
sumulation again
'''

class mainWindow:
	def __init__(self):
		''' 
		    Syfte: 
		    ReturvÃ¤rde: 
		    Kommentarer: 
		''' 
		self.level=2
		self.lives=3

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
		self.labelFrame = LabelFrame_S(self.root,self.level,self.lives)
		self.buttonFrame = ButtonFrame(self.root)
		self.scoreFrame = ScoreFrame(self.root,self.level)
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
		x_coordinate =(screen_width/2-width_of_window/2)
		y_coordinate = (screen_height/2-height_of_window/2)
		self.root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
		
		
	def setNewLinksToFrames(self):
		''' 
		    Syfte: 
		    ReturvÃ¤rde: 
		    Kommentarer: 
		''' 		
		self.labelFrame.setLinktoNavButtons(self.navButtons)
		self.buttonFrame.setLinktoButtons(self.colourButtons)


	def navButtons(self,event):
		''' 
		    Syfte: 
		    ReturvÃ¤rde: -
		    Kommentarer: -
		''' 		
		whichBotton = event.widget.cget('text')

		if whichBotton== 'Start':
			'''
			countdown behovs
			'''		
			self.tmp = self.internalCore.curerntLevelList()
			self.buttonFrame.showFrame(False)
			countdownWindow(self.root, self.buttonFrame, self.tmp)
			self.buttonFrame.showFrame(True)
			print('Starting Countdown')
		#self.nextLevel och self.restartLevel ska kallas när spelaren 
		# klickar klart / klickar fel, de är bara här just nu för att testa.
			self.nextLevel()
		#			self.restartLevel()

		elif whichBotton == 'Highscores':
			tmp =  self.scoresheet.getString()
			self.highscoreFrame.changeHighscoreFrame(tmp)
			self.buttonFrame.showFrame(False)
			self.highscoreFrame.showFrame(True)
			print('Showing Highscores')		            
				
		elif whichBotton == 'Reset':						
			self.reset()

		elif whichBotton =='Back':
			self.buttonFrame.showFrame(True)
			self.highscoreFrame.showFrame(False)


	def reset(self):
		''' 
			Syfte: Does not start simulaton only restart internals
			ReturvÃ¤rde: 
			Kommentarer: 
		'''
		self.level = 1
		self.lives = 3
		self.labelFrame.chageLabelFrame(self.level,self.lives)
		self.internalCore.resetGame(self.level)
		self.internalCore.levelSeqMaker()
		
		print('\nReseting...')
		print('new seq: ',self.internalCore.curerntLevelList())
		print('Press start when you are ready!')


	def colourButtons(self,event):
		''' 
		    Syfte: 
		    ReturvÃ¤rde: -
		    Kommentarer: -
		''' 		
		#event.widget.bell(displayof=0)
		whichColour = event.widget.cget('text')

		if whichColour == 'R':
			print('red')
		elif whichColour == 'G':
			print('green')
		elif whichColour == 'B':
			print('blue')
		elif whichColour == 'Y':
			print('yellow')


	def liveComparison(self):
		''' 
			Syfte: 
			ReturvÃ¤rde: 
			Kommentarer: 
		'''        
		try:
			x= self.tmpLevel.pop(0)
			if x ==self.colorPressed:
				print('Correct')
				#print('CPU :',x,'User :',self.colorPressed)
			else:
				print('Wrong')
		except:
			print(self.tmpLevel)
			
			#print('Comparison Ended (Except loop)')
	
	def nextLevel(self):
		
		grats = "Congratulations, you made it!!\nPress the button to continue to the next level."
		
		self.nxtlvlpopup = Tk()
		self.nxtlvlpopup.wm_title("Congratulations!")
		
		nxtlvlLabel = Label(self.nxtlvlpopup, text=grats,padx=15 ,pady=15)
		nxtlvlLabel.pack()
		nxtlvlButton = Button(self.nxtlvlpopup, text="Next level",command = self.nextLevelCommands)
		nxtlvlButton.pack()
		spacer = Label(self.nxtlvlpopup,pady=5)
		spacer.pack()
		self.nxtlvlpopup.mainloop()
	
	def nextLevelCommands(self):
		self.buttonFrame.showFrame(False)
		self.nxtlvlpopup.destroy()
		self.level = self.level + 1
		self.labelFrame.chageLabelFrame(self.level, self.lives)
		self.internalCore = InternalCore(self.level)
		self.tmp = self.internalCore.curerntLevelList()
		countdownWindow(self.root, self.buttonFrame, self.tmp)
		self.buttonFrame.showFrame(True)

	def restartLevel(self):
		sorry = "You failed the level! You lost a life but can still try again, press the button below to restart the level"
		self.resetlvlpopup = Tk()
		self.resetlvlpopup.wm_title("FAIL!")
		resetlvlLabel = Label(self.resetlvlpopup, text=sorry,)
		resetlvlLabel.pack()
		resetlvlButton = Button(self.resetlvlpopup, text="Restart level", command = self.restartLevelCommands)
		resetlvlButton.pack()
		self.resetlvlpopup.mainloop()
	
	def restartLevelCommands(self):
		self.resetlvlpopup.destroy()
		self.lives = self.lives - 1
		self.labelFrame.chageLabelFrame(self.level, self.lives)
		self.tmp = self.internalCore.curerntLevelList()
		countdownWindow(self.root, self.buttonFrame, self.tmp)


mainWindow()