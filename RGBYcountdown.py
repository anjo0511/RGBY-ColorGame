"""
Kommentar: To run the countdown u need 3 images named "3timer.png, 2timer.png, 1timer.png"
Which are just images with the numbers 3, 2 and 1 on them (They need to be in same folder).
"""
from tkinter import *
"""
def countdownWindow(self, root):

    self.countlabel = Label()
    self.countlabel.pack()
    self.timer3 = PhotoImage(file="3timer.png")
    self.timer2 = PhotoImage(file="2timer.png")
    self.timer1 = PhotoImage(file="1timer.png")
    self.countdownImageSwap(3)

def countdownImageSwap(self, counter = False):

    if counter:
        self.t = counter
    if self.t == 3:
        self.countlabel.configure(image=self.timer3)          
    if self.t == 2:
        self.countlabel.configure(image=self.timer2)  
    if self.t == 1:
        self.countlabel.configure(image=self.timer1)
#When countdown reaches 0 the blink pattern will start
    if self.t == 0:
        counter = False
        self.countlabel.destroy()
#        blink()
    else:
        self.t = self.t - 1
        self.countlabel.after(1000, self.countdownImageSwap)        

"""
#from ButtonFrame import ButtonFrame

class countdownWindow():
    def __init__(self, root, buttonframe, level):
        self.level = level
        self.buttonframe = buttonframe
        self.countlabel = Label()
        self.countlabel.pack()
        self.timer3 = PhotoImage(file="3timer.png")
        self.timer2 = PhotoImage(file="2timer.png")
        self.timer1 = PhotoImage(file="1timer.png")
        self.countdownImageSwap(4)

    def countdownImageSwap(self, counter = False):
        if counter:
            self.t = counter
        if self.t == 4:
            self.countlabel.configure(image=self.timer3)          
        if self.t == 3:
            self.countlabel.configure(image=self.timer2)  
        if self.t == 2:
            self.countlabel.configure(image=self.timer1)
#When countdown reaches 0 the blink pattern will start
        if self.t == 1:
            self.countlabel.pack_forget()
        if self.t == 0:
            self.buttonframe.simulation(self.level)
        else:
            self.t = self.t - 1
            self.countlabel.after(1000, self.countdownImageSwap)

"""
root = countdownWindow()
root.mainloop()
"""