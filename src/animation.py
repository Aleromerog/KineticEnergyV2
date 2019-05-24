from src.ReadFile import ReadFile
from vpython import *

def animate(fileName, kinetic, caloric):
    list = ReadFile.read(fileName)
    #joints
    ball1 = sphere(pos=vector(list[0][1],list[0][2],list[0][3]), radius=.05, color=color.blue)
    ball2 = sphere(pos=vector(list[0][4],list[0][5],list[0][6]), radius=.05, color=color.blue)
    ball3 = sphere(pos=vector(list[0][7],list[0][8],list[0][9]), radius=.05, color=color.blue)
    ball4 = sphere(pos=vector(list[0][10],list[0][11],list[0][12]), radius=.05, color=color.blue)
    ball5 = sphere(pos=vector(list[0][13],list[0][14],list[0][15]), radius=.05, color=color.blue)
    ball6 = sphere(pos=vector(list[0][16],list[0][17],list[0][18]), radius=.05, color=color.blue)
    ball7 = sphere(pos=vector(list[0][19],list[0][20],list[0][21]), radius=.05, color=color.blue)
    ball8 = sphere(pos=vector(list[0][22],list[0][23],list[0][24]), radius=.05, color=color.blue)
    ball9 = sphere(pos=vector(list[0][25],list[0][26],list[0][27]), radius=.05, color=color.blue)
    ball10 = sphere(pos=vector(list[0][28],list[0][29],list[0][30]), radius=.05, color=color.blue)
    ball11 = sphere(pos=vector(list[0][31],list[0][32],list[0][33]), radius=.05, color=color.blue)
    ball12 = sphere(pos=vector(list[0][34],list[0][35],list[0][36]), radius=.05, color=color.blue)
    ball13 = sphere(pos=vector(list[0][37],list[0][38],list[0][39]), radius=.05, color=color.blue)
    ball14 = sphere(pos=vector(list[0][40],list[0][41],list[0][42]), radius=.05, color=color.blue)
    ball15 = sphere(pos=vector(list[0][43],list[0][44],list[0][45]), radius=.05, color=color.blue)
    ball16 = sphere(pos=vector(list[0][46],list[0][47],list[0][48]), radius=.05, color=color.blue)
    #bones
    bone1 = arrow(pos=ball1.pos, axis=ball2.pos-ball1.pos,shaftwidth=0.01, color=color.red)

    print (len(list))
    current = canvas.get_selected() 
    current.background = color.white
    current.title = "Energía cinética: " + str(round(kinetic,2)) + " Joules, Energía calorica: " + str(round(caloric,2)) + " Cal"
    current.width = 1300;
    current.height = 800;
    for frame in range(1, len(list)-1):
        rate(15)
        print(vector(list[frame][1],list[frame][2],list[frame][3]))
        ball1.pos =  vector(list[frame][1],list[frame][2],list[frame][3])
        ball2.pos =  vector(list[frame][4],list[frame][5],list[frame][6])
        ball3.pos =  vector(list[frame][7],list[frame][8],list[frame][9])
        ball4.pos =  vector(list[frame][10],list[frame][11],list[frame][12])
        ball5.pos =  vector(list[frame][13],list[frame][14],list[frame][15])
        ball6.pos =  vector(list[frame][16],list[frame][17],list[frame][18])
        ball7.pos =  vector(list[frame][19],list[frame][20],list[frame][21])
        ball8.pos =  vector(list[frame][22],list[frame][23],list[frame][24])
        ball9.pos =  vector(list[frame][25],list[frame][26],list[frame][27])
        ball10.pos = vector(list[frame][28],list[frame][29],list[frame][30])
        ball11.pos = vector(list[frame][31],list[frame][32],list[frame][33])
        ball12.pos = vector(list[frame][34],list[frame][35],list[frame][36])
        ball13.pos = vector(list[frame][37],list[frame][38],list[frame][39])
        ball14.pos = vector(list[frame][40],list[frame][41],list[frame][42])
        ball15.pos = vector(list[frame][43],list[frame][44],list[frame][45])
        ball16.pos = vector(list[frame][46],list[frame][47],list[frame][48])

        bone1.pos = vector(list[frame][1],list[frame][2],list[frame][3])



    #TODO
    print("kpdo")