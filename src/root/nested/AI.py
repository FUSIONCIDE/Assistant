'''
Created on Jan 9, 2018

@author: FUSIONCIDE
'''

import os
import active_window as aw

print(aw.isRunning)
inputSentence = ""
inputSentence = input("Type here:\n")


def the_func():
    if inputSentence in ("hey john", "john", "hey joe", "joe", "ok joe", "ok john"):
        #aw.openWindow()
        print("Hi!")
        
        
        
        input1 = input("what u want:\n")
        split1 = input1.split(' ', 1)
        #Assign each word to its own variable? How to run command say: open stick fight
        #get first word (open), if it is open, delete it from string, then run whatever is left behind,
        #but what if there are more commands such as: open chrome AND go to google.com?
        print(input1)
        if split1[0] == "open":
            file1 = input1.split(' ', 1)[1]
            #file1 = split1[1]
            if file1 == "stick fight":#2 words
                os.startfile('"steam://rungameid/674940"')
            elif file1 == "speedrunners":#1 word
                os.startfile('"steam://rungameid/207140"')
            else:
                print("Not yet available")
            #search C:\ProgramData\Microsoft\Windows\Start Menu for a file to open (.lnk) but what is command given
            # is: open a.txt (so how to quickly search all directories, starting with desktop, then downloads, etc.,
            # for each file?)
                
                
                
                
        elif input1 in ("open"): #if written open and then something, open that something:
        
            "C:\ProgramData\Microsoft\Windows\Start Menu"#search this directory for shortcuts but ONLY OR WINDOWS
        elif input1 in ("exit", "quit", "stop", "bye", "ok", "ok bye", "ok bye papi", "ok bye pap",
                                  "bye pap", "bye papi", "cya"):
            print("Ok bye!")
        else:
            print("Invalid input! Please try again.\n")
            the_func()
            
            
the_func()
