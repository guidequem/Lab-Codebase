import numpy as np
import scipy.stats as scp
import matplotlib.pyplot as plt
import math
V = np.array([.70,.940,1.37,1.80,2.03,2.60])
f = np.array([1000,2000,5000,10000,15000,30000])
I = np.array([60.81,63.07,56.03,49.10,44.32,35.27])*0.001
figure = plt.figure()
x = np.power((2*np.pi*f),2)
print(x)
y = np.power((V/I),2)
print(y)
slope, intercept, r, p, se = scp.linregress(x,y)
print("inductance:",math.sqrt(slope))
print("resistance:",math.sqrt(intercept))
xs=np.linspace(min(x),max(x),1000)
ys=slope*xs+intercept
plt.plot(xs,ys,color='r')
plt.plot(x,y)
plt.savefig("C:\\Users\\markertlab\\Desktop\\MagnetScans\\curve.png")
plt.show()

