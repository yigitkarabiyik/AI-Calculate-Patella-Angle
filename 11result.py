# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 08:46:53 2020

@author: yigit
"""

import numpy as np 
from all_you_need import *
from matplotlib import image
import random
import math

#Describe directories
project_dir='C:/Users/yigit/OneDrive/Masaüstü/492/project_steps'
npz_file='C:/Users/yigit/OneDrive/Masaüstü/492/project_steps/myresult_v4/myresult_v4.2.64.npz'
original= 'C:/Users/yigit/OneDrive/Masaüstü/492/project_steps/mydataset_v4/mydataset_v4.2.64.npz'
#Load orginal dataset
mydataset= np.load(original)
myinput = mydataset['x']
myoutput = mydataset['y']
#Load model output
result = np.load(npz_file)
train = result['train']
test = result['test']

test_number=int(len(myoutput)/5) # 58
train_number=int(len(myoutput)*(4/5))    # 232

distance_array=np.zeros((290,6))
for data in range(len(myoutput)):

    if data < len(test):
        for heat in range(0,6):
            
            row, col = np.where(test[data,:,:,heat]== np.max(test[data,:,:,heat]))
            row_ori, col_ori = np.where(myoutput[data,:,:,heat] == np.max(myoutput[data,:,:,heat]))
            distance = math.sqrt(((row-row_ori)**2)+((col-col_ori)**2))
            distance_array[data][heat]=distance    
    else:
        for heat in range(0,6):
            
            row, col = np.where(train[data-len(test),:,:,heat]== np.max(train[data-len(test),:,:,heat]))
            row_ori, col_ori = np.where(myoutput[data,:,:,heat] == np.max(myoutput[data,:,:,heat]))
            
            distance = math.sqrt((row-row_ori)**2+(col-col_ori)**2)
            distance_array[data][heat]=distance
