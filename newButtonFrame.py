
from tkinter import *
import time
import random

class ButtonFramme:

    def __init__(self, root, level=1):

        self.level = level
        self.root = root
        self.buttonFrame = Frame(
                                self.root,
                                bd=2,
                                relief='solid',
                                height=150,
                                width=200)
        self.baseButtons()
    
    def changeLevel(self,level):
        self.level=level

    def showFrame(self, bol=None):
        if bol is True:
            self.buttonFrame.pack()
        elif bol is False:
            self.buttonFrame.pack_forget()

    def userClickedButton(self,event):    
        #event.widget.bell(displayof=0)
        self.colorPressed = event.widget.cget('text')
        self.userColorList([self.colorPressed])
        print(self.colorPressed)
        
    def userColorList(self,colorPressed):
        self.lvlList=[]
        pressed = colorPressed

        if len(self.lvlList) < self.level and self.lvlList != []:
            self.lvlList += pressed
        #print(self.lvlList)
        '''
        userColorSequenceList=[]    
        if len(userColorSequenceList) < self.level:
            userColorSequenceList.append(colorPressed)
            print(userColorSequenceList)

        if len(userColorSequenceList) == self.level:
            print('Seq user pressed: ', userColorSequenceList)
        return userColorSequenceList
        '''

    def baseButtons(self):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        '''
        self.button_R = Button(self.buttonFrame, text='R', bg='red',
                          height=4, width=8, bd=7, relief='raised')
        self.button_G = Button(self.buttonFrame, text='G', bg='green',
                          height=4, width=8, bd=7, relief='raised')
        self.button_B = Button(self.buttonFrame, text='B', bg='blue',
                          height=4, width=8, bd=7, relief='raised')
        self.button_Y = Button(self.buttonFrame, text='Y', bg='yellow',
                          height=4, width=8, bd=7, relief='raised')

        self.button_R.grid(row=0, column=0)
        self.button_G.grid(row=0, column=1)
        self.button_B.grid(row=1, column=0)
        self.button_Y.grid(row=1, column=1)

        self.button_R['activebackground'] = self.button_R.cget('background')
        self.button_G['activebackground'] = self.button_G.cget('background')
        self.button_B['activebackground'] = self.button_B.cget('background')
        self.button_Y['activebackground'] = self.button_Y.cget('background')

        self.button_R.bind('<Button-1>', self.userClickedButton)
        self.button_G.bind('<Button-1>', self.userClickedButton)
        self.button_B.bind('<Button-1>', self.userClickedButton)
        self.button_Y.bind('<Button-1>', self.userClickedButton)

    def randomClick(self):
        self.randomColor = random.choice('RYGB')
        return self.randomColor

    def randomLevelSeq(self):     
        self.randomList = []  
        for i in range(self.level):
            self.randomList.append(self.randomClick())
        #print('Seq to remember: ', randomList)
        return self.randomList


    def simulation(self):
        
        randomColorList = self.randomLevelSeq()
        print(randomColorList)
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

x = ButtonFramme(root)

ans = input('Ska jag visa spel planet?: ')
if ans == 'y':
    x.showFrame(True)
    '''
    time.sleep(3)
    print("nu börjar vi om 2 sek!")
    time.sleep(2)
    x.simulation()
    ans2 = input('Ska jag byta level och simulera?: ')
    if ans2 == 'y':
        x.changeLevel(5)
        x.simulation()
'''

root.mainloop()
