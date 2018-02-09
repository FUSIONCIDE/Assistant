'''
Created on Jan 9, 2018

@author: FUSIONCIDE
'''

import active_window as aw
import base_commands as bc

#So apparently there is an error that it cannot seem to be able to import the file as said above
#No idea why but if it works this code could be so much cleaner
#FIXED, so python runs the module when importing, since i was importing a file importing it, python no like
#use if __name__ == "__main__" to trick python


io=[5]


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
        io[0] = 0 #Either use a list or global variable
        
    elif inputCommand in ("thank you", "thanks"):
        bc.thank_command()  #Command to say thanks
        io[0] = 0
        
    else:
        print("I'm sorry, I didn't get that. Please try again.\n")


if __name__ == "__main__":#Make sure that runs this file only
    
    print(aw.isRunning)
    inputSentence = (input("Enter: ")).lower()

    if inputSentence in ("hey john", "john", "hey joe", "joe", "ok joe", "ok john"):
        bc.hi()
        print('''\nCommands Available:
OPEN (stick fight, speedrunners)
exit, quit, stop, bye, ok, ok bye, ok bye joe, ok bye john, bye joe, bye john, cya
thank you, thanks
and\n''')

        while io[0] != 0:
            the_func()
            #io[0]-=1 #like a counter, but i want timed cant do with input