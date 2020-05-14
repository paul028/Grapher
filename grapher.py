import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
headers = ['v_scan','sqrt_vscan','ipc0','ipa0','ipc1','ipa1','ipc2','ipa2','ipc3','ipa3','ipc4','ipa4','ipc5','ipa5','ipc6','ipa6','ipc7','ipa7','ipc8','ipa8','ipc9','ipa9','ipc10','ipa10']
df = pd.read_csv('05-13-2020 PBO2 0-1000RPM 0.01-0.1 scanrate 2M H2SO4.csv',names=headers)
print (df)

x1=df['sqrt_vscan'].values
x1=np.delete(x1,0)
x1=x1.astype('float64')

x=df['v_scan'].values
x=np.delete(x,0)
x=x.astype('float64')

ypc0=df['ipc10'].values
ypc0=np.delete(ypc0,0)
ypc0=ypc0.astype('float64')

ypa0=df['ipa10'].values
ypa0=np.delete(ypa0,0)
ypa0=ypa0.astype('float64')

ypa0
ypc0







plt.scatter(x,ypc0)
plt.scatter(x,ypa0)
plt.plot(x,ypc0)
plt.plot(x,ypa0)
plt.legend([r'$I_{p,c}$',r'$I_{p,a}$'],loc=2)
#plt.title(r' $I_p$ vs $\sqrt{\nu} $ at $c=3$M ')
plt.title(r' $I_p$ vs $\nu $ at $c=2$M & $\omega=10000$RPM')
plt.ylabel(r'$I_p$(A)')
#plt.xlabel(r'$\sqrt{\nu} $ $(mVs^{-1})} $') #squareroot
plt.xlabel(r'$\nu $ $(mVs^{-1})} $')


plt.savefig('10000RPM-normal.png', dpi=600)
plt.show()
plt.scatter(x1,ypc0)
plt.scatter(x1,ypa0)
plt.plot(x1,ypc0)
plt.plot(x1,ypa0)
plt.legend([r'$I_{p,c}$',r'$I_{p,a}$'],loc=2)
#plt.title(r' $I_p$ vs $\sqrt{\nu} $ at $c=3$M ')
plt.title(r' $I_p$ vs $\sqrt{\nu} $ at $c=2$M & $\omega=10000$RPM')
plt.ylabel(r'$I_p$(A)')
#plt.xlabel(r'$\sqrt{\nu} $ $(mVs^{-1})} $') #squareroot
plt.xlabel(r'$\sqrt{\nu} $ $(mVs^{-1})} $')


plt.savefig('10000RPM.png', dpi=600)