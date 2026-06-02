import matplotlib.pyplot as plt
import math
import numpy as np

### Open our data file ###
f = open('test.txt')

n = 0
lines = []

### Reads every line in f, denoted x ###
for x in f:
    
    ### Ignore first two lines ##
    if n < 2:
        n +=1
    else:

        ### Remove '\n' from elements and add to array lines###
        t = x.strip()
        temp = t.split('\t')
        lines.append(temp)

### Make arrays that will hold our data ###
freq = []
r = []

### Fill r, freq, with data values from .txt fle ###
for x in lines:
    freq.append(float(x[0]))
    r.append(float(x[1]))

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
    
