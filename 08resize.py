# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:59:17 2020

@author: yigit
"""

#Describe directories
project_dir='C:/Users/yigit/OneDrive/Masaüstü/492/project_steps'
dir_dataset=project_dir+'/mydataset_v4'

'''Load data from folder drive'''

#load data as npz
dataset_path= dir_dataset+'/mydataset_v4.2.128.npz'
mydataset=np.load(dataset_path)

#extract npz as input and output
myinput=mydataset['x']
myoutput=mydataset['y']

#check input and output on image
from scipy.ndimage import interpolation

plt.imshow(myinput[1,:,:], alpha=0.8, cmap='gray')
plt.imshow(myoutput[1,:,:,4], alpha=0.4, cmap='plasma')
plt.show()

print(myinput.shape)
print(myoutput.shape)

myinput_zoom=np.zeros((myinput.shape[0], 64, 64), dtype=np.float32)   #####
myoutput_zoom=np.zeros((myoutput.shape[0], 64, 64, 6), dtype=np.float32)  #####

for i in range(290):
  
  myinput_zoom[i,:,:]=interpolation.zoom(myinput[i,:,:], 0.5)
  for j in range(6):
    myoutput_zoom[i,:,:,j]=interpolation.zoom(myoutput[i,:,:,j], 0.5)




plt.imshow(myinput_zoom[1,:,:], alpha=0.8, cmap='gray')
plt.imshow(myoutput_zoom[1,:,:,4], alpha=0.4, cmap='plasma')
plt.show()

print(myinput_zoom.shape)
print(myoutput_zoom.shape)

'''Save resized dataset to google drive'''

#os.mkdir('/content/drive/My Drive/mydataset_v3_2')
croped_dataset_path=dir_dataset
np.savez(croped_dataset_path+'/mydataset_v4.2.64.npz', x=myinput_zoom, y=myoutput_zoom)