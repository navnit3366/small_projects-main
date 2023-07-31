from graphics_mine import *
from three_button_monte import Door
from random import choice

def click(mouse,d1,d2,d3):
    if d1.clicked(mouse):
        return d1.get_door()
    elif d2.clicked(mouse):
        return d2.get_door()
    elif d3.clicked(mouse):
        return d3.get_door()

def result(win,door,num):
    if door == num:
        info = Text(Point(4,3), f"Correct, the door number is {door}.").draw(win)
        return info
    else:
        info = Text(Point(4,3), f"Lost, the door number is {door}.").draw(win)
        return info


def main():
    win = GraphWin("Three Button Monte", 450, 400)
    win.setCoords(0, 0, 13, 12)
    win.setBackground("white")
    #Draw the doors
    d1 = Door(win,Point(1,5), Point(4, 10), "green",1)
    d1.draw()
    d2 = Door(win,Point(5, 5) , Point(8,10), "blue", 2)
    d2.draw()
    d3 = Door(win, Point(9,5), Point(12,10), "gray", 3)
    d3.draw()
    #Draw the condition
    text = Text(Point(6.5,11), "Choose a door")
    text.draw(win)
    exit = Rectangle(Point(9,1.85), Point(11, 2.25))
    exit.setFill("cyan")
    exit.draw(win)
    Text(Point(10,2), "EXIT").draw(win)
    #Choosing a door random
    doors = [1,2,3]
    door = choice(doors)
    #Implementing the logic
    i = True
    while True:
        mouse = win.getMouse()
        if exit.getP1().getX() <= mouse.getX() <= exit.getP2().getX() and exit.getP1().getY() <= mouse.getY() <= exit.getP2().getY():
            i = False
            break
        else:
            num = click(mouse, d1, d2, d3)
            al = result(win, door, num)
            i = False
    win.close()

main()
