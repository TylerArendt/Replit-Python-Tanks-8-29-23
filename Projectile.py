import turtle

# new projectile object; set size, shape, heading, position
def newProjectile(projectile, x, y, theta, v0):
  t = turtle.Turtle()
  t.shape(projectile)
  t.turtlesize(1)
  t.penup()
  t.goto(x, y)
  t.setheading(theta)
  t.time = 0
  t.v0 = v0
  t.x0 = x
  t.y0 = y
  return (t)
