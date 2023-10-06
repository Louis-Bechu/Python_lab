# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:26:17 2023

@author: louis
"""


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

class intersection:
    
    def __init__(self,nom_fichier):
        self.nom_fichier = nom_fichier
        # coordinates = []
        with open(nom_fichier,'r') as f:
            lines = f.readlines()
        self.lines = lines
        # for line in lines : 
        #     if line.split() and line.split()[0] == 'vertex' :
        #         coordinates.append([int(line.split()[1]),int(line.split()[2]),int(line.split()[3])])
        # self.coordinate = coordinates
        # print(coordinates)
        
    def plotting(self): 
        coordinates = []
        for line in self.lines : 
            if line.split() and line.split()[0] == 'vertex' :
                coordinates.append([int(line.split()[1]),int(line.split()[2]),int(line.split()[3])])
        return(coordinates)

test = intersection(r'C:\Users\louis\Documents\Année M2 AMSS\Cursus commun\Preuve de concept (Godineau)\Mini projet\python_lab\cube.txt')
X=[]
Y=[]
Z=[]
for i in range(len(test.plotting())):
    X.append(test.plotting()[i][0])
    Y.append(test.plotting()[i][1])
    Z.append(test.plotting()[i][2])

fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot3D(X,Y,Z, 'green')
ax.set_title('3D line plot for 3D intersection')
plt.show()
      








