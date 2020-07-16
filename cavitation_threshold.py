# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:24:20 2020

@author: Paul Vincent Nonat
"""

import numpy as np
import matplotlib.pyplot as plt 

p_inf=101325
rho=8635
trans_freq=np.array([36,42,83,74,150,300]) # frequency in Hz
r_bubble=np.array([10,20,30,40,50,60,70,80,90,100]) #bubble radius in micro meter
tresh_pres= np.zeros((trans_freq.size,r_bubble.size))
def bubble_func(rt,f):
    increment=0.00001 #p value increment
    rt= rt*0.0000010000
    p=1
    test=0
    while p<=11:
        test=(0.13/f)*np.sqrt(p_inf/rho)*(((p-1)/np.sqrt(p))*np.cbrt(1+ ((2/3)*(p-1))))
        #print(test)
        if (np.abs((rt-test)/rt))<=0.01:
            print()
            print("Estimated Error:",((rt-test)/rt))
            print("P seach successfully")
            print(p)
            print()
            print(r'$P_t=$',(p*p_inf))
            return p*p_inf;
        if  (np.abs((rt-test)/rt))>0.01:
            p= p+increment
            test=0
            print("Testing another p")
        if p==11:
            print(" P must be greater than 11")
            test=0
            p=p+increment
        print(p)
            
    if (np.abs((rt-test)/rt))>0.01:
        while (np.abs((rt-test)/rt))>0.01:
            test=(0.13/f)*np.sqrt(p_inf/rho)*np.sqrt((2/3)*(p-1))
            #print(test)
            if (np.abs((rt-test)/rt))<=0.01:
                print()
                print("Estimated Error:",((rt-test)/rt))
                print("P seach successfully")
                print(p)
                print()
                return p*p_inf;
            if (np.abs((rt-test)/rt))>0.01:
                p= p+increment
                test=0
                print("Testing another p")
            print(p)    
            
for x in range(trans_freq.size):
    for y in range(r_bubble.size):
        print("Calculating bubble size=",r_bubble[y],"um at f=",trans_freq[x],"kHz")
        tresh_pres[x][y]=bubble_func(r_bubble[y],trans_freq[x]*1000)