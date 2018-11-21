from tkinter import *
from InternalCore import InternalCore

def nextLevel(self):
    grats = "Congratulations on beating the level! Press the button below to proceed to the next level"
    self.nxtlvlpopup = Tk()
    self.nxtlvlpopup.wm_title("Congratulations!")
    nxtlvlLabel = Label(self.nxtlvlpopup, text=grats, font=("Times", 10))
    nxtlvlLabel.pack()
    nxtlvlButton = Button(self.nxtlvlpopup, text="Next level", command = self.nextLevelCommands)
    nxtlvlButton.pack()
    self.nxtlvlpopup.mainloop()

def nextLevelCommands(self):
    self.nxtlvlpopup.destroy()
    self.level = self.level + 1
    self.labelFrame.chageLabelFrame(self.level, self.lives)
    self.internalCore = InternalCore(self.level)
    self.tmp = self.internalCore.curerntLevelList()
    countdownWindow(self.root, self.buttonFrame, self.tmp)