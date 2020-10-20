# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:17:22 2020

@author: yigit
"""



from all_you_need import *

from numpy import asarray
from numpy import savetxt

'''Take files from directory work on and save to another directory'''

project_dir='C:/Users/yigit/OneDrive/Masaüstü/project_steps'
dir_fcsv=project_dir+'/fcsvs'
dir_dcm=project_dir+'/8merchant_dicoms'

dir_heatmap_png=project_dir+'/13heatmap_pngs'

os.chdir(dir_dcm)
    
for file in os.listdir('.'):

    if file.endswith('.dcm'):
    
        file_name, file_extension= os.path.splitext(file)
                
        landmarks=get_landmarks(dir_fcsv+'/'+file_name+'.fcsv')
        heatmap_array = get_heatmap_array(landmarks,dir_dcm+'/'+file)
        
        plt.axis('off')
#        plt.imshow(heatmap_array, cmap='plasma')
        
        plt.imsave(dir_heatmap_png+'/'+file_name+'.png', heatmap_array ,cmap='plasma')
                
                
        
