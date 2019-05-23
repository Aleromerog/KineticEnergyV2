#!/usr/bin/env python
# coding: utf-8

# In[10]:


#https://ocw.tudelft.nl/wp-content/uploads/H-L-2_Introduction_to_Biomechanics.pdf Mass reference
#https://msdn.microsoft.com/en-us/library/hh973078.aspx kinect documentation

import xml.etree.ElementTree as ET
import lxml.etree as ET2
import re
import os
import xlsxwriter

PATH = "D:\\KineticEnergy\ProyectoIJD_2016"
print("Running..")


        
class Point:
     def __init__ (self,x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        


class Skeleton:
    def __init__ (self, fileName):
        parser = ET2.ETCompatXMLParser()
        self.tree = ET2.parse(fileName, parser)
        root = self.tree.getroot()
        root.tag, root.attrib
        self.file = fileName
           
    
    def getSkeletonJoints(self):
        SKELETONS = []
        for elem in self.tree.iter(tag = 'etiquetasEsqueleto'):
            #CREATES A STRING TO SAVE XML VALUES 
            myString = ""
            myString = elem.get('row')

            #FINDS ALL ROW VALUES AND SEPARATES BY JOINTS
            skeletonXml = re.findall("\[(.*?)\]", myString)

            skeString = []
            skeVal= []
            
            #ASIGNS VALUES TO EACH JOINT AND SAVES IT AS FLOAT  
            for i in range (0,15):
                skeString.append(skeletonXml[i].split(","))
                skeVal.append(Point(skeString[i][0],skeString[i][1],skeString[i][2]))

            #APPENDS ALL THE SKELETON ON A SKELETON LIST
            SKELETONS.append(skeVal)

        return SKELETONS
    
    
    def getDate(self):
        dateAndTime = [""]
        for elem in self.tree.iter(tag = 'sesion'):
            dateAndTime = elem.get('fecha')
            dateAndTime = dateAndTime.split(" ")
        return dateAndTime[0]
    
    def getTime(self):
        dateAndTime = ["", ""]
        for elem in self.tree.iter(tag = 'sesion'):
            dateAndTime = elem.get('fecha')
            dateAndTime = dateAndTime.split(" ")
        return dateAndTime[1]
    
    def getName(self):
        name = ""
        for elem in self.tree.iter(tag = 'jugador'):
            name = elem.get('apellido') + " " + elem.get('nombre')
            
        return name
        
    def getNameId(self):
        name = "" 
        for elem in self.tree.iter(tag = 'jugador'):
            if(elem.get('nameId')):
                name = name + elem.get('nameId')
        return name
    
    def getGameId(self):
        name = self.file 
        name = name.split("\\")
        name = name[len(name)-1] 
        name = name.split("_")
        return name[0]
        
    def getMass(self, nameId):
        # JOINTS POSITIONS:
            # 0.  VNeck
            # 1.  VRHand
            # 2.  VLHand
            # 3.  VHead
            # 4.  VLShoulder
            # 5.  VRShoulder
            # 6.  VLElbow
            # 7.  VRElbow
            # 8.  VTorso
            # 9.  VLHip
            # 10. VRHip
            # 11. VLKnee
            # 12. VRKnee
            # 13. VLFoot
            # 14. VRFoot
        #masa 0 nino 6 años
        #masa 1 niño 10 años 
        #masa 2 niño 5 años
        #Masa 3 nino 4 años
        #Masa 4 nino 8 años
     
        m = [[5.3392,0.15325,0.15325,3.2426,0.5473,0.5473,0.47868,0.47868,7.6879,1.8251,1.8251,0.4985,0.4985,0.1499,0.1499],
            [6.0916,0.2225,0.2225,3.6966,0.7972,0.7972,0.60152,0.60152,10.5166,3.5484,3.5484,1.09,1.09,0.3656,0.3656],
            [5.3464,0.134675,0.134675,3.1161,0.50461,0.50461,0.45719,0.45719,7.03765,1.44345,1.44345,0.34753,0.34753,0.08705,0.08705],
            [5.3536,0.1161,0.1161,2.9896,0.46192,0.46192,0.4357,0.4357,6.3874,1.0618,1.0618,0.19656,0.19656,0.0242,0.0242],
            [5.5931,0.18695,0.18695,3.46155,0.65584,0.65584,0.532305,0.532305,9.0062,2.62045,2.62045,0.78222,0.78222,0.25755,0.25755]]

        if nameId == "IA" or nameId == "JS" or nameId == "AV":
            return m[0]
        elif nameId == "SB":
            return m[1]
        elif nameId == "SD" or nameId == "MS":
            return m[2]
        elif nameId == "EF" or nameId == "AM":
            return m[3]
        elif nameId == "PR":
            return m[4]
        
    def getKineticEnergy(self, nameId):
        skeletons = self.getSkeletonJoints()
        kinetic = 0.0
        velocity = 0
        time = 1/24
        totalTime = 0
        m = self.getMass(nameId)
        KineticPerJoint = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for num in range(len(skeletons)-1):
            for joint in range(0, 15):
                xi = (skeletons[num+1][joint].x - skeletons[num][joint].x)/1000
                yi = (skeletons[num+1][joint].y - skeletons[num][joint].y)/1000
                zi = (skeletons[num+1][joint].z - skeletons[num][joint].z)/1000
                
                distance = ((xi**2) + (yi**2) + (zi**2) )**(1/2)
                velocity = distance/time
                kinetic += m[joint] * velocity**2
                KineticPerJoint[joint] += (m[joint] * velocity**2) / 2
            totalTime = totalTime + time
        KineticPerJoint.append(kinetic/2)
        KineticPerJoint.append(totalTime)
        return KineticPerJoint
    
    

class ReadXml:
    def __init__(self, fileName):
     
        skeleton = Skeleton(fileName)
        
        self.nameId = skeleton.getNameId()
        self.kineticForce = skeleton.getKineticEnergy(self.nameId)
        self.name = skeleton.getName()
        self.date = skeleton.getDate()
        self.time = skeleton.getTime()
        self.gameId = skeleton.getGameId()

        

class ReadAllXml:
    def __init__(self, dire):
        self.file = []  
        self.count = 0
        dire = dire.replace(":\\", ":\\\\")
        for root, dirs, files in os.walk(dire):
            for file in files:
                if file.endswith(".xml"):
                    xmlFile = str((os.path.join(root, file)))
                    xmlFile = xmlFile.replace(":\\", ":\\\\")
                    
                    try:
                        xm = ReadXml(xmlFile)
                        if xm.kineticForce[0] != 0:
                            self.file.append(xm)
                            self.count += 1
                    except:
                        print("Algo salio mal con:", xmlFile, "Se ha ignorado el Archivo")
    
    def CreateExcel(self):
        workbook = xlsxwriter.Workbook("KinectProyect.xlsx")
        worksheet = workbook.add_worksheet()
        row = 2
        
        headers = {'columns' : [{'header': 'Nombre'},
                   {'header': 'Name Id'},
                   {'header': 'Fecha'},
                   {'header': 'Hora'},
                   {'header': 'Duración (segundos)'},
                   {'header': 'Game Id'},
                   {'header': 'VNeck'},
                   {'header': 'VRHand'},
                   {'header': 'VLHand'},
                   {'header': 'VHead'},
                   {'header': 'VLShoulder'},
                   {'header': 'VRShoulder'},
                   {'header': 'VLElbow'},
                   {'header': 'VRElbow'},
                   {'header': 'VTorso'},
                   {'header': 'VLHip'},
                   {'header': 'VRHip'},
                   {'header': 'VLKnee'},
                   {'header': 'VRKnee'},
                   {'header': 'VLFoot'},
                   {'header': 'VRFoot'},
                   {'header': 'Energía cinética total (Joules)'}]
                  }
        #
        
        worksheet.add_table('A1:V' + str(self.count+1), headers)
       
        for i in range (self.count):
            table = [self.file[i].name, 
                     self.file[i].nameId, 
                     self.file[i].date, 
                     self.file[i].time, 
                     self.file[i].kineticForce[16], 
                     self.file[i].gameId,
                     self.file[i].kineticForce[0],
                     self.file[i].kineticForce[1],
                     self.file[i].kineticForce[2],
                    self.file[i].kineticForce[3],
                    self.file[i].kineticForce[4],
                    self.file[i].kineticForce[5],
                    self.file[i].kineticForce[6],
                    self.file[i].kineticForce[7],
                    self.file[i].kineticForce[8],
                    self.file[i].kineticForce[9],
                    self.file[i].kineticForce[10],
                    self.file[i].kineticForce[11],
                    self.file[i].kineticForce[12],
                    self.file[i].kineticForce[13],
                    self.file[i].kineticForce[14],
                    self.file[i].kineticForce[15],]
            worksheet.write_row( 'A'+ str(row), table)
            row += 1
            
        
        workbook.close()
        

archivo = ReadAllXml(PATH)
archivo.CreateExcel()
print("Done")


# In[6]:


s = [[1,2,3],[2,3,4]]


# In[ ]:




