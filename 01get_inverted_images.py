# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:20:57 2020

@author: yigit
"""

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
   