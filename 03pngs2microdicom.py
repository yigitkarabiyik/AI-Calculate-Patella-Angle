# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:23:33 2020

@author: yigit
"""

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
  