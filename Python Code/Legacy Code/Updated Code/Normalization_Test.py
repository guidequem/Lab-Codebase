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
    r.append(float(x[1]))
    freq.append(float(x[0]))


backgroundTestR = []
for w in freq:
    backgroundR = 1.44*(10**-5) + (1.504*(10**-9))*w
    backgroundTestR.append(backgroundR)

newR = []
for x in range(0,len(r)):
    newRValue = r[x] - backgroundTestR[x]
    newR.append(newRValue)

### Using matplotlib to create plot ###
normalizedBackgroundR = plt.plot(freq,newR, label='R')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper left')
plt.show()
    
