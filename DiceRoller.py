#!/usr/bin/env python3

###
# Wilson Miller 2021
###
import random
import tkinter as tk
import sys


# Evaluate the dice roll
def evaluate(event):
    dice = int(numberDice.get())
    lst = []

    for x in range(dice):
        roll = random.randint(1, int(sideDice.get()))
        print("Roll #" + str(x + 1) + " value is: " + str(roll))  # debug print to console
        lst.append(roll)
    print("Sum of rolls: " + str(sum(lst)) + "\n")  # debug print to console
    displayTotal.configure(text="User Rolled: " + str(sum(lst)))
    displayDice.configure(text="Using " + str(dice) + " dice")


def output_file():
    original_stdout = sys.stdout
    with open('output.txt', "a") as f:
        sys.stdout = f
        print("Sum of rolls: " + str(sum(lst)) + "\n")
        sys.stdout = original_stdout


# Quit the game
def exit_program(event):
    exit()


# Set up GUI
master = tk.Tk()
master.geometry('500x500')
master.title("Dice Roll Simulation")

tk.Label(master, text="Dice Roll Simulation\n Created by: Wilson Miller\n January 2021").pack()
# Input for user for how many sides per die they want
tk.Label(master, text="Number of Sides to the Dice").pack()
sideDice = tk.Entry(master)
sideDice.bind("<Return>", evaluate)
sideDice.pack()
# Input for user for how many dice they wish to roll
tk.Label(master, text="Number of Dice").pack()
numberDice = tk.Entry(master)
numberDice.bind("<Return>", evaluate)
numberDice.insert(1, 1)
numberDice.pack()
# Roll button
rollProgram = tk.Button(master, text='Roll Dice')
rollProgram.bind("<Button-1>", evaluate)
rollProgram.pack()
# Display numberDice and total (lst)
displayTotal = tk.Label(master)
displayTotal.pack()
displayDice = tk.Label(master)
displayDice.pack()

# Button click for user to exit game
exitProgram = tk.Button(master, text='Quit')
exitProgram.bind("<Button-1>", exit_program)
exitProgram.pack()
# Checkbox to enable storing output to filename ~~~~ Not finished
c1 = tk.Checkbutton(master, text='Output to File?')
c1.pack()

master.mainloop()
