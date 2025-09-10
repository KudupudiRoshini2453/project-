class Node:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.num_of_children = 0
        self.children = []

def dfs(nodes, quality, current_node_index):
    current_node = nodes[current_node_index]
    #print(current_node_index)
    if current_node.num_of_children == 0:
        quality[current_node_index] = current_node.x * current_node.x + current_node.y * current_node.y
        return

    max_quality = -1
    for child_index in current_node.children:
        dfs(nodes, quality, child_index)
        max_quality = max(max_quality, quality[child_index])
       # print(max_quality)
    for child_index in current_node.children:
        child_node = nodes[child_index]
        #print(child_index)
        if quality[child_index] == max_quality:
            current_node.x += child_node.x
            current_node.y += child_node.y
        else:
            current_node.x -= child_node.x
            current_node.y -= child_node.y

    quality[current_node_index] = current_node.x * current_node.x + current_node.y * current_node.y

def process_input(input_string):
    input_lines = input_string.strip().split("\n")
    num_of_nodes = int(input_lines[0])
    nodes = [Node() for _ in range(num_of_nodes + 1)]
    quality = [0 for _ in range(num_of_nodes + 1)]

    for i in range(1, num_of_nodes + 1):
        node_data = list(map(int, input_lines[i].split()))
        nodes[i].num_of_children = node_data[0]
        if nodes[i].num_of_children == 0:
            nodes[i].x = node_data[1]
            nodes[i].y = node_data[2]
        else:
            nodes[i].children = node_data[1:]

    dfs(nodes, quality, 1)
    print(quality[1])

input_string = """
8
3 4 2 5
2 3 8
0 -3 9
0 -5 -7
2 6 7
0 1 4
0 -3 -1
0 1 4"""
process_input(input_string)

input_string_1 = """
4
3 2 3 4
0 10 1
0 3 6
0 2 7"""
process_input(input_string_1) 

#start of the gui
# creation of the window
from tkinter import*
import tkinter as tk
from pygame import mixer
mixer.init()
  

win = Tk()
win.title("Take on meme")  

win.geometry( "1000x600" )
#1st input no of nodes
canvas1 = tk.Canvas(win, width=1000, height=600)
canvas1.configure(bg='light cyan')
canvas1.pack()
label= Label( win , text = "Enter the number of nodes",font=('times',15,'bold') )
label.config(bg="pink",fg="black")
label.pack()
canvas1.create_window(200,40,window=label)
data_nodes1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(200,80,window=data_nodes1)

#2nd input no of nodes
label2 = Label( win , text = "Enter the number of nodes",font=('Times',15,'bold'))
label2.pack()
label2.config(bg="pink",fg="black")
canvas1.create_window(600,40,window=label2)
data_nodes2=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(600,80,window=data_nodes2)
#the 1st input
# the drop boxes 
def show():
   label.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop = OptionMenu( win , clicked , *options )
drop.config(bg="LIGHT PINK",fg="BLACK")
drop.pack()
def show():
   label.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop1 = OptionMenu( win , clicked , *options )
drop1.config(bg="light pink",fg="black")
drop1.pack()
def show():
   label.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop2 = OptionMenu( win , clicked , *options )
drop2.config(bg="light pink",fg="black")
drop2.pack()
def show():
   label.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop3 = OptionMenu( win , clicked , *options )
drop3.config(bg="light pink",fg="black")
#the second input
#drop down boxes
def show():
   label2.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop4 = OptionMenu( win , clicked , *options )
drop4.config(bg="LIGHT PINK",fg="BLACK")
#2
def show():
   label2.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop5= OptionMenu( win , clicked , *options )
drop5.config(bg="LIGHT PINK",fg="BLACK")
# 3
def show():
   label2.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop6= OptionMenu( win , clicked , *options )
drop6.config(bg="LIGHT PINK",fg='BLACK')
#4
def show():
   label2.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop7= OptionMenu( win , clicked , *options )
drop7.config(bg='LIGHT PINK',fg='BLACK')
#5
def show():
   label2.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop8 = OptionMenu( win , clicked , *options )
drop8.config(bg="LIGHT PINK",fg="BLACK")
#6
def show():
   label2.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop9 = OptionMenu( win , clicked , *options )
drop9.config(bg="LIGHT PINK",fg="black")
#7
def show():
   label2.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop10 = OptionMenu( win , clicked , *options )
drop10.config(bg="LIGHT PINK",fg="black")
# 8
def show():
   label2.config( text = clicked.get() )
  

options = [
   "Simple node","Complex node"]
clicked = StringVar()

drop11= OptionMenu( win , clicked , *options )
drop11.config(bg="LIGHT PINK",fg="BLACK")
#1st input
# entry boxes with drop down boxes
drop3.pack()
canvas1.create_window(320,130,window=drop2)
data_values=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(200,130,window=data_values)
canvas1.create_window(320,220,window=drop1)
data_values1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(200,220,window=data_values1)
canvas1.create_window(320,320,window=drop3)
data_values1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(200,320,window=data_values1)
canvas1.create_window(320,420,window=drop)
data_values1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(200,420,window=data_values1)

# 2nd input entry boxes with drop boxes

data_values=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(600,130,window=data_values)
canvas1.create_window(720,130,window=drop5)
data_values1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(600,180,window=data_values1)
canvas1.create_window(720,180,window=drop6)
data_values1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(600,230,window=data_values1)
canvas1.create_window(720,230,window=drop7)
data_values1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(600,280,window=data_values1)
canvas1.create_window(720,280,window=drop8)
data_values=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(600,320,window=data_values)
canvas1.create_window(720,320,window=drop9)
data_values1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(600,370,window=data_values1)
canvas1.create_window(720,370,window=drop10)
data_values1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(600,420,window=data_values1)
canvas1.create_window(720,420,window=drop11)
data_values1=tk.Entry(win,font=('Times',10,'normal'))
canvas1.create_window(600,470,window=data_values1)
canvas1.create_window(720,470,window=drop4)
# to open a new window 
#1st input
def open_new_window():
    new_window = tk.Toplevel(win)  # Create a new Toplevel window
    new_window.title("Tournament Tree")  # Set the title for the new window
    new_window.geometry('600x600')
    new_window.configure(bg='black')
    numbers = [
    ["",169,"" ],
    [101, 45, 53]
]

    for i in range(2):
        for j in range(3):
            for i in range(len(numbers)):
               for j in range(len(numbers[i])):
                 label = tk.Label(new_window,text=str(numbers[i][j]),font='Times',padx=60, pady=60, relief=tk.RIDGE) 
                 if str(numbers[i][j])=="169":
                    label.config(bg= "yellow", fg= "black")
                 elif str(numbers[i][j])=="101":
                    label.config(bg= "white", fg= "black")
                 elif str(numbers[i][j])=="45":
                    label.config(bg= "white", fg= "black")
                 elif str(numbers[i][j])=="53":
                    label.config(bg= "white", fg= "black")
                 elif str(numbers[i][j])=="|":
                    label.config(bg= "black", fg= "white",font=("times",30,"bold"))
               #  elif str(numbers[i][j])=="->" | str(numbers[i][j])=="<-":
                 #   label.config(bg= "black", fg= "white",font=("times",30,"bold"))
                 else:
                    label.config(bg= "black", fg= "black") 
                 label.grid(row=i, column=j)
     
     # the champion button creation
    def input_box():
        label1=tk.Label(new_window,text="169")
        label1.place(x=290,y=530)
        mixer.music.load('tada fanfare a.mp3')
        mixer.music.set_volume(10)
        mixer.music.play()


    button1=tk.Button(new_window,text="Champion meme",command=input_box)
    button1.place(x=250,y=500)

# 2nd input
def open_new_window1():
    new_window = tk.Toplevel(win)  # Create a new Toplevel window
    new_window.title("Tournament Tree")  # Set the title for the new window
    new_window.geometry('600x400')
    new_window.configure(bg='black')
    numbers = [
    ["","","",314,"","","" ],
    [74 ,"",41,"","",41,""],
    ["",90,"",17,17,"",10]
]

    for i in range(3):
        for j in range(7):
            for i in range(len(numbers)):
               for j in range(len(numbers[i])):
                 label = tk.Label(new_window,text=str(numbers[i][j]),font='Times',padx=20, pady=20, relief=tk.RIDGE) 
                 if str(numbers[i][j])=="314":
                    label.config(bg= "yellow", fg= "black")
                 elif str(numbers[i][j])=="74":  
                    label.config(bg= "white", fg= "black")
                 elif (i,j)==(1,2):  
                    label.config(bg= "pink", fg= "black")
                 elif (i,j)==(2,3):  
                    label.config(bg= "pink", fg= "black")
                 elif (i,j)==(1,5):  
                    label.config(bg= "cyan", fg= "black")
                 elif str(numbers[i][j])=="10":  
                    label.config(bg= "cyan", fg= "black")
                 elif (i,j)==(2,4):  
                    label.config(bg= "cyan", fg= "black")
                 elif str(numbers[i][j])=="90":  
                    label.config(bg= "pink", fg= "black")
                 else:
                    label.config(bg= "black", fg= "black")
                 label.grid(row=i, column=j)
    # the champion button creation
    def input_box():
        label1=tk.Label(new_window,text="314")
        label1.place(x=290,y=350)
        mixer.music.load('tada fanfare a.mp3')
        mixer.music.set_volume(10)
        mixer.music.play()
    button1=tk.Button(new_window,text="Champion meme",command=input_box)
    button1.place(x=250,y=320)

# the touranment button creation
# 1st input button
button = tk.Button(win, text="The tournament tree", command=open_new_window)
button.pack(pady=10)
button.config(bg='pink',fg='black')
canvas1.create_window(200,500,window=button)
# 2nd input button
button1 = tk.Button(win, text="The tournament tree", command=open_new_window1)
button1.pack(pady=10)  
button1.config(bg='pink',fg='black')
canvas1.create_window(600,550,window=button1)


win.mainloop()
