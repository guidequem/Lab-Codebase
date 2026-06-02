import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
import Basic_Functions as bf
from tkinter import filedialog
from scipy.optimize import curve_fit
allData = bf.importData()

freq = np.array(allData[0])
rr = np.array(allData[1])*np.array(allData[1])
xx = np.array(allData[2])
yy = np.array(allData[3])
tt = np.array(allData[4])

m = np.amax(rr)
res = freq[np.where(rr==m)]

x1 = 0
x2 = 0

n = 0
for x in rr:
    if x > (0.5* m):
        x1 = x
        n1 = n
        break
    
    n+=1

n = 0
for x in rr:
    if x < (0.5 *m) and n > n1+5:
        x2 = x
        n2 = n
        break
    n+=1

delta = freq[n2] - freq[n1]
print(str(freq[n2]))
print(str(freq[n1]))
print(str(res/delta))


plt.plot(freq,rr,label='R')
#plt.plot(freq,xx,label='X')
#plt.plot(freq,yy,label='Y')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper left')
plt.show()



