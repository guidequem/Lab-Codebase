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

background = []

### I'm doing this manually instead of relying on pre-loaded functions because I'm stubborn ###

### r = m*freq + b ###

### Do some algebra to solve for b, plug it into m = (r[0]-b)/freq[0]
b = ((xx[-1]*freq[0] - xx[0]*freq[-1])/(freq[0]-freq[-1]))
m = (xx[0] - b)/freq[0]

### Create background values ###
for x in freq:
    y = m*x + b
    background.append(y)

### Build new array without background ###
newXX = []
newYY = []
newR = []

for x in range(0,len(xx)):
    new = xx[x]/background[x]
    newXX.append(new)
    new = yy[x]/background[x]
    newYY.append(new)
    new = r[x]/background[x]
    newR.append(new)


### Using matplotlib to create plot ###
normalizedBackgroundX = plt.plot(freq,newXX, label='X Normalized to Linear Background')
normalizedBackgroundY = plt.plot(freq,newYY, label='Y Normalized to Linear Background')
normalizedBackgroundR = plt.plot(freq,newR, label='R Normalized to Linear Background')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Relative Amplitude")
plt.legend(loc='upper left')
plt.show()
    
