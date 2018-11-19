from tkinter import *

class poop:
    def restartLevel(self):
        sorry = "You failed the level! You lost a life but can still \n try again, press the button below to restart the level"
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
        self.countdownWindow()


x=poop()
x.nextLevel()