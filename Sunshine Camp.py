#Date: 10/05/22
#Author: Prisha

from tkinter import *

root = Tk()
root.title("Sunshine Adventure Camp")

#Quit Fuctions
def quit():
    exit()


#Entrys
groupleader = Entry(root,width=20)
numcampers = Entry(root,width=20)
weathercon = Entry(root,width=20)
location = Entry(root,width=20)
rows = Entry(root,width=20)

#Print Function 
def printdetail():
    groupleader_c = (groupleader.get())
    numcampers_c = (numcampers.get())
    weathercon_c = (weathercon.get())
    location_c = (location.get())

    Label(root,text="Row",font="bold").grid(row=8,column=1)
    Label(root,text="Group Leader",font="bold").grid(row=8,column=2)
    Label(root,text="No. of campers",font="bold").grid(row=8,column=3)
    Label(root,text="Weather",font="bold").grid(row=8,column=4)
    Label(root,text="Location",font="bold").grid(row=8,column=5)

    Label(root,text=groupleader_c).grid(row=9,column=2)
    Label(root,text=numcampers_c).grid(row=9,column=3)
    Label(root,text=weathercon_c).grid(row=9,column=4)
    Label(root,text=location_c).grid(row=9,column=5)




#Labels
Label(root,text="Group Leader").grid(row=2,column=1)
Label(root,text="Number of Campers").grid(row=3,column=1)
Label(root,text="Weather").grid(row=4,column=1)
Label(root,text="Location").grid(row=5,column=1)
Label(root,text="Row#").grid(row=6,column=1)

#Buttons
Button(root,text="Append")
Button(root,text="Print Details",command=printdetail).grid(row=7,column=1)
Button(root,text="Delete")
Button(root,text="Quit",command=quit).grid(row=1,column=1)

groupleader.grid(row=2,column=2)
numcampers.grid(row=3,column=2)
weathercon.grid(row=4,column=2)
location.grid(row=5,column=2)
rows.grid(row=6,column=2)

root.mainloop()