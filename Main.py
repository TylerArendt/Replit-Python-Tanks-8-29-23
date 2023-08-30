import turtle
import playerTank
import enemyTank
import time

screen = turtle.Screen()
screen.setup(800, 400)
screen.colormode(255)
turtle.bgcolor('grey')

turtle.tracer(0, 0)

me = "mytank.gif"
screen.addshape(me)

enemy = "enemytank.gif"
screen.addshape(enemy)

explosion = "Explosion.gif"
screen.addshape(explosion)

projectile = "Projectile.gif"
screen.addshape(projectile)

enemyAmmo = 'EnemyProjectile.gif'
screen.addshape(enemyAmmo)

t = playerTank.newTank(me)
e = enemyTank.newTank(enemy)

myTheta = 40
myV0 = 100
go = False

playerTank.drawbarrel(myTheta, myV0)

turtle.update()


def angleup():
  global myTheta, go, myV0
  if not go:
    go = True
    while go and myTheta < 91:
      myTheta = myTheta + 3
      playerTank.drawbarrel(myTheta, myV0)
      turtle.update()
      time.sleep(.1)


def angledown():
  global myTheta, go, myV0
  if not go:
    go = True
    while go and myTheta > -25:
      myTheta = myTheta - 3
      playerTank.drawbarrel(myTheta, myV0)
      turtle.update()
      time.sleep(.1)


def reset():
  global go
  go = False


def powerup():
  global myV0, go
  myV0 = myV0 + 3
  if myV0 > 255:
    myV0 = 255
  playerTank.drawbarrel(myTheta, myV0)
  turtle.update()


def powerdown():
  global myV0, go
  myV0 = myV0 - 3
  if myV0 < 0:
    myV0 = 0
  playerTank.drawbarrel(myTheta, myV0)
  turtle.update()


def fire(): # fires the player tank
  global myTheta, myV0, projectile, go, enemyAmmo
  if not go:
    go = True
    result = playerTank.fire(projectile, myTheta, myV0)
    if result == True:
      enemyTank.erasebarrel()
      e.shape(explosion)
    else:
      result = enemyTank.fire(enemyAmmo)
      if result == True:
        playerTank.erasebarrel()
        t.shape(explosion)
        

    go = False


turtle.onkeypress(angleup, "Left")
turtle.onkeypress(angledown, "Right")
turtle.onkeyrelease(reset, "Left")
turtle.onkeyrelease(reset, "Right")
turtle.onkeypress(powerup, "Up")
turtle.onkeyrelease(reset, "Up")
turtle.onkeypress(powerdown, "Down")
turtle.onkeyrelease(reset, "Down")
turtle.onkeypress(fire, "space")

turtle.listen()
turtle.done()
