
from tkinter import * 
import tkinter.messagebox
import time

'''
Här ger vi en lista till knapparna som sedan flashar beroende på sekvensen
'''

buttonList = ['Button 1','Button 1','Button 2','Button 1','Button 2']

def button2_click(buttonList):

    userinput = input('color? ')
    if userinput != '':
        time.sleep(1)
        for eachColor in buttonList:
            print(eachColor)
            
            if eachColor == 'Button 1':

                button1['activebackground']='white'
                button1.flash()
                button1.after(2000, lambda:button1.configure(activebackground ='red'))             


            elif eachColor == 'Button 2':

                button2['activebackground']='white'
                button2.flash()
                button2.after(2000, lambda:button2.configure(activebackground ='green'))
            
            time.sleep(0.7)



root = Tk()
root.geometry('400x200+500+500')

button1 = Button(text="Button 1",bg='red',activebackground='red',height=5)
button2 = Button(root,text="Button 2",bg='green',activebackground='green',height=5)

button1.pack()
button2.pack(side=BOTTOM)


button2_click(buttonList)
root.mainloop()

