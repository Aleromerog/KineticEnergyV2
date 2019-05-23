from vpython import *

ball = sphere(pos=vector(0,10,0), radius=1, color=color.red)
floor = box(pos=vector(0,0,0), size = vector(10,0.5,10), color=color.green)
ball.velocity=vector(0,-1,0)
dt=0.1
t=0
while (t<20):
    rate(50)
    ball.pos=ball.pos+ball.velocity*dt
    t=t+dt