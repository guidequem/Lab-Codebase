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

newRR = []

for i in range(0,len(xx)):
    newRR.append(( (xx[i]**2) + (yy[i]**2) )**(1/2))


newRR = np.array(newRR)

gamma = bf.rGamma(freq,newRR)

resonanceI = np.where(newRR == max(newRR))[0][0]
resonance = freq[resonanceI]
    

print("Resonance Frequency at: " + str(resonance) + '\nGamma of: ' + str(gamma) +
      '\nQ-factor of: ' + str(resonance/gamma) + '\nPeak Amplitude: ' + str(max(newRR)))

plt.plot(freq,newRR,label='R^2')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper left')
plt.show()



