#!/usr/bin/env python

import os
from tkinter import *
from tkinter.ttk import *
import random
from gtts import gTTS

def Speak(roll):
    global label
    tts = gTTS(text=roll, lang='en')
    tts.save("roll.mp3")
    os.system("mpg123 roll.mp3")

def roll_d2():
    global roll, label
    roll = str(random.randint(1,2))
    Speak(roll)
    label['text'] = roll


def roll_d4():
    global roll, label
    roll = str(random.randint(1,4))
    Speak(roll)
    label['text'] = roll

def roll_d6():
    global roll, label
    roll = str(random.randint(1,6))
    Speak(roll)
    label['text'] = roll

def roll_d8():
    global roll, label
    roll = str(random.randint(1,8))
    Speak(roll)
    label['text'] = roll

def roll_d10():
    global roll, label
    roll = str(random.randint(1,10))
    Speak(roll)
    label['text'] = roll

def roll_d12():
    global roll, label
    roll = str(random.randint(1,12))
    Speak(roll)
    label['text'] = roll

def roll_d20():
    global roll, label
    roll = str(random.randint(1,20))
    Speak(roll)
    label['text'] = roll

def roll_d100():
    global roll, label
    roll = str(random.randint(1,100))
    Speak(roll)
    label['text'] = roll


def main():
    global roll, label
    window = Tk()
    roll = 0 
    label = Label(window, text=roll)
    label.grid(row=1, column=1, ipadx=40, ipady=40)
    
    buttond2 = Button(window, text="d2", command=roll_d2)
    buttond2.grid(row=0, column=0, padx=20, pady=10)

    buttond4 = Button(window, text="d4", command=roll_d4)
    buttond4.grid(row=0, column=1, padx=20, pady=10)

    buttond6 = Button(window, text="d6", command=roll_d6)
    buttond6.grid(row=0, column=2, padx=20, pady=10)

    buttond8 = Button(window, text="d8", command=roll_d8)
    buttond8.grid(row=1, column=0, padx=20, pady=10)

    buttond10 = Button(window, text="d10", command=roll_d10)
    buttond10.grid(row=1, column=2, padx=20, pady=10)

    buttond12 = Button(window, text="d12", command=roll_d12)
    buttond12.grid(row=2, column=0, padx=20, pady=10)

    buttond20 = Button(window, text="d20", command=roll_d20)
    buttond20.grid(row=2, column=1, padx=20, pady=10)

    buttond100 = Button(window, text="d100", command=roll_d100)
    buttond100.grid(row=2, column=2, padx=20, pady=10)

    window.mainloop()

main()
