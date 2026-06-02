import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
import Basic_Functions as bf
from tkinter import filedialog
from scipy.optimize import curve_fit

### Get Data ###
allData = bf.importData()

freq = np.array(allData[0])
rr = np.array(allData[1])
xx = np.array(allData[2])
yy = np.array(allData[3])
tt = np.array(allData[4])

### Get bounds for fitting and subtract linear background noise ###
bounds = bf.getLinearBounds()
xx = bf.linearBackground(freq,xx,bounds)
yy = bf.linearBackground(freq,yy,bounds)
rr = bf.linearBackground(freq,rr,bounds)

plt.plot(freq,rr,label='R')
plt.plot(freq,xx,label='X')
plt.plot(freq,yy,label='Y')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper right')
plt.show()



