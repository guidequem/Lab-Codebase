import matplotlib.pyplot as plt
import math
import numpy as np

f = open('test.txt')

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



plt.plot(freq,r)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (V)")
plt.show()
    
