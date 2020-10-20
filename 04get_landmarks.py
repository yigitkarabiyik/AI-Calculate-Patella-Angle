# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:24:27 2020

@author: yigit
"""

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
