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
v_scan=list()
sqrt_vscan=list()
for i in range(1,3,1):
    v_scan.append((i))#10)
    sqrt_vscan.append(np.sqrt((i+1)))#10))
    temp = df['0.'+str((i))+'v'].values
    temp=np.delete(temp,0)
    temp=temp.astype('float64')    
    
    temp2 = df['0.'+str((i))+'i'].values
    temp2=np.delete(temp2,0)
    temp2=temp2.astype('float64')    
    v.append(temp)
    current.append(temp2)
min_i=list()
min_v = list()
max_i=list()
max_v=list()
for j in range(len(v)):
    min_i.append(np.min(current[j])) 
    min_v.append(v[j][np.where(current[j]==np.min(current[j]))][0]) 
    max_i.append(np.max(current[j])) 
    max_v.append(v[j][np.where(current[j]==np.max(current[j]))][0]) 
    
    
diff_maxvminv=list()
baseline=list()
for i in range(len(max_v)):
    diff_maxvminv.append((max_v[i]-min_v[i])*1000)
    baseline.append(59)
    
ratio_ipia =list()
ratio_baseline=list()
for i in range(len(max_i)):
    ratio_ipia.append(np.abs(max_i[i]/min_i[i]))
    ratio_baseline.append(1)
plt.scatter(sqrt_vscan,min_i)
plt.scatter(sqrt_vscan,max_i)
plt.plot(sqrt_vscan,min_i)
plt.plot(sqrt_vscan,max_i)

#plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)))

#plt.text(0.6, 0.5, 'R-squared = %0.2f' % r_squared)
plt.legend([r'$I_{p,c}$',r'$I_{p,a}$'],loc=2)
#plt.title(r' $I_p$ vs $\sqrt{\nu} $ at $c=3$M ')
plt.title(r' $I_p$ vs $\sqrt{\nu} $ at $c=4.7$M')
plt.ylabel(r'$I_p$(mA)')
plt.xlabel(r'$\sqrt{\nu}$')
plt.savefig('sqrt.png', dpi=600)

plt.show()
plt.scatter(v_scan,min_i)
plt.scatter(v_scan,max_i)
plt.plot(v_scan,min_i)
plt.plot(v_scan,max_i)

plt.legend([r'$I_{p,c}$',r'$I_{p,a}$'],loc=2)
#plt.title(r' $I_p$ vs $\sqrt{\nu} $ at $c=3$M ')
plt.title(r' $I_p$ vs $\nu $ at $c=4.7$M')
plt.ylabel(r'$I_p$(mA)')
plt.xlabel(r'$\nu$')

plt.savefig('normal.png', dpi=500)
plt.show()

#no3 test
plt.scatter(v_scan,ratio_ipia)
plt.plot(v_scan,ratio_ipia)
plt.title("Peak Current Ratio")
plt.ylabel(r'|$I_{p,a}/I_{p,c}$|')
plt.xlabel(r'$\nu$  $(mVs^{-1})$')
plt.savefig('3 ratio_ip_ia.png', dpi=500)
plt.show()
#no1 test
plt.scatter(v_scan,diff_maxvminv)
plt.plot(v_scan,diff_maxvminv)
plt.plot(v_scan,baseline)
plt.title(r'$\Delta E_p$=$E_{p}^{a} -$$E_{p}^{c}$')
plt.ylabel(r'$E_{p}^{a}-E_{p}^{c}$ (mV)')
plt.xlabel(r'$\nu$  $(mVs^{-1})$')
plt.savefig('1 delta_ep.png', dpi=500)
plt.show()
# no.5 test
plt.scatter(v_scan,min_v)
plt.scatter(v_scan,max_v)
plt.plot(v_scan,min_v)
plt.plot(v_scan,max_v)
#plt.plot(np.unique(min_v), np.poly1d(np.polyfit(v_scan, min_v, 1))(np.unique(min_v)))
#plt.plot(np.unique(max_v), np.poly1d(np.polyfit(v_scan, max_v, 1))(np.unique(max_v)))

plt.legend([r'$E_{p,c}$',r'$E_{p,a}$'])
plt.title(r'Dependency of $E_p$ to $\nu$')
plt.ylabel(r'$E_p$ V')
plt.xlabel(r'$\nu$  $(mVs^{-1})$')

plt.savefig('5 scanrate_dependency.png', dpi=500)
plt.show()