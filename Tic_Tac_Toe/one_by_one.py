#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:53:52 2022

@author: cristian
"""
from tkinter import messagebox
import turtle as t

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

def mark_cell(x,y):
    global turn, rounds, validinputs
    if -300<x<300 and -300<y<300:
        col = int((x+500)//200)
        row = int((y+500)//200)
        cellnumber = str(col+(row-1)*3)
    else:
        print("You clicked outside the game board")
        
    if cellnumber in validinputs:
        t.up()
        t.goto(cellcenter[cellnumber])
        t.dot(180,turn)
        t.update()
        #Add the move to the occupied list for the player
        occupied[turn].append(cellnumber)
        #Disallow the move from future rounds
        validinputs.remove(cellnumber)
        #check if player has won the game
        if win_game() == True:
            validinputs = []
            messagebox.showinfo("End Game",f"Congrats player {turn}, you won!")
        elif rounds == 9:
            messagebox.showinfo("Tie Game", "Game over, it's tie!")
        rounds +=1
            
        if turn == "blue":
            turn = "white"
        else:
            turn = "blue"
    else:
        messagebox.showinfo("Error", "Sorry, that's an invalid move!")
        

t.onscreenclick(mark_cell)
t.listen()    
t.done()
try:
    t.bye()
except t.Terminator:
    print("exit Turtle")
    
    
    
    
    
    
    