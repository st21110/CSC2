#Date: 3/5/22
#Author: Prisha

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Deck Planner")

#Entrys
length_input=ttk.Entry(root,width=20)
width_input=ttk.Entry(root,width=20)
height_input=ttk.Entry(root,width=20)

#Calculations
def calculate():
    length = float(length_input.get())
    width = float(width_input.get())
    height = float(height_input.get())

    area = length * width
    post_num = (length+1)*width
    if height <=1:
        post_len = 1.8
    else:
        post_len = 2.4
    cementbag = post_num
    bearers = area * 2
    joists = area/0.4
    decking = area*11

    #Labels and placements for calculation output _c means calculation

    area_label=ttk.Label(root,text="Area: ").grid(row=4,column=0)
    area_c=ttk.Label(root, text=area).grid(row=4,column=1)

    posts_label=ttk.Label(root,text="Post: ").grid(row=5,column=0)
    post_c=ttk.Label(root,text=post_num).grid(row=5,column=1)

    postlen_label=ttk.Label(root,text="Post Length: ").grid(row=6,column=0)
    postlen_c=ttk.Label(root,text=post_len).grid(row=6,column=1)

    cementbag_label=ttk.Label(root,text="Cement Bags: ").grid(row=7,column=0)
    cement_c=ttk.Label(root,text=cementbag).grid(row=7,column=1)

    bearers_label=ttk.Label(root,text="Bearers: ").grid(row=8,column=0)
    bearers_c=ttk.Label(root,text=bearers).grid(row=8,column=1)

    joists_label=ttk.Label(root,text="Joists: ").grid(row=9,column=0)
    joists_c=ttk.Label(root,text=joists).grid(row=9,column=1)

    decking_label=ttk.Label(root,text="Decking: ").grid(row=10,column=0)
    decking_c=ttk.Label(root,text=decking).grid(row=10,column=1)

#Exit command
def quit():
    exit()

#Labels
length_label=ttk.Label(root,text="Length")
width_label=ttk.Label(root,text="Width")
height_label=ttk.Label(root,text="Height")

#Buttons and placements
calculation = ttk.Button(root,text="Calculate",command=calculate).grid(row=0,column=1)
quit = ttk.Button(root,text="Quit",command=quit).grid(row=0,column=0)

#Placement of labels and inputs (.entry)
length_label.grid(row=1,column=0)
width_label.grid(row=2,column=0)
height_label.grid(row=3,column=0)

length_input.grid(row=1,column=1)
width_input.grid(row=2,column=1)
height_input.grid(row=3,column=1)


root.geometry("300x250")
root.mainloop()