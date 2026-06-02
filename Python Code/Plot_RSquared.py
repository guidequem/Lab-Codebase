import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
import Basic_Functions as bf
from tkinter import filedialog
from scipy.optimize import curve_fit

def rSquared(x,t,gamma,f):
    return (((f)**2) * (1/(t**4 + (gamma**2 - 2*t**2)*x**2 + x**4)) )

### Get Data ###
allData = bf.importData()

freq = np.array(allData[0])
rr = np.array(allData[1])
rr = rr*rr
xx = np.array(allData[2])
yy = np.array(allData[3])

### Truncate Data ###

response = input('Truncate Data?\n')
print(response.upper())
if 'Y' in response.upper():
    left = int(input('Left Frequency?\n'))
    print(str(np.where(freq==left)))
    leftN = int(np.where(freq==left)[0][0])
    right = int(input('Right Frequency?\n'))
    rightN = int(np.where(freq==right)[0][0])

    freq = freq[leftN:rightN]
    rr = rr[leftN:rightN]
    xx = xx[leftN:rightN]
    yy = yy[leftN:rightN]

### Find parameters ###
resonance = freq[np.where(rr==max(rr))[0][0]]
gamma = bf.rGamma(freq,rr)
print('\n'+str(resonance))
print('\n'+'Gamma: ' + str(gamma))

f = max(rr) * resonance**2 / gamma
print(str(max(rr)))

parsr,covr = curve_fit(f=rSquared, xdata=freq,ydata = rr,p0=[resonance,gamma,2000],bounds = (0,np.inf))


importantPars = parsr
print("Resonance Frequency = " + str(importantPars[0]) + "\nGamma = " +
      str(importantPars[1]) + "\nForce = " + str(importantPars[2]))
print("Possible Q-Value of : " + str(importantPars[0]/importantPars[1]))
print('Absorptive Peak = ' + str(max(yy)))
print('F/m = ' + str(importantPars[2]))


plt.plot(freq,rr,label='R-Squared')
plt.plot(freq,rSquared(freq,*importantPars),label='R-Squared Fit')

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (mV)")
plt.legend(loc='upper right')
plt.show()
