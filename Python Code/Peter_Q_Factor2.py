import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
import Basic_Functions as bf
from tkinter import filedialog
from scipy.optimize import curve_fit
allData = bf.importData()

freq = np.array(allData[0])
rr = np.array(allData[1])
xx = np.array(allData[2])
yy = np.array(allData[3])
tt = np.array(allData[4])

bounds = bf.getLinearBounds()
xx = bf.linearBackground(freq,xx,bounds)
yy = bf.linearBackground(freq,yy,bounds)
rr = bf.linearBackground(freq,rr,bounds)

newRSquared = []

for i in range(0,len(xx)):
    newRSquared.append(( (xx[i]**2) + (yy[i]**2) ))


newRSquared = np.array(newRSquared)

gamma = bf.rGamma(freq,newRSquared)

resonanceI = np.where(newRSquared == max(newRSquared))[0][0]
resonance = freq[resonanceI]
    

print("Resonance Frequency at: " + str(resonance) + '\nGamma of: ' + str(gamma) +
      '\nQ-factor of: ' + str(resonance/gamma) + '\nPeak Amplitude: ' + str(max(newRSquared)))

plt.plot(freq,newRSquared,label='R^2')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper left')
plt.show()



