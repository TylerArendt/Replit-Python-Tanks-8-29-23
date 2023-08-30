import turtle
import Projectile
import math
import time
import random

b = 0
theta = 90
targetCoeff = 1
target_coords = (-350, -160)


def newTank(me):
  t = turtle.Turtle()
  t.shape(me)
  t.turtlesize(1)
  t.penup()
  t.goto(340, -160)

  global b
  b = turtle.Turtle()
  b.penup()
  b.hideturtle()
  b.width(3)
  drawbarrel(180)
  return t
  
def drawbarrel(angle): 
  turtle.tracer(0, 0)
  global b
  b.clear()
  b.showturtle()
  b.goto(326, -153)
  b.penup()
  b.seth(angle)
  b.forward(5)
  b.pendown()
  b.forward(25)
  b.penup()
  b.hideturtle()
  turtle.tracer(1, 0)


def fire(projectile):
  #randomly generate theta based on split search
  global theta, targetCoeff
  #if targetCoeff registers if last shot was too low or high
  #eventually narrows onto spot
  theta = theta + random.randint(0, 50) * targetCoeff
  if theta > 180:
    theta = 180
  if theta < 90:
    theta = 90
  drawbarrel(theta)
  turtle.update()
  #new projectile fire projectile; see playerTank fire for more details
  p = Projectile.newProjectile(projectile, 330, -160, theta, 100)
  while p.xcor() > -370 and p.xcor() < 370 and p.ycor() > -180:
    p.time = p.time + .2
    xPos = p.x0 + p.v0 * math.cos(p.heading() * math.pi / 180) * p.time
    yPos = p.y0 + p.v0 * math.sin(
      p.heading() * math.pi / 180) * p.time - .5 * 9.8 * p.time * p.time
    p.goto(xPos, yPos)
    turtle.update()
    time.sleep(.05)
    if abs(p.xcor() - target_coords[0]) < 40 and abs(p.ycor() -
                                                     target_coords[1]) < 30:
      p.hideturtle()
      return True
  #check whether projectile is too high or low, adjust coeff to modify next trajectory accordingly
  if p.xcor() > target_coords[0]:
    targetCoeff = -1
  if p.ycor() > target_coords[1]:
    targetCoeff = 1
  p.hideturtle()
  return False


def erasebarrel():
  b.clear()
