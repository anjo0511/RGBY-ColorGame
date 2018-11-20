from tkinter import *
import tkinter.messagebox
import random
import time

from scoreSheetClass import ScoreSheetClass
from newButtonFrame import ButtonFramme
from newScoreLabelFrame import ScoreFrame
from RGBYcountdown import countdownWindow


class MainApplicationLayout():

    def __init__(self):
        ''' 
            Syfte: -
            Returvärde: -
            Kommentarer: -
        '''
        root = Tk()
        self.level = 1 
        self.root = root
        self.rootWindow()     
        root.mainloop() 

    def rootWindow(self):
        ''' 
            Syfte: Center the main window and gives it nice appearence
            Returvärde: -
            Kommentarer: -
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
        self.liveslevel = ScoreFrame(self.root)
        self.liveslevel.showFrame(True)
        self.countdown = countdownWindow(self.root)
        

MainApplicationLayout()
