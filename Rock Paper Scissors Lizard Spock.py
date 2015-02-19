#Rock Paper Scissors Lizard Spock
#Tabor Fessenden

import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

#Assignment
winner = None
rock = 0
Spock = 1
paper = 2
lizard = 3
scissors = 4

messagebox.showinfo("Welcome",
                    "We're going to play Rock, Paper," + \
                    " Scissors, Lizard, Spock! \n " + \
                    "You choose one of the 5 abilities " + \
                    "and go up against this program.")
                    
comp = random.randrange(0,4)
user = simpledialog.askinteger("Choose your ability.",
                               "Enter 0 for rock, 1 for Spock, " +\
                               "2 for paper, 3 for lizard " +\
                               "and 4 for scissors.")
while winner == None:
                    
