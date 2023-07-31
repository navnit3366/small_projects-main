#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:53:52 2022

@author: cristian
"""
from tkinter import messagebox
import turtle as t
from random import choice
from mysay import print_say
from mysr import voice_to_text

t.setup(600,600,10,70)
t.tracer(False)
t.bgcolor("lightgreen")
t.hideturtle()
t.title("Tic-Tac-Toe")
t.pencolor("white")
#draw the horizontal lines and vertical lines to form a grid
t.pensize(5)
for i in (-100,100):
    t.up()
    t.goto(i,-300)
    t.down()
    t.goto(i,300)
    t.up()
    t.goto(-300,i)
    t.down()
    t.goto(300,i)
    t.up() 

#create a dict to map cell numbers to cell centre coordinates
cellcenter = {'1':(-200,-200),'2':(0,-200),'3':(200,-200),'4':(-200,0),'5':(0,0),
              '6':(200,0),'7':(-200,200),'8':(0,200),'9':(200,200)}
for cell, center in list(cellcenter.items()):
    t.pencolor("black")
    t.goto(center)
    t.write(cell,font=("Arial",20,"normal"))
    
turn = "blue"
rounds = 1
#Create a list of valid moves
validinputs = list(cellcenter.keys())
#Create a dict of moves made by each player
occupied = {"blue":[],'white':[]}
#determine if a player has won the game
def win_game():
    win = False
    if "1" in occupied[turn] and "2" in occupied[turn] and "3" in occupied[turn]:
        win = True
    if "1" in occupied[turn] and "5" in occupied[turn] and "9" in occupied[turn]:
        win = True
    if "3" in occupied[turn] and "5" in occupied[turn] and "7" in occupied[turn]:
        win = True
    if "7" in occupied[turn] and "8" in occupied[turn] and "9" in occupied[turn]:
        win = True
    if "1" in occupied[turn] and "4" in occupied[turn] and "7" in occupied[turn]:
        win = True
    if "2" in occupied[turn] and "5" in occupied[turn] and "8" in occupied[turn]:
        win = True
    if "3" in occupied[turn] and "6" in occupied[turn] and "9" in occupied[turn]:
        win = True
    if "4" in occupied[turn] and "5" in occupied[turn] and "6" in occupied[turn]:
        win = True
    return win
to_replace = {"number":'','cell':'',
              'one':'1', 'two':'2', 'three':'3',
'four':'4', 'for':'4', 'five':'5',
'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
while True:
    print_say(f"Player {turn}, what's your move?")
    inp = voice_to_text()
    print_say(f"You said, {inp}.")
    for x in list(to_replace.keys()):
        inp = inp.replace(x, to_replace[x])
    
    if inp in validinputs:
        t.up()
        t.goto(cellcenter[inp])
        t.dot(180,turn)
        t.update()
        occupied[turn].append(inp)
        validinputs.remove(inp)
        if win_game() == True:
            validinputs = []
            print_say(f"Congrats player {turn}, you won!")
            messagebox.showinfo("End Game", f"Congrats player {turn}, you won!")
            break
        elif rounds == 9:
            print_say("Game over, it's a tie!")
            messagebox.showinfo("Tie Game", "Game over, it's a tie!")
            break
        rounds += 1
        if turn == "blue":
            turn = "white"
        else: 
            turn = "blue"
        
        #Computer makes a random move
        inp = choice(validinputs)
        print_say(f"The computer occupies cell {inp}.")
        t.up()
        t.goto(cellcenter[inp])
        t.dot(180,turn)
        t.update()
        occupied[turn].append(inp)
        validinputs.remove(inp)
        if win_game() == True:
            validinputs = []
            print_say(f"Congrats player {turn}, you won!")
            messagebox.showinfo("End Game", f"Congrats player {turn}, you won!")
            break
        elif rounds == 9:
            print_say("Game over, it's a tie!")
            messagebox.showinfo("Tie Game", "Game over, it's a tie!")
            break
        rounds += 1
        if turn == "blue":
            turn = "white"
        else: 
            turn = "blue"
    else:
        print_say("Sorry, that's an invalid move!")
            
t.done()
try:
    t.bye()
except t.Terminator:
    print("exit Turtle")
    
    
    
    
    
    
    
