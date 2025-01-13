#Christopher Chen, Oliver Giron, Destiney Cardenas, Annika Chauhan
#10/07/24

import turtle
import random
turt = turtle.Turtle()
turtle.colormode(255)
annika = turtle.Turtle()
destiney= turtle.Turtle()
dragonfly = turtle.Turtle()



#functions
#Draw awesome gradient for sky you nitpicking sob
def drawGradient(length, r, g, b, rr, gg, bb):
    turt.speed(0)
    turt.setheading(0)
    turt.width(10)
    #transitions from color to color over length (if length is done, it will just keep drawing color)
    for i in range (length):
        turt.pencolor(int(r), int(g), int(b))
        turt.pu()
        turt.goto(-500, 400-5*i)
        turt.pd()
        turt.forward(1000)
        if r != rr:
            r = r-(r-rr)/(abs(r-rr))
        if g != gg:
            g = g-(g-gg)/(abs(g-gg))
        if b != bb:
            b = b-(b-bb)/(abs(b-bb))
#buncha stars
def drawStars(amount, size1, size2):
    turt.pencolor(255, 255, 255)
    for i in range(amount):
        turt.pu()
        turt.goto(random.randint(-500, 500), random.randint(-500, 500))
        turt.pd()
        turt.dot(random.randint(size1, size2))
#transitions from color to color over size (if size is done, it will just keep drawing color)
def drawDotGradient(size, r, g, b, rr, gg, bb):
    turt.speed(0)
    turt.setheading(0)
    turt.width(10)
    for i in range (size):
        turt.pencolor(int(r), int(g), int(b))
        turt.dot(size-i)
        if r != rr:
            r = r-(r-rr)/(abs(r-rr))
        if g != gg:
            g = g-(g-gg)/(abs(g-gg))
        if b != bb:
            b = b-(b-bb)/(abs(b-bb))
#annika's code to do water
def drawWater():
  annika.speed(0)
  annika.penup()
  annika.goto(500,0)
  annika.pendown()
  annika.setheading(180)
  num = 212
  gre = 203
  red=52
#creates an ombre effect
  for i in range (70):
    annika.pencolor(red,num,gre)
    num=num-1
    gre=gre+1
    red=red+1
    if gre > 255: #stops the green number from exceeding 255
        gre=255
    annika.forward(1000) #each color gets repeated for 6 pixel rows
    annika.left(90)
    annika.forward(1)
    annika.left(90)
    annika.forward(1000)
    annika.right(90)
    annika.forward(1)
    annika.right(90)
    annika.forward(1000)
    annika.left(90)
    annika.forward(1)
    annika.left(90)
    annika.forward(1000)
    annika.right(90)
    annika.forward(1)
    annika.right(90)
    annika.forward(1000)
    annika.left(90)
    annika.forward(1)
    annika.left(90)
    annika.forward(1000)
    annika.right(90)
    annika.forward(1)
    annika.right(90)

#annika's code to draw mountains
def drawMountains(size):
  annika.speed(0)
  annika.penup()
  annika.goto(-500,0)
  annika.pendown()
  annika.pencolor(0,0,0)
  annika.begin_fill()
  annika.setheading(180)
  annika.forward(400)
  annika.right(135)
  annika.forward(size)
#able to change the height of mountains
  for i in range(30):
    annika.right(90)
    annika.forward(size-10)
    annika.left(90)
    annika.forward(size-10)
  annika.right(90)
  annika.forward(size)
  annika.left(90)
  annika.end_fill()
            
def drawOliver():
    drawGradient(100, 50, 123, 201, 155, 17, 247)
    drawStars(100, 3, 10)
    turt.pu()
    turt.goto(200, 200)
    turt.pd()
    drawDotGradient(200, 245, 245, 213, 245, 245, 103)

def drawAnnika():
    drawMountains(45)
    drawWater()

def drawDestiney():
    greenery()

def drawScene():
    drawOliver()
    drawAnnika()
    greenery()
    draw_dragonflies()
#this is going to make curvy lines to make the greenery 
def curvedLine(length, curve):
    for i in range(length):
        destiney.forward(3)
        destiney.left(curve)

#this will make one lilypad
#color = string
#size = integer
#x,y = integers
def lillypad(size,color,x,y):
    for i in range(1):
        destiney.penup()
        destiney.goto(x,y)
        destiney.setheading(0)
        destiney.fillcolor(color)
        destiney.pendown()
        destiney.begin_fill()
        destiney.circle(size,320)
        destiney.setheading(45)
        destiney.forward(size)
        destiney.right(138)
        destiney.forward(size)
        destiney.end_fill()


#this is going to make lilypads but these are facing a different way
def lillypad_double(size,color,x,y):
    for i in range(1):
        destiney.penup()
        destiney.goto(x,y)
        destiney.setheading(180)
        destiney.fillcolor(color)
        destiney.pendown()
        destiney.begin_fill()
        destiney.circle(size,320)
        destiney.setheading(230)
        destiney.forward(size)
        destiney.right(138)
        destiney.forward(size)
        destiney.end_fill()


        
#this is going to randomize the position of the lilypad and will make multiple of them   
def lillypads_plural():
    for i in range(random.randint(4,6)):
        lillypad(random.randint(15,40),(random.randint(39,89),random.randint(156,158),random.randint(39,68)),random.randint(-400,400),random.randint(-418,-50))
        lillypad_double(random.randint(15,40),(random.randint(3,148),random.randint(252,255),random.randint(3,127)),random.randint(-400,400),random.randint(-418,-50))

#this makes leaves that face right but are only on the left
def leaf_left(length, color,x,y):
    destiney.penup()
    destiney.goto(x,y)
    destiney.setheading(90)
    destiney.fillcolor(color)
    destiney.pendown()
    destiney.begin_fill()
    curvedLine(length,-.5)
    destiney.right(170)
    curvedLine(length-1,.5)
    destiney.right(100)
    destiney.forward(length/2)
    destiney.end_fill()

#this makes leave that face left but are only on the right
def leaf_right(length, color,x,y):
    destiney.penup()
    destiney.goto(x,y)
    destiney.setheading(90)
    destiney.fillcolor(color)
    destiney.pendown()
    destiney.begin_fill()
    curvedLine(length,.5)
    destiney.right(172)
    curvedLine(length+4,-.5)
    destiney.right(100)
    destiney.forward((length/2)+2)
    destiney.end_fill()

#this makes double leaves in the middle
def leaves(length, color,x,y):
    destiney.penup()
    destiney.goto(x,y)
    destiney.setheading(90)
    destiney.fillcolor(color)
    destiney.pendown()
    destiney.begin_fill()
    curvedLine(length,-.5)
    destiney.right(170)
    curvedLine(length-1,.5)
    destiney.right(100)
    destiney.forward(length/2)
    destiney.end_fill()
    destiney.penup()
    destiney.goto(x,y)
    destiney.setheading(90)
    destiney.fillcolor(color)
    destiney.pendown()
    destiney.begin_fill()
    curvedLine(length,.5)
    destiney.right(172)
    curvedLine(length+4,-.5)
    destiney.right(100)
    destiney.forward((length/2)+2)
    destiney.end_fill()

#this puts all of the functions together to just make all of them run together
def greenery():
    lillypads_plural()
    for i in range(3):
      leaf_left(random.randint(40,65),(random.randint(39,89),random.randint(156,158),random.randint(39,68)),random.randint(-400,-100),-418)
      leaf_right(random.randint(40,65),(random.randint(39,89),random.randint(156,158),random.randint(39,68)),random.randint(100,400),-418)
      leaves(random.randint(40,65),(random.randint(39,89),random.randint(156,158),random.randint(39,68)),random.randint(-100,100),-418)
def draw_dragonflyHead(size,x,y):
    dragonfly.pu()
    dragonfly.goto(x,y)
    dragonfly.pd()
    dragonfly.begin_fill()
    dragonfly.color("#ffdd99")
    dragonfly.dot(size)
    dragonfly.rt(90)
    for i in range(30):
        dragonfly.forward(3)
        dragonfly.left(1)
    dragonfly.rt(180)
    dragonfly.right(30)
    for i in range(30):
        dragonfly.forward(3)
        dragonfly.left(1)
    dragonfly.right(30)
    dragonfly.rt(180)
    
    #wings
    for i in range(15):
        dragonfly.forward(3)
        dragonfly.left(1)
    dragonfly.right(90)
    for i in range(15):
        dragonfly.forward(3)
        dragonfly.right(2)
    dragonfly.rt(180)
    dragonfly.left(45)
    for i in range(15):
        dragonfly.forward(3)
        dragonfly.right(2)
    #moving back to head to create 2nd wing
    dragonfly.left(30)
    dragonfly.rt(180)
    dragonfly.pu()
    dragonfly.goto(x,y)
    dragonfly.rt(90)
    dragonfly.pd()
    for i in range(15):
        dragonfly.forward(3)
        dragonfly.left(1)
    dragonfly.right(45)
    #creating 2nd wing
    dragonfly.pu()
    dragonfly.goto(x,y)
    dragonfly.pd()
    for i in range(15):
        dragonfly.forward(3)
        dragonfly.right(1)
    dragonfly.left(45)
    dragonfly.pu()
    dragonfly.goto(x,y)
    dragonfly.rt(180)
    dragonfly.pd()
    for i in range(15):
        dragonfly.forward(3)
        dragonfly.right(1)
    dragonfly.left(90)
    for i in range(15):
        dragonfly.forward(3)
        dragonfly.left(2)
    dragonfly.rt(180)
    dragonfly.right(45)
    for i in range(15):
        dragonfly.forward(3)
        dragonfly.left(2)
    dragonfly.end_fill()

def draw_dragonflies():
    draw_dragonflyHead(random.randint(15,30),random.randint(-300,300),random.randint(0,300))
    draw_dragonflyHead(random.randint(15,30),random.randint(-300,300),random.randint(0,300))
    draw_dragonflyHead(random.randint(15,30),random.randint(-300,300),random.randint(0,300))


#main
drawScene()
