'''
Created on Jan 27, 2018

@author: FUSIONCIDE
'''
import os
import random as rand
import base_file as bf


def remember_command(self):
  split1 = self.split('remember ')
  #create new var everytime asked to remember something, store the name and the thing (like a number)
  bf.io[0] = 0#????
  

def open_command(self):
    file1 = self[5:]  #delete open from string
    if file1 == "stick fight":  #2 words
        os.startfile('"steam://rungameid/674940"')
        bf.io[0] = 0#????
    elif file1 == "speedrunners":  #1 word
        os.startfile('"steam://rungameid/207140"')
        bf.io[0] = 0#????
    else:
        print("Not yet available")
        print(file1)

    
def and_command(self):
    #split it from one side of "and" and the other side (testing for multi-command)
    input2 = self.split(" and ")
    for k in input2:
        print(k)
    bf.io[0] = 0#????
     
            
def what_command(self):
    file1 = self[5:]
    print(file1)
    bf.io[0] = 0#????
    return bf.io#????


def play_command(self):
    file1 = self[5:]
    print("play things")
    bf.io[0] = 0#????
    

def timer_command():
    time = int(input("For how long? (seconds): "))
    time *= 1000  #seonds?
    while time != 0:
        print(time)
        time -= 1
        if time == 0:
            print("Timer over!")
            
def stopwatch_command(): #no worko
    stopp = 0
    while stopp == 0:
        time=0
        time = time + 1
        print(time)
        time += 1

#FUNCITONING THINGS
def bye_command():
    int1 = rand.randint(0, 1)
    if int1 == 0:
        print("Ok bye!")
    else:
        print("Bye!")


def hi():
    int1 = rand.randint(0, 3)
    if int1==0:
        print("Hi!")
    elif int1==1:
        print("Hey! How can I help?")
    elif int1==2:
        print("Hi, how can I help?")
    elif int1==3:
        print("Hi, how can I assist you?")


def thank_command():
    int1 = rand.randint(0, 1)
    if int1 == 0:
        print("Your welcome")
    else:
        print("No problem")