"""
Kommentar: To run the countdown u need 3 images named "3timer.png, 2timer.png, 1timer.png"
Which are just images with the numbers 3, 2 and 1 on them (They need to be in same folder).
"""
from tkinter import *

def countdownWindow(self):
    """
        Syfte: Creates a label which will show time until blink starts using images
        Returv�rde: -
        Parametrar: -
    """
    self.countlabel = Label()
    self.countlabel.pack()
    self.timer3 = PhotoImage(file="3timer.png")
    self.timer2 = PhotoImage(file="2timer.png")
    self.timer1 = PhotoImage(file="1timer.png")
    self.countdownImageSwap(3)

def countdownImageSwap(self, counter = False):
    """
        Syfte: Changes image every second to represent a countdown
        Returv�rde:
        Parametrar: Counter that controls when the loop shall stop and what image should be displayed.
    """
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


#The code below can be run to be test the countdown module, simply remove the """ at start and end.

class countdownWindow(Tk):

    
    def __init__(self):
        Tk.__init__(self)
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
#            blink()
        else:
            self.t = self.t - 1
            self.countlabel.after(1000, self.countdownImageSwap)

root = countdownWindow()
root.mainloop()
