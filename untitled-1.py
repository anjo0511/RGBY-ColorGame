# -*- coding: utf-8 -*-

from tkinter import *
import time
import random
import tkinter.messagebox
from scoreSheetClass import ScoreSheetClass

from newButtonFrame import ButtonFrame
from newLabelFrame import ScoreFrame
from newSoreInputFrame import ScoreInputFrame


class mainWindow():
	def __init__(self):
		''' 
		    Syfte: 
		    ReturvÃ¤rde: -
		    Kommentarer: -
		''' 
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
		
		self.score = ScoreFrame(self.root)
		self.buttons = ButtonFrame(self.root)
		#self.userInput = ScoreInputFrame(self.root)
		self.setnewLinks()
		self.score.showFrame(True)
		self.buttons.showFrame(True)
	
	def setnewLinks(self):
		self.score.setLinktoNavButtons(self.navbuttonsNewlink)
		self.buttons.setLinktoButtons(self.buttonsNew)

	def navbuttonsNewlink(self,event):
		print('nooooooooooooooooooooo')
		
	def buttonsNew(self,event):
		print('yeeeeeeeeeeeeeeeeeeeeeeeeeey')

mainWindow()