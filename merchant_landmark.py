# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:32:44 2020

@author: yigit
"""

import math
import csv
import matplotlib.pyplot as plt
import numpy as np
import pydicom
import nrrd
from PIL import Image
import pandas as pd

'''Load dcm and fcsv files'''
#from pydicom.data import get_testdata_files
file_dcm=("C:/Users/yigit/OneDrive/Masaüstü/landmark/EE626ED3.dcm")
#file_mrml=("C:/Users/yigit/OneDrive/Masaüstü/landmark/2020-04-15-Scene.mrml")
#file_nrrd=("C:/Users/yigit/OneDrive/Masaüstü/landmark/EE626ED3.nrrd")
#file_fcsv=("C:/Users/yigit/OneDrive/Masaüstü/landmark/F.fcsv")
#file_png=("C:/Users/yigit/OneDrive/Masaüstü/landmark/2020-04-15-Scene.png")
#file_mrb=("C:/Users/yigit/OneDrive/Masaüstü/landmark/landmark_folder/2020-04-15-Scene.mrb")
file_000=("C:/Users/yigit/OneDrive/Masaüstü/landmark/000.fcsv")

#df=pd.read_csv(file_fcsv,header=None)


'''Read Landmark file(.fscv)'''
# Read .fcsv file line by line
with open(file_000) as f:
    landmark_file=f.readlines()
    
    
landmark_file=landmark_file[3:] # get ride of unneccessary lines

'''Creat Landmark Dictionary from fcsv'''
landmarks={}
for line in landmark_file:
    splited_line=line.split(',') #split 
    
    name=splited_line[0][22:30]     #read name of node as 'Node_0'
    x_dimension=splited_line[1]     #read x dimension of node
    y_dimension=splited_line[2]     #read y dimension of node
    dimensions=[x_dimension,y_dimension]
    
    landmarks[name]=dimensions

'''Creat a Vector'''
def vector_a_to_b(a,a_sign,b,b_sign,color):
    
    
    b=[-1*float(b[0])*10,-1*float(b[1])*10]     # =1 bec of slicer coordinate
    a=[-1*float(a[0])*10,-1*float(a[1])*10]
    
    
    head_length = -500
    
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    
    vec_ab = [dx,dy]
    
    vec_ab_magnitude = math.sqrt(dx**2+dy**2)

    dx = dx / vec_ab_magnitude
    dy = dy / vec_ab_magnitude
    
    vec_ab_magnitude = vec_ab_magnitude - head_length
    
    ax = plt.axes()
    
    c=ax.arrow(a[0], a[1], vec_ab_magnitude*dx, vec_ab_magnitude*dy, head_width=1, 
             head_length=-1500, fc='lightblue', ec=color)
    plt.scatter(a[0],a[1],color=color) # dot A color
    plt.scatter(b[0],b[1],color=color) # dot B color
    
    ax.annotate(a_sign, (a[0]+0.5,a[1]),fontsize=14, color=color) # mark A
    ax.annotate(b_sign, (b[0]+0.5,b[1]),fontsize=14, color=color) # mark B
    
    #plt.grid()
#    plt.xlim(0, 150)
#    plt.ylim(-150,0)
    return vec_ab

'''Call vector function'''  
dicom=pydicom.dcmread(file_dcm)
plt.imshow(dicom.pixel_array)

vec1=vector_a_to_b(landmarks['Node_1'],'A',landmarks['Node_0'],'B','red')
vec2=vector_a_to_b(landmarks['Node_1'],'A',landmarks['Node_2'],'C','red')
vec3=vector_a_to_b(landmarks['Node_1'],'A',landmarks['Node_3'],'D','red')

vec4=vector_a_to_b(landmarks['Node_4'],'E',landmarks['Node_5'],'F','white')
vec5=vector_a_to_b(landmarks['Node_0'],'B',landmarks['Node_2'],'C','white')


'''Calculate angel between two vectors'''
def angle(u,v):
    dot=0
    for i in range(len(u)):
        dot=dot+(float(u[i])*float(v[i]))

    u_magnitude = math.sqrt(u[0]**2+u[1]**2)
    v_magnitude = math.sqrt(v[0]**2+v[1]**2)
    
    return math.degrees(math.acos(dot/(u_magnitude*v_magnitude)))


'''Call angle function an print it'''
print('BAC:',angle(vec1,vec2))
print('BAD:',angle(vec1,vec3))
print('DAC:',angle(vec2,vec3))

print('BC-EF:',angle(vec5,vec4))

print('Bisector-AD:',abs((angle(vec1,vec2)/2)-angle(vec2,vec3)))



