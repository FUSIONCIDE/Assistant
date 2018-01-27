'''
Created on Jan 9, 2018

@author: FUSIONCIDE
'''

import os
import active_window as aw
import random as rand


print(aw.isRunning)
inputSentence = (input("")).lower()


def the_func():
        #aw.openWindow()
        inputCommand = (input("What would you like?:")).lower()
        split1 = inputCommand.split(' ', 1)
        #Assign each word to its own variable? How to run command say: open stick fight
        #get first word (open), if it is open, delete it from string, then run whatever is left behind,
        #but what if there are more commands such as: open chrome AND go to google.com?
        #search fof and if found then split down middle and evaluate the command
        
        #What if I only wanted to look for key words, what if user typed: hey can you open stick fight. How to get
        #program to run the command disregarding other words?
        
        if "and" in inputCommand:
            #split it from one side of "and" and the other side (testing for multi-command)
            input2 = inputCommand.split(" and ")
            for k in input2:
                print(k)
            
        if split1[0] == "open":
            file1 = inputCommand.split(' ', 1)[1] #delete open from string
            #file1 = split1[1]
            if file1 == "stick fight":#2 words
                os.startfile('"steam://rungameid/674940"')
            elif file1 == "speedrunners":#1 word
                os.startfile('"steam://rungameid/207140"')
            else:
                print("Not yet available")
                the_func()
            #search C:\ProgramData\Microsoft\Windows\Start Menu for a file to open (.lnk) but what is command given
            # is: open ab.bat (so how to quickly search all directories, starting with desktop, then downloads, etc.,
            # for each file?)

            "C:\ProgramData\Microsoft\Windows\Start Menu"  #search this directory for shortcuts but ONLY OR WINDOWS
        
        #Music, Calculate, Search, News, Weather
        elif "what" in inputCommand:
            file1 = inputCommand.split(' ', 1)[1]
            print(file1)
        elif "play" in inputCommand:
            print("play things")
        
        elif inputCommand in ("exit", "quit", "stop", "bye", "ok", "ok bye", "ok bye john", "ok bye joe",
                        "bye joe", "bye john", "cya"): #Is there an easier way to do this?
        
            print("Ok bye!")
        
        #Testing two different outcomes for one input
        elif inputCommand in ("thank you", "thanks"):
            int1 = rand.randint(0, 1)
            if int1 == 0:
                print("Your welcome")
            else:
                print("No problem")
        
        #If all else fails do this (rerun the program)
        else:
            print("Invalid input! Please try again.\n")
            the_func()


#Start off the program, down here because I don't want print("Hi!") to print every time there is an invalid input
if inputSentence in ("hey john", "john", "hey joe", "joe", "ok joe", "ok john"):
    print("Hi!")
    print('''\nCommands Available:
OPEN (stick fight, speedrunners)
exit, quit, stop, bye, ok, ok bye, ok bye joe, ok bye john, bye joe, bye john, cya
thank you, thanks
and\n''')
    the_func()

