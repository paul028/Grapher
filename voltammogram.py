# -*- coding: utf-8 -*-
"""
Created on Fri May 22 01:56:23 2020

@author: Paul Vincent Nonat
"""

import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
df = pd.read_csv('cv_comparison_egan.csv')
print (df)
v=list()
current=list()

x=df['v_egan'].values
x=np.delete(x,0)
x=x.astype('float64')

y=df['i_egan'].values
y=np.delete(y,0)
y=y.astype('float64')

x_ours=df['v_egan_sound'].values
x_ours=np.delete(x_ours,0)
x_ours=x_ours.astype('float64')

y_ours=df['i_egan_sound'].values
y_ours=np.delete(y_ours,0)
y_ours=y_ours.astype('float64')








#plt.scatter(x,y)
plt.plot(x,y)
#plt.scatter(x_ours,y_ours)
plt.plot(x_ours,y_ours)
plt.legend([r'Baseline w/o Ultrasound','w/ Ultrasound $f= 60 kHz$'],loc=2)
#plt.title(r' $I_p$ vs $\sqrt{\nu} $ at $c=3$M ')
plt.title(r'Voltammogram Comparison at $c=4.7M$')
plt.ylabel(r'Current Density $ mA/cm^2$')
#plt.xlabel(r'$\sqrt{\nu} $ $(mVs^{-1})} $') #squareroot
plt.xlabel(r'Electric Potential vs SCE $(V)$')


plt.savefig('Voltammogram Comparison.png', dpi=600)
plt.show()