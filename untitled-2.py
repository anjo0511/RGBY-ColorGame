from tkinter import *

"""
higscore print out på meassage box!!s

""""

from  tkinter import messagebox
from scoreSheetClass import ScoreSheetClass

x= ScoreSheetClass().getScoreList()
print(x)

redLista = ''
for eachtuple in x:

	var1 , var2 = eachtuple

	avst = 50 - len(var1)
	var2 = str(var2)
	var1 = var1 + ' '*avst
	var2 = 'level: '+var2 + '\n'
	redLista += var1+var2
print(redLista)


root=Tk()
messagebox.showinfo('Top10 higest scores',redLista)

root.mainloop()
