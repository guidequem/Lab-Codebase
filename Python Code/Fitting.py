import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
import Basic_Functions as bf
from tkinter import filedialog
from scipy.optimize import curve_fit

def elastic(x,t,gamma,f,m):
    return (f/m)*((t**2)-(x**2))/((((t**2)-(x**2))**2)+(gamma**2)*(x**2))

def absorb(x,t,gamma,f,m):
    return (f/m)*(gamma*x)/((((t**2)-(x**2))**2)+(gamma**2)*(x**2))

def rSquared(x,t,gamma,f,m):
    return ((f**2)/(m**2)) * 1/(t**4 - 2*(t*x)**2 + (gamma*x)**2 + x**4)

### Get Data ###
allData = bf.importData()

freq = np.array(allData[0])
rr = np.array(allData[1])
xx = np.array(allData[2])
yy = np.array(allData[3])

### Get bounds for fitting and subtract linear background noise ###
bounds = bf.getLinearBounds()
xx = bf.linearBackground(freq,xx,bounds)
yy = bf.linearBackground(freq,yy,bounds)
rr = bf.linearBackground(freq,rr,bounds)

### Get bounds for plotting over and analysis ###
leftW = int(input('Leftmost Frequency to analyze?\n'))
rightW = int(input('Rightmost Frequency to analyze? 0 if all data.\n'))


### Shorten data ###
leftI = np.where(freq==leftW)[0][0]

if rightW == 0:
    rightI = len(freq)
else:
    rightI = np.where(freq==rightW)[0][0]

freq = freq[leftI:rightI]
xx = xx[leftI:rightI]
yy = yy[leftI:rightI]
rr = rr[leftI:rightI]

### Find parameters ###
gamma = bf.findGamma(freq,yy,xx)[0]
resonance = freq[np.where(yy==max(yy))[0][0]]
print('\n'+str(resonance))
print(str(gamma))

rs = bf.getRSquared(xx,yy)

parsx,covx = curve_fit(f=elastic,xdata = freq,ydata = xx,p0=[resonance-5,gamma-1,0,0],bounds = (0,np.inf))
parsy,covy = curve_fit(f=absorb,xdata = freq,ydata = yy,p0=[resonance-5,gamma-1,0,0],bounds = (0,np.inf))
parsr,covr = curve_fit(f=rSquared, xdata=freq,ydata = rs,p0=[resonance,gamma,0,0],bounds = (0,np.inf))


importantPars = parsx
print("Resonance Frequency = " + str(importantPars[0]) + "\nGamma = " +
      str(importantPars[1]) + "\nForce = " + str(importantPars[2]) + "\nMass = " + str(importantPars[3]))
print("Possible Q-Value of : " + str(importantPars[0]/importantPars[1]))
print('Absorptive Peak = ' + str(max(yy)))
print('F/m = ' + str(importantPars[2]/importantPars[3]))


plt.plot(freq,yy,label='Absorptive')
plt.plot(freq,xx,label='Elastic')
plt.plot(freq,elastic(freq,*importantPars),label='Elastic Fit')
plt.plot(freq,absorb(freq,*importantPars),label='Absorptive Fit')

'''
plt.plot(freq,rs,label='R-Squared')
plt.plot(freq,rSquared(freq,*importantPars),label='R-Squared Fit')
'''
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper right')
plt.show()



