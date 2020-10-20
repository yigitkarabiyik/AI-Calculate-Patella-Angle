# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:28:48 2020

@author: yigit
"""

'''
This code do that save 6 heatmaps based on individual 
heatpoints to file
'''

from all_you_need import *

'''Take files from directory work on and save to another directory'''

project_dir='C:/Users/yigit/OneDrive/Masaüstü/project_steps'
dir_fcsv=project_dir+'/fcsvs'
dir_dcm=project_dir+'/8merchant_dicoms'

dir_heatpoints=project_dir+'/15heatpoints'

os.chdir(dir_dcm)
    
for file in os.listdir('.'):

    if file.endswith('.dcm'):
    
        file_name, file_extension= os.path.splitext(file)
                
        landmarks=get_landmarks(file_name,dir_fcsv)
        heatmap_dict = get_heatpoints_array(landmarks,dir_dcm+'/'+file)
        
        file_heatpoint = dir_heatpoints+'/heatpoints_pil_'+file_name
        os.mkdir(file_heatpoint)
        
        for i in range(6):

           #plt.axis('off')
#           plt.imshow(heatmap_array, cmap='plasma')
#            plt.imsave(file_heatpoint+'/'+file_name+'_node'+str(i+1)+'_heatpoint.png', heatmap_dict['Node_'+str(i)] ,cmap='plasma')
            #np.savez_compressed(file_heatpoint+'/'+file_name+'_node'+str(i+1)+'_heatpoint', hmap=np.float32(heatmap_dict['Node_'+str(i)]))
            
            hmap=Image.fromarray(heatmap_dict['Node_'+str(i)])
            hmap.save(file_heatpoint+'/'+file_name+'_node'+str(i+1)+'_heatpoint.png')
            
            