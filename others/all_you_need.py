# -*- coding: utf-8 -*-
"""
Created on Wed May 13 01:36:02 2020

@author: yigit

THIS MODULE INCLUDES THIS FUNCTIONS:
    dicom_show
    get_inverted_images
    eliminate_images
    pngs2microdicom
    get_landmarks

"""


import matplotlib.pyplot as plt
import numpy as np
import pydicom

from PIL import Image, ImageOps
import os

import time
import pyautogui

import skimage
from skimage.color import rgb2gray

'''Open dicom pixel array'''
def get_dicom_pixels(dicom_file):
    merchant_dicom=pydicom.dcmread(dicom_file)
    return merchant_dicom.pixel_array

"""Show dicom image and if there is anotation"""
def dicom_show(dicom_file,anotation_file=''):
    
    merchant_dicom=pydicom.dcmread(dicom_file)
    
    plt.imshow(merchant_dicom.pixel_array)
    plt.show()
    if anotation_file!='':
        anotation=pydicom.dcmread(anotation_file)
        plt.imshow(anotation.overlay_array(0x6000))


'''Save inverte of image with sequently name'''
def get_inverted_images(images_path,new_path):
    
    current_directory = os.getcwd()
    os.chdir(file_path)
    
    #current_directory_list=os.listdir()
    
    i=0
    for file in os.listdir('.'):    # list current directory
        if file.endswith('.png'):   # if end of file is .png
            image = Image.open(file)       # open png
            
            inverted_image = ImageOps.invert(image)  # invert image 
            
    #        file_name, file_extension = os.path.splitext(file)
            i+=1
            file_name=str(i)    #creat filename starting from 1.png
            
            inverted_image.save(new_path+'/{}.png'.format(file_name))
       
        
'''Eliminate image into two pices'''
def eliminate_images(images_path,new_path):
    os.chdir(images_path)
    
    for file in os.listdir('.'):
        if file.endswith('.png'):
            image=Image.open(file)
            
            file_name, file_extension= os.path.splitext(file)
            
            width, height = image.size
            half_width=int(width/2)
    
            # Calculate: (top left paint, right bottom point)
            image_left=image.crop((0,0,half_width,height))      # crap image
            image_right=image.crop((half_width,0,width,height))
            
            
            
            image_left.save(new_path+'/{}.png'.format(file_name+'_left'))
            image_right.save(new_path+'/{}.png'.format(file_name+'_right'))


'''Send to pngs to microdicom and convert to dicom type'''
#you should be sure microdicoms behavior 
def pngs2microdicom(pngs_file,save_file):
    
    os.chdir(pngs_file)
    
    micro_dicom=os.startfile('C:/Program Files/MicroDicom/mDicom.exe')
    time.sleep(2)
    
    for file in os.listdir('.'):
        if file.endswith('.png'):
            
            file_name, file_extension= os.path.splitext(file)
              
            pyautogui.hotkey('ctrl','o')
            time.sleep(1)
            pyautogui.write(file_name+'.png')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.hotkey('ctrl','alt','d')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(2)
            
            pyautogui.hotkey('alt','tab')
            time.sleep(1)
  
'''Creat Landmark Dictionary from fcsv for single file'''
def get_landmarks(file_name, fcsv_dir):
    # Read .fcsv file line by line
    with open(fcsv_dir+'/'+file_name+'.fcsv') as f:
        landmark_file=f.readlines()
        
    landmark_file=landmark_file[3:] # get ride of unneccessary lines    
    #Dictionary part
    landmarks={}
    for line in landmark_file:
        splited_line=line.split(',') #split 
        
        name=splited_line[0][22:30]     #read name of node as 'Node_0'
        x_dimension=splited_line[1]     #read x dimension of node
        y_dimension=splited_line[2]     #read y dimension of node
        dimensions=[x_dimension,y_dimension]
        
        landmarks[name]=dimensions
    return landmarks          


'''Generate heatmap array from landmarks for single file'''
# you have to multiply by 10 at a (158) line if work on dicom else multiply by 1
def get_heatmap_array(landmarks, file_dcm, sigma=15):
    
    # Import image and get x and y extents
    merchant_dicom=pydicom.dcmread(file_dcm)
    I = merchant_dicom.pixel_array
    p = np.asarray(I).astype('int')
    
    I = skimage.color.rgb2gray(I)
    
    w, h = I.shape
    y, x = np.mgrid[0:w, 0:h]   
    
    g_array=np.zeros(shape=(w,h))
    
    for i in range(6):
        a=landmarks['Node_'+str(i)]
    
        a=[-1*float(a[0])*1,-1*float(a[1])*1]
        xo=a[0]
        yo=a[1]
        
        r = 1./(2*sigma**2) + 1./(2*sigma**2)
        g = np.exp( - (r*((x-xo)**2) + r*((y-yo)**2)))
        
        for i in range(g.shape[0]):
            for j in range(g.shape[1]):
                if g[i][j]>=g_array[i][j]:
                    g_array[i][j]=g[i][j]
        
    return g_array

def get_heatpoints_array(landmarks, file_dcm, sigma=10):
    
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