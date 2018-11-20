
from tkinter import *


class ButtonFramme:

    def __init__(self, root):
        self.level = 5
        self.root = root
        self.buttonFrame = Frame(
            self.root, bd=2, relief='solid', height=150, width=200)
        self.baseButtons()

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
        print(self.lvlList)
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
        button_R = Button(self.buttonFrame, text='R', bg='red',
                          height=4, width=8, bd=7, relief='raised')
        button_G = Button(self.buttonFrame, text='G', bg='green',
                          height=4, width=8, bd=7, relief='raised')
        button_B = Button(self.buttonFrame, text='B', bg='blue',
                          height=4, width=8, bd=7, relief='raised')
        button_Y = Button(self.buttonFrame, text='Y', bg='yellow',
                          height=4, width=8, bd=7, relief='raised')

        button_R.grid(row=0, column=0)
        button_G.grid(row=0, column=1)
        button_B.grid(row=1, column=0)
        button_Y.grid(row=1, column=1)

        button_R['activebackground'] = button_R.cget('background')
        button_G['activebackground'] = button_G.cget('background')
        button_B['activebackground'] = button_B.cget('background')
        button_Y['activebackground'] = button_Y.cget('background')

        button_R.bind('<Button-1>', self.userClickedButton)
        button_G.bind('<Button-1>', self.userClickedButton)
        button_B.bind('<Button-1>', self.userClickedButton)
        button_Y.bind('<Button-1>', self.userClickedButton)



root = Tk()

x = ButtonFramme(root)

ans = input('Ska jag visa spel planet?: ')
if ans == 'y':
    x.showFrame(True)
    ans2 = input('Ska jag ta bort den nu?: ')
    if ans2 == 'y':
        x.showFrame(False)


root.mainloop()
