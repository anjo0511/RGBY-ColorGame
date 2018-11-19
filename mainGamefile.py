#
from tkinter import *
import tkinter.messagebox
import random
import time
from scoreSheetClass import ScoreSheetClass


class MainApplicationLayout():

    def __init__(self,root,scoreSheetName):
        ''' 
            Syfte: -
            Returvärde: -
            Kommentarer: -
        '''    
        self.userColorSequenceList=[]   
        self.level = 5 
        self.scoreSheet = scoreSheetName
        self.root = root
        self.rootWindow()       
        self.baseFrames()
        self.baseLabels()
        self.baseButtons()
        self.submitScoreFrame() #erase when done fixin to be called when nececary

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


    def baseFrames(self):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        '''                
        self.frame1 = Frame(self.root,bd=2,relief='solid',height=100, width=600, pady=20,padx=200)
        self.frame2 = Frame(self.root,bd=2,relief='solid',height=150, width=200)
        self.frame1.pack()
        self.frame2.pack()


    def baseButtons(self):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        '''
        self.button_R = Button(self.frame2,text='R',bg='red',height=4, width=8,bd=7,relief='raised')
        self.button_G = Button(self.frame2,text='G',bg='green',height=4, width=8,bd=7,relief='raised')
        self.button_B = Button(self.frame2,text='B',bg='blue',height=4, width=8,bd=7,relief='raised')
        self.button_Y = Button(self.frame2,text='Y',bg='yellow',height=4, width=8,bd=7,relief='raised')

        self.button_R.grid(row=0,column=0)
        self.button_G.grid(row=0,column=1)
        self.button_B.grid(row=1,column=0)
        self.button_Y.grid(row=1,column=1)

        self.button_R['activebackground']=self.button_R.cget('background')
        self.button_G['activebackground']=self.button_G.cget('background')
        self.button_B['activebackground']=self.button_B.cget('background')
        self.button_Y['activebackground']=self.button_Y.cget('background')

        self.button_R.bind('<Button-1>', self.userClickedButton)
        self.button_G.bind('<Button-1>', self.userClickedButton)
        self.button_B.bind('<Button-1>', self.userClickedButton)
        self.button_Y.bind('<Button-1>', self.userClickedButton)


    def userClickedButton(self,event):    
        #event.widget.bell(displayof=0)
        self.colorPressed = event.widget.cget('text')
        self.userColorList(self.colorPressed)


    def userColorList(self,colorPressed):
        #self.userColorSequenceList=[]    

        if len(self.userColorSequenceList) < self.level:
            self.userColorSequenceList.append(colorPressed)
            print(self.userColorSequenceList)

        if len(self.userColorSequenceList) == self.level:
            print('Seq user pressed: ', self.userColorSequenceList)
        return self.userColorSequenceList


    def baseLabels(self):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        '''
        level_Label = Label(self.frame1,text='Level: 1', font= 'Times 18')
        lives_Label = Label(self.frame1,text='Lives: 3',font= 'Times 18')
        level_Label.pack()
        lives_Label.pack()


    def submitScoreFrame(self):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        '''
        self.frame3 = Frame(self.root,bd=4,relief='solid',height=180, width=250)
        self.frame3.pack()

        
        nameLabel = Label(self.frame3,text='Name: ',font='Times 12 bold') 
        self.label_meassage=Label(self.frame3,bd=1,font='Times 11 bold',padx=10,pady=5,bg='red')

        self.entry1 = Entry(self.frame3)

        spacer1 = Label(self.frame3,bg='red')
        infoLabel = Label(self.frame3,pady=4,text='Submit highscore',font='Times 12 bold')

        
        button1 = Button(self.frame3,font='Times 12 bold',text='Submit',bg='red',bd=7,relief='raised',command = self.storeHighScore)
       
               
        infoLabel.grid(row=0, columnspan=2)
        nameLabel.grid(row=1, column=0)
        self.entry1.grid(row=1, column=1)
        spacer1.grid(row=2, columnspan=2)
        button1.grid(row=3, columnspan=2)
        self.label_meassage.grid(row=4, columnspan=2)


    def storeHighScore(self):
        ''' 
            Syfte: 
            Returvärde: 
            Kommentarer: 
        '''        
        if not self.entry1.get() == '':
            ###This random seq needs to be removed to allow users to enter their scores
            self.random_score = random.randint(100,2682)
            print(self.entry1.get(),self.random_score)
            
            ScoreSheetClass(self.scoreSheet).scoreWrite(self.entry1.get(),self.random_score)
            ScoreSheetClass(self.scoreSheet).printScoreSheet()

            self.entry1.get()
            self.entry1.delete(0, 'end')

            self.label_meassage['text']= 'Thanks '
            self.label_meassage.after(700, lambda: self.label_meassage.config(text=''))
            self.frame3.after(600, lambda: self.frame3.pack_forget())
           
        else:
            self.label_meassage['text']= 'Submit a name'
            self.label_meassage.after(1000, lambda: self.label_meassage.config(text=''))
            print('Submit a name')
            
        
    def meassageBox(self,txtTitle,txtstring):
        """
            Syfte: 
            Returvärde: 
            Kommentarer: 
        """
        tkinter.messagebox.showinfo(txtTitle,txtstring)


    def questionBox(self,txtTitle,txtstring):
        """
            Syfte: 
            Returvärde: 'yes' or 'no' text string
            Kommentarer: 
        """
        answer = tkinter.messagebox.askquestion(txtTitle,txtstring)
        return answer


class ComputerSimulation():

    def computerRandomClick(self):
        self.computerRandomClick = random.choice('RYGB')
        return self.computerRandomClick

    def gameLevelcomputerSequence(self,level):
        self.computerRandomClickList = []
        for i in range(level):
            self.computerRandomClickList.append(self.computerRandomClick())
        #print('Seq to remember: ', computerRandomClickList)
        return self.computerRandomClickList

'''
class userGameplay():
    
    def __init__(self):
        
        self.self.userColorSequenceList=[]
        self.level= level
    
    def userColorList(self,colorPressed):    

        if len(self.self.userColorSequenceList) < self.level:
            self.self.userColorSequenceList.append(colorPressed)
            print(self.self.userColorSequenceList)

            
            checkIfClickIsCorrect(colorPressed)
            
         
        if len(self.self.userColorSequenceList) == self.level:
            print('Seq user pressed: ', self.self.userColorSequenceList)

        return self.self.userColorSequenceList

    def userClickedButton(self,event):    
        #event.widget.bell(displayof=0)
        self.colorPressed = event.widget.cget('text')
        self.userColorList(self.colorPressed)
   '             
'''
class gameGame(MainApplicationLayout):

    def __init__(self,root,scoreSheetName):
        super().__init__(root,scoreSheetName)

    def __repr__(self):
        pass

    def __str__(self):
        pass    

        '''
            x = gameLevelcomputerSequence(level)
            print('Seq to remember: ', x)
            
            passedLevelBol = True    
            

        def checkIfClickIsCorrect(colorPressed):
            computerSeq = x.pop(0)
            if colorPressed == computerSeq:
                passedLevelBol = True
                print('Correct')
                return passedLevelBol

            else:
                passedLevelBol = False
                print('Wrong')
                return passedLevelBol
                
        def restartGame():

            if passedLevelBol is False:
                meassageBox('Restart','Click okej to start the countdown')
                self.self.userColorSequenceList=[]
                x = gameLevelcomputerSequence(level)
                print(x)
                return self.self.userColorSequenceList,x
        '''


'''
root = Tk()


gameGame(root,'top10scoreSheet')

root.mainloop() 
'''