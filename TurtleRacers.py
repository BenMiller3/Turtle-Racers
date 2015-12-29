from turtle import *            
import random
import time
import pygame

def race():
    reset()
    clear()
    hideturtle()
    penup()
    starter = pygame.mixer.Sound('pop.wav')
    pygame.mixer.Sound.play(starter)
    goto(200,200)
    goto(0,0)
    goto(-300,140)
    write("3", move=False, align="left", font=("Arial", 60, "bold"))
    goto(85,0)
    clear()
    hideturtle()
    penup()
    goto(-300,140)
    write("2", move=False, align="left", font=("Arial", 60, "bold"))
    goto(85,0)
    clear()
    hideturtle()
    penup()
    goto(-300,140)
    write("1", move=False, align="left", font=("Arial", 60, "bold"))
    goto(85,0)
    clear()
    hideturtle()
    penup()
    goto(-300,140)
    write("GO!", move=False, align="left", font=("Arial", 60, "bold"))
    goto(85,0)
    clear()
    race = True
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while(race == True):

        v = random.random()*11
        w = random.random()*11
        x = random.random()*11
        y = random.random()*11
        z = random.random()*11
        tut1.forward(v)
        tut2.forward(w)
        tut3.forward(x)
        tut4.forward(y)
        tut5.forward(z)
        a = a + v
        b = b + w
        c = c + x
        d = d + y
        e = e + z
        if(a >= 1095 or b >= 1095 or c >= 1095 or d >= 1095 or e >= 1095):
            race = False
            
    winners = [a,b,c,d,e]
    winners = sorted(winners)
    first = ""
    second = ""
    third = ""
    fourth = ""
    fifth = ""

    if(winners[4] == a):
        first = "1. Red"
    elif(winners[4] == b):
        first = "1. Blue"
    elif(winners[4] == c):
        first = "1. Green"
    elif(winners[4] == d):
        first = "1. Yellow"
    elif(winners[4] == e):
        first = "1. Orange"
    else:
        first = "ERROR"

    
    if(winners[3] == a):
        second = "2. Red"
    elif(winners[3] == b):
        second = "2. Blue"
    elif(winners[3] == c):
        second = "2. Green"
    elif(winners[3] == d):
        second = "2. Yellow"
    elif(winners[3] == e):
        second = "2. Orange"
    else:
        second = "ERROR"

    if(winners[2] == a):
        third = "3. Red"
    elif(winners[2] == b):
        third = "3. Blue"
    elif(winners[2] == c):
        third = "3. Green"
    elif(winners[2] == d):
        third = "3. Yellow"
    elif(winners[2] == e):
        third = "3. Orange"
    else:
        third = "ERROR"

    if(winners[1] == a):
        fourth = "4. Red"
    elif(winners[1] == b):
        fourth = "4. Blue"
    elif(winners[1] == c):
        fourth = "4. Green"
    elif(winners[1] == d):
        fourth = "4. Yellow"
    elif(winners[1] == e):
        fourth = "4. Orange"
    else:
        fourth = "ERROR"

    if(winners[0] == a):
        fifth = "5. Red"
    elif(winners[0] == b):
        fifth = "5. Blue"
    elif(winners[0] == c):
        fifth = "5. Green"
    elif(winners[0] == d):
        fifth = "5. Yellow"
    elif(winners[0] == e):
        fifth = "5. Orange"
    else:
        fifth = "ERROR"
    fin = pygame.mixer.Sound('app.wav')
    pygame.mixer.Sound.play(fin)
    hideturtle()
    penup()
    goto(-500,140)
    write(first, move=False, align="left", font=("Arial", 30, "bold"))
    goto(-500,90)
    write(second, move=False, align="left", font=("Arial", 30, "bold"))
    goto(-500,40)
    write(third, move=False, align="left", font=("Arial", 30, "bold"))
    goto(-500,-10)
    write(fourth, move=False, align="left", font=("Arial", 30, "bold"))
    goto(-500,-60)
    write(fifth, move=False, align="left", font=("Arial", 30, "bold"))

    
    for i in range(75):
        v = random.random()*11
        w = random.random()*11
        x = random.random()*11
        y = random.random()*11
        z = random.random()*11
        tut1.forward(v)
        tut2.forward(w)
        tut3.forward(x)
        tut4.forward(y)
        tut5.forward(z)
        
    hideturtle()
    penup()
    goto(-500,-160)
    write("Press Spacebar to race again", move=False, align="left", font=("Arial", 30, "bold"))

def reset():
    tut1.up()                  
    tut2.up()
    tut3.up()
    tut4.up()
    tut5.up()
    tut1.goto(-600,0)
    tut2.goto(-600,-300)
    tut3.goto(-600,180)
    tut4.goto(-600,-180)
    tut5.goto(-600,300)
    

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
song = pygame.mixer.Sound('son.wav')
pygame.mixer.Sound.play(song,3)
song.set_volume(0.1)


wn = Screen()           
wn.title("Turtle Racers")
wn.setup(width = 1500, height = 1000, startx = 0, starty = 0)
wn.bgcolor('black')
hideturtle()
penup()
goto(-400,100)
pencolor('white')
write("Turtle Racers", move=False, align="left", font=("Arial", 60, "bold"))
goto(500,500)
goto(-400,0)
write("Created by: Ben Miller", move=False, align="left", font=("Arial", 30, "bold"))
goto(500,500)
goto(-500,-500)
clear()
pencolor('black')

bgpic('track(1).gif')
    
tut1 = Turtle()    
tut2 = Turtle()
tut3 = Turtle()
tut4 = Turtle()
tut5 = Turtle()
tut1.shapesize(5,5,6)
tut2.shapesize(5,5,6)
tut3.shapesize(5,5,6)
tut4.shapesize(5,5,6)
tut5.shapesize(5,5,6)
tut1.color('black','red')
tut2.color('black','blue')
tut3.color('black','green')
tut4.color('black','yellow')
tut5.color('black','orange')
tut1.shape('turtle')
tut2.shape('turtle')
tut3.shape('turtle')
tut4.shape('turtle')
tut5.shape('turtle')
hideturtle()
penup()
goto(-250,140)
write("Press Spacebar to begin the race", move=False, align="left", font=("Arial", 30, "bold"))
gameOver = False
while(gameOver == False):
    reset()
    wn.onkeypress(race)
    wn.listen()

