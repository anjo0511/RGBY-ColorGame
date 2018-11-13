from tkinter import *
import tkinter.messagebox


def mainWindow():
    root.title('RGBY-ColorGame 1.0')
    root.resizable(width=False, height=False)
    width_of_window = 600
    height_of_window = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate =(screen_width/2-width_of_window/2)
    y_coordinate = (screen_height/2-height_of_window/2)
    root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate)) 

def BottonSumulation():
    answe = input('what botton?: ')
    if answe == 'R':         
        button_R.flash()   


def flashClickedButton(event):
    #event.widget.bell(displayof=0)
    s= event.widget.cget('text')
    
    if s == 'R':
        button_R.config(bg='white')
        button_R.after(100, lambda: button_R.config(bg='red'))
    elif s == 'G':
        button_G.config(bg='white')
        button_G.after(100, lambda: button_G.config(bg='green'))
    elif s == 'B':
        button_B.config(bg='white')
        button_B.after(100, lambda: button_B.config(bg='blue'))
    elif s == 'Y':
        button_Y.config(bg='white')
        button_Y.after(100, lambda: button_Y.config(bg='yellow'))


root = Tk()
mainWindow()

frame1 = Frame(root,bd=2,relief='solid',height=100, width=600, pady=20,padx=200)
frame2 = Frame(root,bd=2,relief='solid',height=150, width=200)

level_Label = Label(frame1,text='Level: 1', font= 'Times 18')
lives_Label = Label(frame1,text='Lives: 3',font= 'Times 18')

frame1.pack()
frame2.pack()
level_Label.pack()
lives_Label.pack()

button_R = Button(frame2,bg='red',height=4, width=8,bd=7,relief='raised')
button_G = Button(frame2,bg='green',height=4, width=8,bd=7,relief='raised')
button_B = Button(frame2,bg='blue',height=4, width=8,bd=7,relief='raised')
button_Y = Button(frame2,bg='yellow',height=4, width=8,bd=7,relief='raised')


button_R['text']='R'
button_G['text']='G'
button_B['text']='B'
button_Y['text']='Y'


button_R.grid(row=0,column=0)
button_G.grid(row=0,column=1)
button_B.grid(row=1,column=0)
button_Y.grid(row=1,column=1)

button_R['activebackground']=button_R.cget('background')
button_G['activebackground']=button_G.cget('background')
button_B['activebackground']=button_B.cget('background')
button_Y['activebackground']=button_Y.cget('background')

button_R.bind('<Button-1>', flashClickedButton)
button_G.bind('<Button-1>', flashClickedButton)
button_B.bind('<Button-1>', flashClickedButton)
button_Y.bind('<Button-1>', flashClickedButton)


root.mainloop() 