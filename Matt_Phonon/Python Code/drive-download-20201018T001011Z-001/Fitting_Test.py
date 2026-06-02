import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
import Basic_Functions as bf
from tkinter import filedialog
from scipy.optimize import curve_fit

def absorb(x,t,gamma,f,m):
    return (f/m)*((t**2)-(x**2))/((((t**2)-(x**2))**2)+(gamma**2)*(x**2))

def elastic(x,t,gamma,f,m):
    return (f/m)*(gamma*x)/((((t**2)-(x**2))**2)+(gamma**2)*(x**2))

def rSquared(x,t,gamma,f,m):
    return (absorb(x,t,gamma,f,m)**2 + elastic(x,t,gamma,f,m)**2)**(1/2)

allData = bf.importData()

freq = np.array(allData[0])
rr = np.array(allData[1])
xx = np.array(allData[2])
yy = np.array(allData[3])

xx = np.array(bf.normalize(freq,xx,'x'))
yy = np.array(bf.normalize(freq,yy,'y'))
rr = np.array(bf.normalize(freq,yy,'r'))

'''
for n in range(0,50):
    if n == 0:
        parsx,covx = curve_fit(f=absorb,xdata = freq,ydata = xx,p0=[2100,0,0,0],bounds = (0,np.inf))
    parsy,covy = curve_fit(f=elastic,xdata = freq,ydata = yy,p0=parsx,bounds = (0,np.inf))
    parsx,covx = curve_fit(f=absorb,xdata = freq,ydata = xx,p0=parsy,bounds = (0,np.inf))
'''
parsx,covx = curve_fit(f=absorb,xdata = freq,ydata = xx,p0=[2100,0,0,0],bounds = (0,np.inf))
parsr,covr = curve_fit(f=rSquared,xdata = freq,ydata = rr,p0=parsx,bounds = (0,np.inf))

print(str(parsx))
print(str(parsr))
print(str(rr[0]))
plt.plot(freq,rSquared(freq,*parsr))
plt.plot(freq,rr,'r-')
plt.show()



