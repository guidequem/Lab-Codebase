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

plt.plot(freq,r)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (V)")
plt.show()

leftMostFrequency = int(input("Input the left most frequency to analyze. It must be an exact data point. I don't have error-handling, so don't mess this up.\n"))
rightMostFrequency = int(input("Input the right most frequency to analyze. It must be an exact data point. I don't have error-handling, so don't mess this up.\n"))

leftIndex = freq.index(leftMostFrequency)
rightIndex = freq.index(rightMostFrequency)

print(str(leftIndex))
print(str(rightIndex))

freq = freq[leftIndex:rightIndex]
r = r[leftIndex:rightIndex]
print(str(len(freq)))

plt.plot(freq,r)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (V)")
plt.show()
### Find resonance frequency ###
maxAmplitude = max(r)
maxIndex = r.index(maxAmplitude)
resonantFrequency = freq[maxIndex]

print(str(resonantFrequency))
print(str(maxIndex))

### Find leftmost FWHM value ###
leftFWHM = 0
for n in range(0,maxIndex):
    if r[n] > (maxAmplitude/2 + r[0]):
        leftFWHM = n-1
        break

print("left = " + str(leftFWHM))

### Find rightmost FWHM value ###
rightFWHM = 0
for n in range(maxIndex,len(r)):
    if r[n] < (maxAmplitude/2 + r[-1]):
        rightFWHM = n-1
        break

print("right = " + str(rightFWHM))
### Del-Frequency is difference between the two ###
deltaW = freq[rightFWHM] - freq[leftFWHM]


### Q-value is resonant frequency divided by delta ###
q = resonantFrequency/deltaW

print(str(q))




    
