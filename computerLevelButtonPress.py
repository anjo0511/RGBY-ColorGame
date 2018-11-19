
from tkinter import * 
import tkinter.messagebox
import time
import random
from mainGamefile import MainApplicationLayout

'''
Här ger vi en lista till knapparna som sedan flashar beroende på sekvensen
'''

class ComputerSimulation(MainApplicationLayout):


    def __init__(self,root,scoreSheetName):
        super().__init__(root,scoreSheetName)
        self.randomList = []
        self.level = 5

    def randomClick(self):
        self.randomColor = random.choice('RYGB')
        return self.randomColor

    def gameLevelcomputerSequence(self):     
           
        for i in range(self.level):
            self.randomList.append(self.randomClick())
        #print('Seq to remember: ', randomList)
        return self.randomList

    def button2_click(self):
        randomColorList = self.gameLevelcomputerSequence()

        userinput = input('color? ')
        if userinput != '':
            time.sleep(1)
            for eachColor in randomColorList:
                print(eachColor)
                
                if eachColor == 'R':
                    self.button_R['activebackground']='white'
                    self.button_R.flash()
                    self.button_R.after(2000, lambda:self.button_R.configure(activebackground ='red'))          
                elif eachColor == 'G':
                    self.button_G['activebackground']='white'
                    self.button_G.flash()
                    self.button_G.after(2000, lambda:self.button_G.configure(activebackground ='green'))
                elif eachColor == 'B':
                    self.button_B['activebackground']='white'
                    self.button_B.flash()
                    self.button_B.after(2000, lambda:self.button_B.configure(activebackground ='blue'))
                elif eachColor == 'Y':
                    self.button_Y['activebackground']='white'
                    self.button_Y.flash()
                    self.button_Y.after(2000, lambda:self.button_Y.configure(activebackground ='yellow'))
                time.sleep(0.5)
                
        

root = Tk()

x =ComputerSimulation(root,'top10scoreSheet')

x.button2_click()

root.mainloop() 

