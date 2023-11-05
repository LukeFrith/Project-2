import turtle 

window = turtle.Screen()
window.bgcolor("Light Blue")
pen = turtle.Turtle()


def create_Sun():

    pen.color("Yellow")
    pen.pensize(5)
    pen.speed(10)
    pen.goto(225,150)
    pen.pendown()
    pen.circle(50)
    pen.penup()
    pen.goto(225,200)
    
    for i in range(12):
        pen.penup()
        pen.forward(65)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(-85)
        pen.left(360/12)

def create_clouds():
    
    pen.color('White')
    pen.pensize(5)
    pen.speed(15)
    pen.pendown()
    pen.begin_fill()
    for i in range(4):
        pen.circle(20)
        pen.left(360/4)
    pen.end_fill()

    
def create_more_clouds_1():
    
    for i in range(3):
        create_clouds()
        pen.right(360/3)
        pen.penup()
        pen.forward(100)
        pen.pendown()

def create_more_clouds_2():
    for i in range(2):
        create_more_clouds_1()
        pen.penup()
        pen.forward(200) 
        pen.pendown() 
    pen.penup()    

def create_water():
    pen.color("Blue")
    pen.speed(5)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        
        pen.forward(1000)
        pen.right(90)
        pen.forward(215)
        pen.right(90)
        
    pen.end_fill()

def create_sand():
    pen.color("Yellow")
    pen.speed(5)
    pen.penup()
    pen.right(90)
    pen.forward(215)
    pen.left(90)
    pen.pendown() 
    pen.begin_fill()
    for i in range(2):
        pen.forward(1000)
        pen.right(90)
        pen.forward(200)
        pen.right(90)
    pen.end_fill()

def create_boat():
    pen.color("Brown")
    pen.speed(3)
    pen.begin_fill()
    for i in range(2):
        pen.forward(150)
        pen.left(90)
        pen.forward(80)
        pen.left(90)
    pen.end_fill()
    pen.left(90)
    pen.forward(75)
    pen.right(90)
    pen.forward(68)
    pen.left(90)
    pen.begin_fill()
    for i in range(2):
        pen.forward(45)
        pen.right(90)
        pen.forward(60)
        pen.right(90)
    
    pen.end_fill()

def create_more_boats():
    
        create_boat()
        pen.left(90)
        pen.forward(68)
        pen.left(90)
        pen.forward(75)
        pen.right(90)
        pen.penup()
        pen.forward(200)
        pen.right(180)
        pen.pendown()
        create_boat()
        pen.left(90)
        pen.forward(68)
        pen.left(90)
        pen.forward(75)
        pen.right(90)
        pen.penup()
        pen.forward(200)
        pen.right(180)
        pen.pendown()
        create_boat()
        

def create_blankets():
    pen.pendown()

    pen.begin_fill()
    for i in range(2):
        pen.forward(75)
        pen.right(90)
        pen.forward(35)
        pen.right(90)

    pen.end_fill()
    pen.right(45)
    pen.penup()
    pen.forward(175)
    pen.left(45)
    pen.pendown()
    

def create_coloured_blankets():
    colours = ["Light Green", "Light Blue", "Pink",  "Orange"]
    for i in colours:
        pen.color(i)
        create_blankets()


def create_umbrellas():
    pen.pendown()
    pen.speed(3)
    
    
    pen.right(270)
    pen.forward(50)
    pen.begin_fill()
    pen.circle(-25,180)
    pen.right(90)
    pen.forward(50)
    pen.end_fill()
    pen.penup()
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(175)
    pen.pendown()

def create_coloured_umbrellas():
    colours = ["Light Green", "Light Blue", "Pink",  "Orange"]
    for i in colours:
        pen.color(i)
        create_umbrellas()


def create_person():
    pen.color("White")
    pen.speed(3)
    pen.left(90)
    pen.forward(25)
    pen.right(90)
    pen.circle(10)
    pen.left(90)
    pen.forward(-15)
    pen.right(45)
    pen.forward(17)
    pen.forward(-17)
    pen.left(90)
    pen.forward(17)
    pen.forward(-17)   
    pen.right(45)
    pen.forward(-15)
    pen.right(135)
    pen.forward(17)
    pen.forward(-17) 
    pen.right(90)
    pen.forward(17)
    pen.forward(-17) 
    pen.left(135)

pen.penup()

create_Sun()

pen.penup()
pen.goto(-150,250)
pen.pendown()

create_more_clouds_2()

pen.goto(-500,75)

create_water()

create_sand()

pen.penup()
pen.goto(0,20)
pen.pendown()


create_more_boats()  

pen.penup()
pen.goto(-250,-250)
pen.pendown()
pen.right(90)
pen.left(45)

create_coloured_blankets()

pen.penup()
pen.goto(-300,-275)
pen.pendown()
pen.right(90)
pen.left(45)

create_coloured_umbrellas()

pen.penup()
pen.goto(0,-100)
pen.pendown()

create_person()  

pen.penup()
pen.goto(-300,-107)
pen.pendown()

create_person()

pen.penup()
pen.goto(275,-120)
pen.pendown()

create_person()

pen.penup()
pen.goto(150,-65)
pen.pendown()

create_person()

pen.penup()
pen.goto(-200,-155)
pen.pendown()

create_person()

turtle.done()
