
from tkinter import *

class CountDown:

    def startTimer(self):
        
        self.root = Toplevel()
        self.root.geometry('+700+300')
        self.countlabel = Label(self.root)
        self.countlabel.pack()
        self.timer3 = PhotoImage(file="3timer.png")
        self.timer2 = PhotoImage(file="2timer.png")
        self.timer1 = PhotoImage(file="1timer.png")
        self.countdownImageSwap(3)
        self.root.mainloop()
 
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
            #self.countlabel.destroy()
            self.root.destroy()
                                          
    # blink()
        else:
            self.t = self.t - 1
            self.countlabel.after(1000, self.countdownImageSwap)        

        
'''
x = CountDown()
x.startTimer()

print('Moderfucker')
'''
"""

class CountDown():
    def __init__(self, root):

        self.root = root
        self.countlabel = Label(self.root)        
        self.loadImages()    

    def loadImages(self):
        self.timer3 = PhotoImage(file="3timer.png")
        self.timer2 = PhotoImage(file="2timer.png")
        self.timer1 = PhotoImage(file="1timer.png")        
    
    def showFrame(self, bol=None):
        ''' 
            #Syfte: 
            #ReturvÃ¤rde: 
            #Kommentarer: 
        '''
        if bol is True:
            self.countlabel.pack()
        elif bol is False:
            self.countlabel.pack_forget()
    
    def startTimer(self):
        
        self.countlabel.after(100,lambda: self.countlabel.pack())
        self.countlabel.configure(image=self.timer3)
        self.countlabel.after(1000, lambda: self.countlabel.configure(image=self.timer2))
        self.countlabel.after(2000, lambda: self.countlabel.configure(image=self.timer1))
        self.countlabel.after(3000,lambda: self.countlabel.pack_forget())
    
    """
