# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:25:11 2020

@author: yigit
"""

def get_heatpoints_array(landmarks, file_dcm, sigma=30):
    
    # Import image and get x and y extents
    merchant_dicom=pydicom.dcmread(file_dcm)
    I = merchant_dicom.pixel_array
    p = np.asarray(I).astype('int')
    
    I = skimage.color.rgb2gray(I)
    
    w, h = I.shape
    y, x = np.mgrid[0:w, 0:h]   
    
    g_array=np.zeros(shape=(w,h))
    
    heatmap_dict={}
    
    for i in range(6):
        
        a=landmarks['Node_'+str(i)]
        
        a=[-1*float(a[0])*1,-1*float(a[1])*1]
        xo=a[0]
        yo=a[1]

        r= 1./(2*(sigma**2))
        g = np.exp( - (r*((x-xo)**2) + r*((y-yo)**2)))
        
        heatmap_dict['Node_'+str(i)]=np.float32(g)
        
    return heatmap_dict