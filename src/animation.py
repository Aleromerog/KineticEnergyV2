from src.ReadFile import ReadFile
from vpython import *

def animate(fileName, kinetic, caloric):
    list = ReadFile.read(fileName)
    #joints
    ball1 = sphere(pos=vector(list[0][1],list[0][2],list[0][3]), radius=.05, color=color.blue) #Codo Izquierdo
    ball2 = sphere(pos=vector(list[0][4],list[0][5],list[0][6]), radius=.05, color=color.blue) #Codo Derecho
    ball3 = sphere(pos=vector(list[0][7],list[0][8],list[0][9]), radius=.05, color=color.blue) #Pie Izquierdo
    ball4 = sphere(pos=vector(list[0][10],list[0][11],list[0][12]), radius=.05, color=color.blue) #Pie Derecho
    ball5 = sphere(pos=vector(list[0][13],list[0][14],list[0][15]), radius=.05, color=color.blue) #Mano Izquierda
    ball6 = sphere(pos=vector(list[0][16],list[0][17],list[0][18]), radius=.05, color=color.blue) #Mano Derecha
    ball7 = sphere(pos=vector(list[0][19],list[0][20],list[0][21]), radius=.05, color=color.blue) #Cabeza
    ball8 = sphere(pos=vector(list[0][22],list[0][23],list[0][24]), radius=.05, color=color.blue) #Cade Izquierda
    ball9 = sphere(pos=vector(list[0][25],list[0][26],list[0][27]), radius=.05, color=color.blue) #Cadera Derecha
    ball10 = sphere(pos=vector(list[0][28],list[0][29],list[0][30]), radius=.05, color=color.blue) #Rodila Izquierda
    ball11 = sphere(pos=vector(list[0][31],list[0][32],list[0][33]), radius=.05, color=color.blue) #Rodilla Derecha
    ball12 = sphere(pos=vector(list[0][34],list[0][35],list[0][36]), radius=.05, color=color.blue) #Hombro Izquierdo
    ball13 = sphere(pos=vector(list[0][37],list[0][38],list[0][39]), radius=.05, color=color.blue) #Hombro Derecho
    ball14 = sphere(pos=vector(list[0][40],list[0][41],list[0][42]), radius=.05, color=color.blue) #Espina Dorsal Baja
    ball15 = sphere(pos=vector(list[0][43],list[0][44],list[0][45]), radius=.05, color=color.blue) #Espina Dorsal Media
    ball16 = sphere(pos=vector(list[0][46],list[0][47],list[0][48]), radius=.05, color=color.blue) #Espina Dorsal Alta
    #bones
    bone1 = arrow(pos=ball5.pos, axis=ball1.pos-ball5.pos, shaftwidth=0.01, color=color.red) #Mano a Codo Izquierdos
    bone2 = arrow(pos=ball6.pos, axis=ball2.pos-ball6.pos, shaftwidth=0.01, color=color.red) #Mano a Codo Derechos
    bone3 = arrow(pos=ball1.pos, axis=ball12.pos-ball1.pos, shaftwidth=0.01, color=color.red) #Codo a Hombro Izquierdos
    bone4 = arrow(pos=ball2.pos, axis=ball13.pos-ball2.pos, shaftwidth=0.01, color=color.red) #Codo a Hombro Derechos
    bone5 = arrow(pos=ball16.pos, axis=ball15.pos-ball16.pos, shaftwidth=0.01, color=color.red) #Espina Dorsal Alta a Media
    bone6 = arrow(pos=ball14.pos, axis=ball15.pos-ball14.pos, shaftwidth=0.01, color=color.red) #Espina Dorsal Baja a Media
    bone7 = arrow(pos=ball7.pos, axis=ball16.pos-ball7.pos, shaftwidth=0.01, color=color.red) #Cabeza a Espina Dorsal Alta
    bone8 = arrow(pos=ball12.pos, axis=ball16.pos-ball12.pos, shaftwidth=0.01, color=color.red) #Hombro Izquierdo a Espina Dorsal Alta
    bone9 = arrow(pos=ball13.pos, axis=ball16.pos-ball13.pos, shaftwidth=0.01, color=color.red) #Hombro Derecho a Espina Dorsal Alta
    bone10 = arrow(pos=ball3.pos, axis=ball10.pos-ball3.pos, shaftwidth=0.01, color=color.red) #Pie a Rodilla Izquierdos
    bone11 = arrow(pos=ball4.pos, axis=ball11.pos-ball4.pos, shaftwidth=0.01, color=color.red) #Pie a Rodilla Derechos
    bone12 = arrow(pos=ball10.pos, axis=ball8.pos-ball10.pos, shaftwidth=0.01, color=color.red) #Rodilla a Cadera Izquierdos
    bone13 = arrow(pos=ball11.pos, axis=ball9.pos-ball11.pos, shaftwidth=0.01, color=color.red) #Rodilla a Cadera Derechos
    bone14 = arrow(pos=ball8.pos, axis=ball14.pos-ball8.pos, shaftwidth=0.01, color=color.red) #Cadera Izquierda a Espina Dorsal Baja
    bone15 = arrow(pos=ball9.pos, axis=ball14.pos-ball9.pos, shaftwidth=0.01, color=color.red) #Cadera Derecha a Espina Dorsal Baja

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

        #bone1.pos = vector(list[frame][1],list[frame][2],list[frame][3])
        #Ya chingamos :)
        bone1.pos = ball5.pos
        bone1.axis = ball1.pos - ball5.pos

        bone2.pos = ball6.pos
        bone2.axis = ball2.pos - ball6.pos

        bone3.pos = ball1.pos
        bone3.axis = ball12.pos-ball1.pos

        bone4.pos = ball2.pos
        bone4.axis = ball13.pos-ball2.pos

        bone5.pos = ball16.pos
        bone5.axis = ball15.pos-ball16.pos

        bone6.pos = ball14.pos
        bone6.axis = ball15.pos-ball14.pos

        bone7.pos = ball7.pos
        bone7.axis = ball16.pos-ball7.pos

        bone8.pos = ball12.pos
        bone8.axis = ball16.pos-ball12.pos

        bone9.pos = ball13.pos
        bone9.axis = ball16.pos-ball13.pos

        bone10.pos = ball3.pos
        bone10.axis = ball10.pos-ball3.pos

        bone11.pos = ball4.pos
        bone11.axis = ball11.pos-ball4.pos

        bone12.pos = ball10.pos
        bone12.axis = ball8.pos-ball10.pos

        bone13.pos = ball11.pos
        bone13.axis = ball9.pos-ball11.pos

        bone14.pos = ball8.pos
        bone14.axis = ball14.pos-ball8.pos

        bone15.pos = ball9.pos
        bone15.axis = ball14.pos-ball9.pos
        

