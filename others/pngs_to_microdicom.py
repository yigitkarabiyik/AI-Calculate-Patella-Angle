# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:35:03 2020

@author: yigit
"""

import subprocess
import os
import time

import pyautogui

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
        
#        pyautogui.hotkey('alt','f4')
#        time.sleep(2)






#command='asdf'
#
##os.system(command)
#baby=subprocess.Popen('C:/Program Files/MicroDicom/mDicom.exe'
#                      ,stdin=PIPE)


