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

ypc0=df['ipc0'].values
ypc0=np.delete(ypc0,0)
ypc0=ypc0.astype('float64')

ypc1=df['ipc1'].values
ypc1=np.delete(ypc1,0)
ypc1=ypc1.astype('float64')

ypc2=df['ipc2'].values
ypc2=np.delete(ypc2,0)
ypc2=ypc2.astype('float64')

ypc3=df['ipc3'].values
ypc3=np.delete(ypc3,0)
ypc3=ypc3.astype('float64')

ypc4=df['ipc4'].values
ypc4=np.delete(ypc4,0)
ypc4=ypc4.astype('float64')

ypc5=df['ipc5'].values
ypc5=np.delete(ypc5,0)
ypc5=ypc5.astype('float64')

ypc6=df['ipc6'].values
ypc6=np.delete(ypc6,0)
ypc6=ypc6.astype('float64')


ypc7=df['ipc7'].values
ypc7=np.delete(ypc7,0)
ypc7=ypc7.astype('float64')

ypc8=df['ipc8'].values
ypc8=np.delete(ypc8,0)
ypc8=ypc8.astype('float64')

ypc9=df['ipc9'].values
ypc9=np.delete(ypc9,0)
ypc9=ypc9.astype('float64')

ypc10=df['ipc10'].values
ypc10=np.delete(ypc10,0)
ypc10=ypc10.astype('float64')


plt.scatter(x,ypc0)
plt.scatter(x,ypc1)
plt.scatter(x,ypc2)
plt.scatter(x,ypc3)
plt.scatter(x,ypc4)
plt.scatter(x,ypc5)
plt.scatter(x,ypc6)
plt.scatter(x,ypc7)
plt.scatter(x,ypc8)
plt.scatter(x,ypc9)
plt.scatter(x,ypc10)

plt.plot(x,ypc0)
plt.plot(x,ypc1)
plt.plot(x,ypc2)
plt.plot(x,ypc3)
plt.plot(x,ypc4)
plt.plot(x,ypc5)
plt.plot(x,ypc6)
plt.plot(x,ypc7)
plt.plot(x,ypc8)
plt.plot(x,ypc9)
plt.plot(x,ypc10)

plt.legend([r'$\omega=0$',r'$\omega=1000$',r'$\omega=2000$',r'$\omega=3000$',r'$\omega=4000$',r'$\omega=5000$',r'$\omega=6000$',r'$\omega=7000$',r'$\omega=8000$',r'$\omega=9000$',r'$\omega=10000$'],loc=3)
plt.title(r' $I_{p,c}$ vs $\nu $ at $\omega=10000\ RPM $ ')
plt.ylabel(r'$I_{p,c}$(A)')
plt.xlabel(r'$\nu $')

plt.savefig('all_ipc.png', dpi=600)

plt.show()
plt.scatter(x1,ypc0)
plt.scatter(x1,ypc1)
plt.scatter(x1,ypc2)
plt.scatter(x1,ypc3)
plt.scatter(x1,ypc4)
plt.scatter(x1,ypc5)
plt.scatter(x1,ypc6)
plt.scatter(x1,ypc7)
plt.scatter(x1,ypc8)
plt.scatter(x1,ypc9)
plt.scatter(x1,ypc10)

plt.plot(x1,ypc0)
plt.plot(x1,ypc1)
plt.plot(x1,ypc2)
plt.plot(x1,ypc3)
plt.plot(x1,ypc4)
plt.plot(x1,ypc5)
plt.plot(x1,ypc6)
plt.plot(x1,ypc7)
plt.plot(x1,ypc8)
plt.plot(x1,ypc9)
plt.plot(x1,ypc10)

plt.legend([r'$\omega=0$',r'$\omega=1000$',r'$\omega=2000$',r'$\omega=3000$',r'$\omega=4000$',r'$\omega=5000$',r'$\omega=6000$',r'$\omega=7000$',r'$\omega=8000$',r'$\omega=9000$',r'$\omega=10000$'],loc=3)
plt.title(r' $I_{p,c}$ vs $\sqrt{\nu} $ at $\omega=10000\ RPM $ ')
plt.ylabel(r'$I_{p,c}$(A)')
plt.xlabel(r'$\sqrt{\nu} $')

plt.savefig('all_ipc-sqrt.png', dpi=600)

plt.show()

