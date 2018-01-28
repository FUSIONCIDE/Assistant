'''
Created on Jan 9, 2018

@author: FUSIONCIDE
'''

import active_window as aw
import base_commands as bc

#So apparently there is an error that it cannot seem to be able to import the file as said above
#No idea why but if it works this code could be so much cleaner

print(aw.isRunning)
inputSentence = (input("")).lower()


def the_func():
        #aw.openWindow()
        inputCommand = (input("What would you like?:")).lower()
        split1 = inputCommand.split(' ', 1)
        
        if "and" in inputCommand:
            bc.and_command(inputCommand)#If it is a command with two commands
        
        if split1[0] == "open":
            bc.open_command(inputCommand)#Command to open
        
        elif "what" in inputCommand:
            bc.what_command(inputCommand)#Command to search online
       
        elif "play" in inputCommand:
            bc.play_command()#Command to play something
        
        elif inputCommand in ("exit", "quit", "stop", "bye", "ok", "ok bye", "ok bye john", "ok bye joe",
                        "bye joe", "bye john", "cya"): #Is there an easier way to do this?
            bc.bye_command()#Command to exit
        
        elif inputCommand in ("thank you", "thanks"):
            bc.thank_command()#Command to say thanks
            
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

