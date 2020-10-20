# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:22:11 2020

@author: yigit
"""

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
