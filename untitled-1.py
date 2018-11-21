# -*- coding: utf-8 -*-

from tkinter import *
import time , random

from LabelFrame_S import LabelFrame_S
from ButtonFrame import ButtonFrame
from ScoreFrame import ScoreFrame




class mainWindow:
	def __init__(self):
		''' 
		    Syfte: 
		    ReturvÃ¤rde: -
		    Kommentarer: -
		''' 
		self.level=50
		self.lives=100

		self.root = Tk()

		self.order()		

		self.root.mainloop()
		
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
		
		
	def order(self):
		''' 
		    Syfte: 
		    ReturvÃ¤rde: 
		    Kommentarer: 
		'''		
		self.mainWinLayout()
		
		self.labelFrame = LabelFrame_S(self.root,self.level,self.lives)
		self.buttonFrame = ButtonFrame(self.root,self.level)
		self.scoreFrame = ScoreFrame(self.root,self.level)

		self.setnewLinks()
		self.labelFrame.showFrame(False)
		self.buttonFrame.showFrame(False)
		self.scoreFrame.showFrame(True)
	
	def setnewLinks(self):
		self.labelFrame.setLinktoNavButtons(self.navbuttonsNewlink)
		self.buttonFrame.setLinktoButtons(self.buttonsNew)

	def navbuttonsNewlink(self,event):
		print('nooooooooooooooooooooo')
		self.whichBotton = event.widget.cget('text') 
		print(self.whichBotton)
		if self.whichBotton== 'Start':
			self.buttonFrame.simulation()

		if self.whichBotton == 'Highscores':
			#self.scoreFrame.showFrame(True)            
			self.buttonFrame.showFrame(False)
			self.scoreFrame.showFrame(True) 

		elif self.whichBotton == 'Restart':
			self.buttonFrame.showFrame(False)
			self.labelFrame.chageScoreFrame(self.lives-1,20)

	def buttonsNew(self,event):
		print('yeeeeeeeeeeeeeeeeeeeeeeeeeey')



mainWindow()