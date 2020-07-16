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
df = pd.read_csv('cv_val_001square.csv')
print (df)
v=list()
current=list()

x=df['v'].values
x=np.delete(x,0)
x=x.astype('float64')

y=df['i'].values
y=np.delete(y,0)
y=y.astype('float64')

x_ours=df['ov'].values
x_ours=np.delete(x_ours,0)
x_ours=x_ours.astype('float64')

y_ours=df['oi'].values
y_ours=np.delete(y_ours,0)
y_ours=y_ours.astype('float64')

x_s=df['sv'].values
x_s=np.delete(x_s,0)
x_s=x_s.astype('float64')

y_s=df['si'].values
y_s=np.delete(y_s,0)
y_s=y_s.astype('float64')






#plt.scatter(x,y)
plt.plot(x,y)
#plt.scatter(x_ours,y_ours)
plt.plot(x_ours,y_ours)

plt.plot(x_s,y_s)
plt.legend([r'CV-VAL-001','ours','CV-VAL-001Square'],loc=2)
#plt.title(r' $I_p$ vs $\sqrt{\nu} $ at $c=3$M ')
plt.title(r'Comparison to Our Model')
plt.ylabel(r'Current Density $ mA/cm^2$')
#plt.xlabel(r'$\sqrt{\nu} $ $(mVs^{-1})} $') #squareroot
plt.xlabel(r'Electric Potential vs SCE $(V)$')


plt.savefig('CV-VAL-003.png', dpi=600)
plt.show()