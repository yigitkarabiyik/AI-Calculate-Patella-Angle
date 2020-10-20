# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:20:50 2020

@author: yigit
"""

from all_you_need import *

project_dir='C:/Users/yigit/OneDrive/Masaüstü/492/project_steps'
dir_fcsv=project_dir+'/fcsvs'

dir_xray_png=project_dir+'/7merchant_final_pngs'
dir_heatmap_png=project_dir+'/13heatmap_pngs'

dir_dcm=project_dir+'/8merchant_dicoms'

file='1.dcm'
file_name='1'

xray = Image.open(dir_xray_png+'/'+file_name+'.png')
heatmap= Image.open(dir_heatmap_png+'/'+file_name+'.png')

'''Get node_1 from landmark fcsv'''
landmarks=get_landmarks(file_name,dir_fcsv)

mydict=get_heatpoints_array(landmarks,dir_dcm+'/'+file, sigma=10)
for i in range(6):
    plt.axis('off')
    plt.imshow(mydict['Node_'+str(i)], cmap='plasma')
    plt.show()
    print(mydict['Node_'+str(i)].shape)