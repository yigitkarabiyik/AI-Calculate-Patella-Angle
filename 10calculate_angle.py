# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:32:37 2020

@author: yigit
"""

'''Calculate angel between two vectors'''
def angle(u,v):
    dot=0
    for i in range(len(u)):
        dot=dot+(float(u[i])*float(v[i]))

    u_magnitude = math.sqrt(u[0]**2+u[1]**2)
    v_magnitude = math.sqrt(v[0]**2+v[1]**2)
    
    return math.degrees(math.acos(dot/(u_magnitude*v_magnitude)))


'''Call angle function an print it'''
print('BAC:',angle(vec1,vec2))
print('BAD:',angle(vec1,vec3))
print('DAC:',angle(vec2,vec3))

print('BC-EF:',angle(vec5,vec4))

print('Bisector-AD:',abs((angle(vec1,vec2)/2)-angle(vec2,vec3)))