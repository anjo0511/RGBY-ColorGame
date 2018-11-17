from tkinter import *

def restartLevel(self):
    sorry = "You failed the level! You lost a life but can still try again, press the button below to restart the level"
    self.resetlvlpopup = Tk()
    self.resetlvlpopup.wm_title("FAIL!")
    resetlvlLabel = Label(self.resetlvlpopup, text=sorry, font=("Times", 10))
    resetlvlLabel.pack()
    resetlvlButton = Button(self.resetlvlpopup, text="Restart level", command = self.restartLevelCommands)
    resetlvlButton.pack()
    self.resetlvlpopup.mainloop()

def restartLevelCommands(self):
    self.resetlvlpopup.destroy()
    self.lives = self.lives - 1
    self.countdownWindow()