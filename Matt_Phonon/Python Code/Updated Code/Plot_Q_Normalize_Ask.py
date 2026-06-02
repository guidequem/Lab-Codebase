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
r = []


for x in lines:
    freq.append(float(x[0]))
    r.append(float(x[1]))

### Find resonance frequency ###
maxAmplitude = max(r)
maxIndex = r.index(maxAmplitude)
resonantFrequency = freq[maxIndex]

### Find leftmost FWHM value ###
leftFWHM = 0
for n in range(0,maxIndex):
    if r[n] > (maxAmplitude*0.7071):
        leftFWHM = n-1
        break

### Find rightmost FWHM value ###
rightFWHM = 0
for n in range(maxIndex,len(r)):
    if r[n] < (maxAmplitude*0.7071):
        rightFWHM = n-1
        break

### Del-Frequency is difference between the two ###
deltaW = freq[rightFWHM] - freq[leftFWHM]


### Q-value is resonant frequency divided by delta ###
q = resonantFrequency/deltaW

print(str(q))

background = []

### I'm doing this manually instead of relying on pre-loaded functions because I'm stubborn ###

### r = m*freq + b ###

### Do some algebra to solve for b, plug it into m = (r[0]-b)/freq[0]
b = ((r[-1]*freq[0] - r[0]*freq[-1])/(freq[0]-freq[-1]))
m = (r[0] - b)/freq[0]

### Create background values ###
for x in freq:
    y = m*x + b
    background.append(y)

### Build new array without background ###
newR = []

for x in range(0,len(r)):
    new = r[x]/background[x]
    newR.append(new)

### Normalize to first entry to show comparison ###
test = []
for x in range(0,len(r)):
    te = r[x]/r[0]
    test.append(te)

### Using matplotlib to create plot ###
normalizedBackground = plt.plot(freq,newR, label='Normalized to Linear Background')
normalized = plt.plot(freq,test, label='Normalized to First Entry')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Relative Amplitude")
plt.legend(loc='upper left')
plt.show()
    
