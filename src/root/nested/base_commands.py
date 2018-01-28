'''
Created on Jan 27, 2018

@author: FUSIONCIDE
'''
import os
import random as rand
import base_file as ai


def open_command(self):
    file1 = self.split(' ', 1)[1]  #delete open from string
    #file1 = split1[1]
    if file1 == "stick fight":  #2 words
        os.startfile('"steam://rungameid/674940"')
    elif file1 == "speedrunners":  #1 word
        os.startfile('"steam://rungameid/207140"')
    else:
        print("Not yet available")
        ai.the_func()


def thank_command():
    int1 = rand.randint(0, 1)
    if int1 == 0:
        print("Your welcome")
    else:
        print("No problem")
    
    
def and_command(self):
    if "and" in self:
        #split it from one side of "and" and the other side (testing for multi-command)
        input2 = self.split(" and ")
        for k in input2:
            print(k)
     
            
def what_command(self):
    file1 = self.split(' ', 1)[1]
    print(file1)
        

def play_command():
    print("play things")
    

def bye_command():
    int1 = rand.randint(0, 1)
    if int1 == 0:
        print("Ok bye!")
    else:
        print("Bye!")