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
dir_heatmap_png=project_dir+'/13heatmap_pngs'

dir_dataset=project_dir+'/mydataset'

xrays=os.listdir(dir_xray_png)
heatmaps=os.listdir(dir_heatmap_png)


for file in xrays:
    
    file_name, file_extension= os.path.splitext(file)

    xray = Image.open(dir_xray_png+'/'+file)
    heatmap= Image.open(dir_heatmap_png+'/'+file)
    
    '''Get node_1 from landmark fcsv'''
    landmarks=get_landmarks(file_name,dir_fcsv)
    
    x=-1*int(float(landmarks['Node_1'][0]))
    y=-1*int(float(landmarks['Node_1'][1]))
    
    cols, rows = xray.size
    
    if x-512<0 or x+512>cols or y-762<0 or y+256>rows:
    
        '''Add border to image'''
        padding=768     # give size for margin
        
        xray_extended = ImageOps.expand(xray,border=padding,fill=38)    # 38 xray black
        heatmap_extended = ImageOps.expand(heatmap,border=padding,fill='#0C0786')   # 0C0786 = plasma blue
        
        x+=padding
        y+=padding
        
        xray_croped= xray_extended.crop((x-512,y-768,x+512,y+256))
        heatmap_croped= heatmap_extended.crop((x-512,y-768,x+512,y+256))
    
    else:
    
        xray_croped= xray.crop((x-512,y-768,x+512,y+256))
        heatmap_croped= heatmap.crop((x-512,y-768,x+512,y+256))
    
    # write xray and heatmap path for data
    data_path = dir_dataset+'/data'+file_name
    data_xray_path = data_path+'/xray'
    data_heatmap_path = data_path+'/heatmap'
    
    #creat xray directory
    os.makedirs(data_xray_path)
    
#    plt.axis('off')
    xray_croped.save(data_xray_path+'/'+file_name+'_croped_xray'+'.png')  
    
    os.mkdir(data_heatmap_path)
    
    plt.axis('off')
    heatmap_croped.save(data_heatmap_path+'/'+file_name+'_croped_heatmap'+'.png') 


