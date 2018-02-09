'''
Created on Jan 9, 2018

@author: FUSIONCIDE
'''
from tkinter import *
import active_window as aw
import base_commands as bc

root = Tk()

io = 5


def Enter():
    global text
    text = content.get()
    global outtext
    outtext=""
    if text in ("hey john", "john", "hey joe", "joe", "ok joe", "ok john"):
        outtext="Hi there!"
        h=True
    output.config(text=outtext)

content = StringVar()

root.geometry('500x500')
frameTop = Frame(root, bg="red")
frameTop.pack(side=TOP, fill=X)
frameMiddle = Frame(root, bg="green")
frameMiddle.pack(fill=X)
frameBottom = Frame(root, bg="yellow")
frameBottom.pack(side=BOTTOM, fill=X)


text1 = Label(frameTop, text="Type Here:", font='40', bg="red")
text1.pack(side=LEFT, padx=5, pady=5)
entry1 = Entry(frameTop, textvariable=content, bd=0)
buttonEnter = Button(frameTop, text="Enter", font=35, bd=0, command=Enter)
buttonEnter.pack(side=RIGHT, padx=5, pady=5, ipady=0, ipadx=5)
entry1.pack(side=RIGHT, expand=True, fill=X, ipady=4)


output=Label(frameMiddle, font=100, padx=5, pady=5, bg="green")
output.pack()





def the_func():
    #aw.openWindow()
    inputCommand = (input("What would you like?:")).lower()
    split1 = inputCommand.split(' ', 1)
    
    if "and" in inputCommand:
        bc.and_command(inputCommand)  #If it is a command with two commands
    
    if split1[0] == "open":
        bc.open_command(inputCommand)  #Command to open
    
    elif "what" in inputCommand:
        bc.what_command(inputCommand)  #Command to search online
    
    elif "play" in inputCommand:
        bc.play_command()  #Command to play something
    
    elif inputCommand in ("exit", "quit", "stop", "bye", "ok", "ok bye", "ok bye john", "ok bye joe",
                          "bye joe", "bye john", "cya"):  #Is there an easier way to do this?
        bc.bye_command()  #Command to exit
        io = 0  #Either use a list or global variable
    
    elif inputCommand in ("thank you", "thanks"):
        bc.thank_command()  #Command to say thanks
        io = 0
    
    else:
        print("I'm sorry, I didn't get that. Please try again.\n")
   
    



root.mainloop()
while io != 0:
    the_func()
    io -= 1  #like a counter, but i want timed cant do with input