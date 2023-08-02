# Project 4 Part 2 - Art Exhibit 
# Name: Nandini Jirobe
# Date: June 10, 2021
# Course: CS111
# Summer Semester
# Project Theme: "THE GREAT RESCUE"


import turtle
import random
import time

# This function reads and filters the color shade lists
# The parameter file_name is the name of the color file
def randomShade(file_name):
  file = open(file_name)
  colorRGBs = file.readlines()
  colorShadeList = []

  for i in range(0,len(colorRGBs)):
    blank = ""
    tempList = colorRGBs[i].split("rgb(")
    colorRGBs[i] = blank.join(tempList )
    tempList = colorRGBs[i].split(")")
    colorRGBs[i]= blank.join(tempList )
    tempList = colorRGBs[i].split(",")
    for j in range(0,len(tempList )):
      tempList[j] = int(tempList [j].strip())
    colorShadeList.append(tempList )

  randomShade = random.randint(0,len(colorShadeList)-1)
  red = (colorShadeList[randomShade][0])
  green = (colorShadeList[randomShade][1])
  blue = (colorShadeList[randomShade][2])

  return red, green, blue

# The parameter xLoc is x-coordinate of the mountain
# The parameters yLocStart and yLocEnd is where the mountain starts and ends
def mountain(width, xLoc, yLocStart, yLocEnd):
  penSize = 10
  t.penup()
  t.pensize(penSize)
  layer = 1

  while yLocStart >= yLocEnd:
    t.goto(xLoc,yLocStart)
    t.pendown()
    for j in range (0, layer*width,5):
      t.pencolor(randomShade("purpleShades.txt"))
      t.forward(5)
    t.penup()
    t.goto(xLoc,yLocStart)
    t.pendown()
    for j in range (0, layer*width,5):
      t.pencolor(randomShade("purpleShades.txt"))
      t.backward(5)
    t.penup()
    yLocStart-=penSize
    layer+=1

# The parameters x and y is where the water starts being drawn 
# The parameters h and w is height an width of the water
def water(h, w, x, y ):
  t.penup()
  t.goto(x,y)
  penSize = 10
  t.pensize(penSize)
  t.pendown()
  for j in range(h):
    for i in range(20):
      t.pendown()
      t.pencolor(randomShade("blueShades.txt"))
      t.forward(w)
  
# The parameters startX and startY is where the land starts being drawn 
# The parameters endX and endY is where the land stops being drawn
def land(startX, endX, startY, endY ):
  t.penup()
  t.goto(startX-20,startY)
  penSize = 10
  t.pensize(penSize)

  while t.ycor()<endY:
    t.pendown()
    t.pencolor(randomShade("greenShades.txt"))
    t.forward(20)
    t.penup()
    if(t.xcor()>endX):
      t.left(90)
      t.forward(penSize)
      t.left(90)
    elif(t.xcor()<startX):
      t.right(90)
      t.forward(penSize)
      t.right(90)

# This function moves a turtle from start to end 
def turtle_walks(turtle, start, end):
  turtle.goto(start[0], start[1])
  turtle.showturtle()
  turtle.speed(1)
  turtle.goto(end[0], end[1])



# Turtle which draws landscape is setup:
t = turtle.Turtle()
screen = turtle.getscreen()
screen.colormode(255)
screen.bgcolor(0, 160, 153)
t.shape("arrow")
t.speed(10)

# Sun and moon turtles are setup
turtle.addshape("sun.gif")
turtle.addshape("moon.gif")
sun = turtle.Turtle()
sun.hideturtle()
sun.shape("sun.gif")
sun.penup()
sun.goto(25,100)
sun.showturtle()

# Draw landscape
mountain(25, -250, 50, 0)
mountain(20, 0, 100, 0)
mountain(25, 200, 75, 0)
land(-400, 400, -200, 5)
t.right(180)
riverXVar = -275
riverYVar = -200
for i in range(1,22):
  water(1, int(35/i), riverXVar, riverYVar)
  riverXVar+=10
  riverYVar+=10

# Turtles which displays text is setup
words = turtle.Turtle()
words.hideturtle()
words.penup()
words.goto(30, 150)
words.write("THE GREAT RESCUE", False, align = "center", font=("Courier", 14, "bold"))
time.sleep(2)
words.clear()

nameTurtle = turtle.Turtle()
nameTurtle.hideturtle()
nameTurtle.penup()
nameTurtle.goto(200, -190)
nameTurtle.color("white")
nameTurtle.write("by: Nandini Jirobe", False, align = "center", font=("Courier", 12, "bold"))

# house turtle is created and setup
turtle.addshape("house2.gif")
house = turtle.Turtle()
house.hideturtle()
house.shape("house2.gif")
house.penup()
house.hideturtle
house.goto(175, -100)
house.showturtle()

# pixelMan turtle is created and setup
turtle.addshape("pixelMan.gif")
pixelMan = turtle.Turtle()
pixelMan.hideturtle()
pixelMan.shape("pixelMan.gif")
pixelMan.penup()

# cat turtle is created and setup
turtle.addshape("cat1.gif")
turtle.addshape("cat2.gif")
cat = turtle.Turtle()
cat.shape("cat1.gif")
cat.hideturtle()
cat.penup()
cat.goto(200,87)
cat.showturtle()

# manInboat image is added to turtle shapes
turtle.addshape("manInBoat.gif")
manInBoat = turtle.Turtle()

# catmanballoon image is added to turtle shapes
turtle.addshape("catmanballoon.gif")
catmanballoon = turtle.Turtle()


# <-------------Story begins here ------------->

words.pencolor("black")
words.write("A cat was stuck in a tree in the mountains", False, align = "center", font=("Courier", 12, "normal"))
time.sleep(2)
words.clear()
words.write("A man decided to rescue the cat", False, align = "center", font=("Courier", 12, "normal"))
time.sleep(2)
words.clear()
words.write("He left his house...", False, align = "center", font=("Courier", 12, "normal"))
time.sleep(2)
words.clear()

# man stand outside house.
pixelMan.goto(63, -167)
pixelMan.showturtle()
turtle_walks(pixelMan,[63, -167], [-72,-170])
time.sleep(2)

# man rides in boat 
words.write("... and crossed the river on a boat", False, align = "center", font=("Courier", 12, "normal"))
time.sleep(2)
words.clear()
pixelMan.shape("manInBoat.gif")
pixelMan.goto(-177,-175) 
time.sleep(2)
pixelMan.showturtle()
turtle_walks(pixelMan, [-177,-175], [-72,-5])
pixelMan.shape("pixelMan.gif")
time.sleep(2)

# man walks up the mountain and reaches cat
turtle_walks(pixelMan,[-72,-5], [-397,6])
time.sleep(2)
words.write("He climbed up the mountains...", False, align = "center", font=("Courier", 12, "normal"))
time.sleep(2)
words.clear()
turtle_walks(pixelMan, [-397,6], [-267,73])
words.write("...both day...", False, align = "center", font=("Courier", 12, "normal"))
time.sleep(2)
words.clear()
turtle_walks(pixelMan, [-267,73], [-174,50])
words.write("...and night", False, align = "center", font=("Courier", 12, "normal"))
turtle_walks(pixelMan, [-174,50], [-11,125])
screen.bgcolor(28,46,74)
sun.goto(25,-400)
sun.shape("moon.gif")
sun.goto(25,100)
time.sleep(2)
words.clear()
sun.goto(25,-400)
sun.shape("sun.gif")
screen.bgcolor(0, 160, 153)
sun.goto(25,100)
time.sleep(2)
words.write("He finally found and rescued the cat!", False, align = "center", font=("Courier", 12, "normal"))
time.sleep(2)
words.clear()
turtle_walks(pixelMan, [-11,125], [122,71])

#The cat was happy and danced in joy 
words.write("The cat was so happy it jumped up and down in joy!", False, align = "center", font=("Courier", 12, "normal"))
for i in range(5):
  cat.goto(200,120)
  cat.shape("cat2.gif")
  time.sleep(1)
  cat.goto(200,87)
  cat.shape("cat1.gif")
  time.sleep(1)
time.sleep(2)
words.clear()

# pixelMan and cat go home
words.write("The man decided to take the cat home and take care if it.", False, align = "center", font=("Courier", 12, "normal"))
time.sleep(2)
words.clear()
words.write("Both of them went home in a hot air balloon.", False, align = "center", font=("Courier", 12, "normal"))
pixelMan.goto(200,87)
cat.hideturtle()
pixelMan.shape("catmanballoon.gif")
time.sleep(2)
pixelMan.goto(175, -100)
words.clear()
words.write("They lived happily ever after.", False, align = "center", font=("Courier", 12, "normal"))
time.sleep(2)
words.clear()
words.write("The end.", False, align = "center", font=("Courier", 12, "normal"))

  
#Image citations:
# pixelMan: (n.d.). www.stockunlimited.com. https://www.stockunlimited.com/similar/1957778.html. 

#house: (n.d.). www.istockphoto.com. https://www.istockphoto.com/vector/pixel-art-house-vector-8-bit-game-web-icon-set-isolated-on-white-background-gm1038703764-278023905. 

#cat: (n.d.). giphy.com. https://giphy.com/gifs/hoppip-cat-hoppip-pixel-art-ea74cjF0jieXu.  

#hot air balloon: (n.d.). www.shutterstock.com. https://www.shutterstock.com/image-vector/vector-illustration-balloon-pixel-art-1028960227. 

# pixelBoat:(n.d.). shutterstock.com. https://image.shutterstock.com/image-vector/ship-yacht-boat-pixel-art-260nw-712468606.jpg. 

