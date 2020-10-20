# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 15:47:50 2020

@author: yigit
"""

from all_you_need import *



import numpy as np 

#Describe directories
project_dir='C:/Users/yigit/OneDrive/Masaüstü/492/project_steps'
dir_fcsv=project_dir+'/fcsvs'
npz_file='C:/Users/yigit/OneDrive/Masaüstü/492/project_steps/mydataset_v4/mydataset_v4.npz'
dir_dataset=project_dir+'/mydataset_v4'

dataset = np.load(npz_file)

xrays = dataset['x']

heatmaps = dataset['y']

mirror_array=np.zeros((145,1024,1024), dtype=np.float32)

for i in range(np.shape(xrays)[0]):
    
    xray=xrays[i,:,:]
    mirror=np.flip(xray,1)
    
    mirror_array[i,:,:]=mirror
    

heatmap_array=np.zeros((145,1024,1024,6), dtype=np.float32)

for i in range(np.shape(heatmaps)[0]):
    for j in range(np.shape(heatmaps)[3]):
        
        heatmap= heatmaps[i,:,:,j]
        mirror_h=np.flip(heatmap,1)
        
        heatmap_array[i,:,:,j]=mirror_h[:,:]
     
myoutput=np.zeros((290,1024,1024,6), dtype=np.float32)

for i in range(145):
    for j in range(6):
    
        myoutput[i,:,:,j]=heatmaps[i,:,:,j]
    
for i,n in zip(range(145),range(145,291)):
    for j in range(6):
        
        myoutput[n,:,:,j]=heatmap_array[i,:,:,j]
    
np.savez(dir_dataset+'/mydataset_v4.2.npz',x=myinput, y=myoutput)