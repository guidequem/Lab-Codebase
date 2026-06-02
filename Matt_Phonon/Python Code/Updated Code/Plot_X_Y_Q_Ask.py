import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

f = open(file_path)

n = 0

lines = []
for x in f:
    
    ### Ignore first two lines ##
    if n < 2:
        n +=1
    else:

        ### Remove '\n' from elements ###
        t = x.strip()
        temp = t.split('\t')
        lines.append(temp)

freq = []
xx = []
yy = []
r = []


for x in lines:
    freq.append(float(x[0]))
    xx.append(float(x[2]))
    yy.append(float(x[3]))
    r.append(float(x[1]))

### Find resonance frequency ###
maxAmplitude = max(xx)
maxIndex = xx.index(maxAmplitude)
resonantFrequency = freq[maxIndex]

### Find leftmost FWHM value ###
leftFWHM = 0
for n in range(0,maxIndex):
    if xx[n] > (maxAmplitude*0.7071):
        leftFWHM = n-1
        break

### Find rightmost FWHM value ###
rightFWHM = 0
for n in range(maxIndex,len(yy)):
    if xx[n] < (maxAmplitude*0.7071):
        rightFWHM = n-1
        break

### Del-Frequency is difference between the two ###
deltaW = freq[rightFWHM] - freq[leftFWHM]


### Q-value is resonant frequency divided by delta ###
q = resonantFrequency/deltaW

print(str(q))
print(str(file_path))


### Using matplotlib to create plot ###
normalizedBackgroundX = plt.plot(freq,xx, label='X')
normalizedBackgroundY = plt.plot(freq,yy, label='Y')
normalizedBackgroundR = plt.plot(freq,r, label='R')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper left')
plt.show()
    
