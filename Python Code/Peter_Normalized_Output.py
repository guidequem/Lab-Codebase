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


leftW = int(input('Leftmost Frequency to analyze? 0 if all data.\n'))
rightW = int(input('Rightmost Frequency to analyze? 0 if all data.\n'))


if leftW == 0:
    leftI = 0
else:
    leftI = np.where(freq==leftW)[0][0]

if rightW == 0:
    rightI = len(freq)
else:
    rightI = np.where(freq==rightW)[0][0]

freq = freq[leftI:rightI]
xx = xx[leftI:rightI]
yy = yy[leftI:rightI]
rr = rr[leftI:rightI]
tt = tt[leftI:rightI]

f = open(str(allData[5])[:-4] + '_NORMALIZED.txt','w+')

for i in range(0,len(freq)):
    f.write(str(freq[i]) + ',' + str(rr[i]) + ',' + str(xx[i]) + ',' + str(yy[i]) + ',' + str(tt[i]) +'\n')

f.close()


plt.plot(freq,rr,'g-')

plt.show()



