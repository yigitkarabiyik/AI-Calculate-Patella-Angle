# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:25:36 2020

@author: yigit
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:34:53 2020

@author: yigit
"""

"""
This code work on pngs
"""

import os
from all_you_need import *
from PIL import Image, ImageOps

project_dir='C:/Users/yigit/OneDrive/Masaüstü/project_steps'
dir_fcsv=project_dir+'/fcsvs'

dir_xray_png=project_dir+'/7merchant_final_pngs'
dir_heatpoints=project_dir+'/15heatpoints'

dir_dataset=project_dir+'/mydataset_v2'

xrays=os.listdir(dir_xray_png)
heatpoints=os.listdir(dir_heatpoints)



for file in xrays:
    
    file_name, file_extension= os.path.splitext(file)
    
    #images open
    xray = Image.open(dir_xray_png+'/'+file)
    heatpoints_list=[]
    for i in range(6):    
        heatpoints_path=dir_heatpoints+'/heatpoints_'+file_name
        heatmap= Image.open(heatpoints_path+'/'+file_name+'_node'+str(i+1)+'_heatpoint.png')
        heatpoints_list.append(heatmap)
        
    #select node_1 for center of the croped image
    '''Get node_1 from landmark fcsv'''
    landmarks=get_landmarks(file_name,dir_fcsv)
    
    x=-1*int(float(landmarks['Node_1'][0]))
    y=-1*int(float(landmarks['Node_1'][1]))
    
    cols, rows = xray.size
    
    #if image size smaller than we expected, adding border
    if x-512<0 or x+512>cols or y-768<0 or y+256>rows:
    
        '''Add border to image'''
        padding=768     # give size for margin
        
        #add image border
        xray_extended = ImageOps.expand(xray,border=padding,fill=38)    # 38 xray black
        heatpoints_extended=[]
        for i in range(6):
            heatmap_extended = ImageOps.expand(heatpoints_list[i],border=padding,fill='#0C0786')   # 0C0786 = plasma blue
            heatpoints_extended.append(heatmap_extended)                 
       
        x+=padding
        y+=padding
        
        #crope image
        xray_croped= xray_extended.crop((x-512,y-768,x+512,y+256))
        heatpoints_croped=[]
        for i in range(6):
            heatmap_croped= heatpoints_extended[i].crop((x-512,y-768,x+512,y+256))
            heatpoints_croped.append(heatmap_croped)
    else:
        
        #crope image
        xray_croped= xray.crop((x-512,y-768,x+512,y+256))
        heatpoints_croped=[]
        for i in range(6):    
            heatmap_croped= heatpoints_list[i].crop((x-512,y-768,x+512,y+256))
            heatpoints_croped.append(heatmap_croped)
    
    
    # write xray and heatmap path for data
    data_path = dir_dataset+'/data'+file_name
    data_xray_path = data_path+'/xray'
    data_heatmap_path = data_path+'/heatpoints'
    
    #creat xray directory
    os.makedirs(data_xray_path)
    
#    plt.axis('off')
    xray_croped.save(data_xray_path+'/'+file_name+'_croped_xray'+'.png')  
    
    os.mkdir(data_heatmap_path)
    
    for i in range(6):
        plt.axis('off')
        heatpoints_croped[i].save(data_heatmap_path+'/'+file_name+'_node'+str(i+1)+'_heatpoint_croped.png') 
    

