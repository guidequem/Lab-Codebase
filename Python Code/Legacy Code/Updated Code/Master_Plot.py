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

### Ask to Calculate Q ###
qCalc = input("Calculate Q from X? Yes/No.\n")

if 'y' in qCalc or 'Y' in qCalc:
    qCalcBool = True
    leftFreq = int(input("Input the lower bound on frequency to begin scanning to calculate Q.\n"))
    rightFreq = int(input("Input the higher bound on frequency to begin scanning to calculate Q.\n"))
else:
    qCalcBool =  False

if qCalcBool:
    ### Find resonance frequency ###
    leftIndex = freq.index(leftFreq)
    rightIndex = freq.index(rightFreq)
    freq = freq[leftIndex:rightIndex]
    xx = xx[leftIndex:rightIndex]
    yy = yy[leftIndex:rightIndex]
    r = r[leftIndex:rightIndex]
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

### Ask to Normalize ###
normCalc = input("Normalize? Yes/No.\n")

if ('y' in normCalc) or ('Y' in normCalc):
    backgroundR = []
    backgroundX = []
    backgroundY = []
    ### I'm doing this manually instead of relying on pre-loaded functions because I'm stubborn ###

    ### r = m*freq + b ###

    ### Do some algebra to solve for b, plug it into m = (r[0]-b)/freq[0]
    br = ((r[-1]*freq[1] - r[1]*freq[-1])/(freq[1]-freq[-1]))
    mr = (r[1] - br)/freq[1]
    bx = ((xx[-10]*freq[10] - xx[10]*freq[-10])/(freq[10]-freq[-10]))
    mx = (xx[10] - bx)/freq[10]
    by = ((yy[-10]*freq[10] - yy[10]*freq[-10])/(freq[10]-freq[-10]))
    my = (yy[10] - by)/freq[10]

    print("bx = " + str(bx) + " | mx = " + str(mx))
    print("br = " + str(br) + " | mr = " + str(mr))
    print("by = " + str(by) + " | my = " + str(my))
    ### Create background values ###
    for x in freq:
        yr = mr*x + br
        backgroundR.append(yr)
        yx = mx*x + bx
        backgroundX.append(yx)
        y = my*x + by
        backgroundY.append(y)

    ### Build new array without background ###
    newXX = []
    newYY = []
    newR = []

    for x in range(0,len(xx)):
        new = xx[x]-backgroundX[x]
        newXX.append(new)
        new = yy[x]-backgroundY[x]
        newYY.append(new)
        new = r[x]-backgroundR[x]
        newR.append(new)

    r = newR
    xx = newXX
    yy = newYY

### Using matplotlib to create plot ###
rPlot = input("Plot R? Yes/No.\n")
xPlot = input("Plot X? Yes/No.\n")
yPlot = input("Plot Y? Yes/No.\n")
if 'y' in rPlot or 'Y' in rPlot:
    normalizedBackgroundR = plt.plot(freq,r, label='R')
if 'y' in xPlot or 'Y' in xPlot:
    normalizedBackgroundX = plt.plot(freq,xx, label='X')
if 'y' in yPlot or 'Y' in yPlot:
    normalizedBackgroundY = plt.plot(freq,yy, label='Y')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper left')
plt.show()
    
