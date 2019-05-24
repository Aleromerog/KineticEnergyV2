from vpython import *

ball = sphere(pos=vector(0,10,0), radius=.5, color=color.red)
floor = box(pos=vector(0,0,0), size = vector(10,0.5,10), color=color.green)
ball.velocity=vector(0,-1,0)
dt=.1
t=0
current = canvas.get_selected() 
current.background = color.cyan
current.caption = "Hee"


for i in range(0, 1000000):
    rate(100)
    ball.pos=ball.pos + vector(0, -.1, 0)
 	

#añlsdjflkñsaj

exit()