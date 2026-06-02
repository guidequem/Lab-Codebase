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
rr = []

for i in range(0,len(xx)):
    rr.append( ( (xx[i]**2) + (yy[i]**2) )**(1/2))

f = open(str(allData[5])[:-4] + '_NORMALIZED.txt','w+')

for i in range(0,len(freq)):
    f.write(str(freq[i]) + '\t' + str(rr[i]) + '\t' + str(xx[i]) + '\t' + str(yy[i]) + '\t' + str(tt[i]) +'\n')

f.close()

input("Press Any Key To Exit.")



