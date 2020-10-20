# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:20:50 2020

@author: yigit
"""

from all_you_need import *

from matplotlib import image

#Describe directories
project_dir='C:/Users/yigit/OneDrive/Masaüstü/project_steps'
dir_fcsv=project_dir+'/fcsvs'

dir_xray_png=project_dir+'/7merchant_final_pngs'
dir_dcm=project_dir+'/8merchant_dicoms'
dir_heatmap_png=project_dir+'/13heatmap_pngs'

dir_dataset=project_dir+'/mydataset_v2'
########################

#Describe file id
file_id='103_left'
#########################

#Describe file paths
path_xray_png=dir_xray_png+'/'+file_id+'.png'
path_dcm=dir_dcm+'/'+file_id+'.dcm'
#########################

#Describe input and output as zeros
myinput=np.zeros((145,1024,1024), dtype=np.float32)
myoutput=np.zeros((145,1024,1204,6), dtype=np.float32)
#########################

#xrays=os.listdir(dir_xray_png)
#
#for xray in xrays:
#    path_xray_png=dir_xray_png+'/'+xray
#    
#    xray=image.imread(path_xray_png)
#    xray=np.float32(xray)

#read xray as float32
xray=image.imread(path_xray_png)
xray=np.float32(xray)

#get landmark
landmarks=get_landmarks(file_id,dir_fcsv)

#generate heatmap as float32
heatpoints=get_heatpoints_array(landmarks,path_dcm)


#find node1
x=-1*int(float(landmarks['Node_1'][0]))
y=-1*int(float(landmarks['Node_1'][1]))

cols, rows = xray.shape

mydata=0
    
#if array size smaller than we expected, adding border
if x-512<0 or x+512>rows or y-768<0 or y+256>cols:

    '''Add border to image'''
    padding=768     # give size for margin
    
    x+=padding
    y+=padding
    
    #add border to xray array
    xray_extended = np.pad(xray, pad_width=768, mode='constant', constant_values=0)
    #crope knee
    xray_croped= xray_extended[y-768:y+256,x-512:x+512]
    #write xray in to input array
    myinput[mydata]=xray_croped
    
    #add border to heatpoints
    heatpoints_extended=[]
    for i in range(6):
        heatmap_extended = np.pad(heatpoints['Node_'+str(i)], pad_width=768,
                                             mode='constant', constant_values=0)   # 0C0786 = plasma blue
        heatpoints_extended.append(heatmap_extended)                 
   
    heatpoints_croped=np.zeros((1024,1024,6), dtype=np.float32)
    
    for i in range(6):
        heatmap_croped= heatpoints_extended[i][y-768:y+256,x-512:x+512]
        heatpoints_croped[:,:,i]=heatmap_croped[:,:]
    
    #write heatmaps in to output array
    myoutput[mydata,0:1024,0:1024,0:6]=heatpoints_croped
else:
    
    #crope xray array
    xray_croped= xray[y-768:y+256,x-512:x+512]
    #write xray in to input array
    myinput[mydata]=xray_croped
    
    #crope heatpoints
    heatpoints_croped=np.zeros((1024,1024,6), dtype=np.float32)
    for i in range(6):
        heatmap_croped= heatpoints_extended[i][y-768:y+256,x-512:x+512]
        heatpoints_croped[:,:,i]=heatmap_croped[:,:]
    
    #write heatmaps in to output array
    myoutput[mydata,0:1024,0:1024,0:6]=heatpoints_croped








