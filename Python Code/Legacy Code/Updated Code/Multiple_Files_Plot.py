import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
from tkinter import filedialog

freqt = []
xt = []
yt = []
rt = []

nxt = []
nyt = []
nrt = []

files = ['0.txt','40.txt','45.txt']

for ti in files:
    f = open(ti)
    freq = []
    xx = []
    yy = []
    r = []

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




    for x in lines:
        freq.append(float(x[0]))
        xx.append(float(x[2]))
        yy.append(float(x[3]))
        r.append(float(x[1]))
    f.close()
    freqt.append(freq)
    xt.append(xx)
    yt.append(yy)
    rt.append(r)


### Ask to Normalize ###
normCalc = input("Normalize? Yes/No.\n")

for i in range(0,3):

    if ('y' in normCalc) or ('Y' in normCalc):
        backgroundR = []
        backgroundX = []
        backgroundY = []
        ### I'm doing this manually instead of relying on pre-loaded functions because I'm stubborn ###

        ### r = m*freq + b ###

        ### Do some algebra to solve for b, plug it into m = (r[0]-b)/freq[0]
        br = ((rt[i][-10]*freqt[i][10] - rt[i][10]*freqt[i][-10])/(freqt[i][10]-freqt[i][-10]))
        mr = (rt[i][10] - br)/freqt[i][10]
        bx = ((xt[i][-10]*freqt[i][10] - xt[i][10]*freqt[i][-10])/(freqt[i][10]-freqt[i][-10]))
        mx = (xt[i][10] - bx)/freqt[i][10]
        by = ((yt[i][-10]*freqt[i][10] - yt[i][10]*freqt[i][-10])/(freqt[i][10]-freqt[i][-10]))
        my = (yt[i][10] - by)/freqt[i][10]

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

        nrt.append(newR)
        nxt.append(newXX)
        nyt.append(newYY)

if ('y' in normCalc) or ('Y' in normCalc):
        rt = nrt
        xt = nxt
        yt = nyt

### Using matplotlib to create plot ###
rPlot = input("Plot R? Yes/No.\n")
xPlot = input("Plot X? Yes/No.\n")
yPlot = input("Plot Y? Yes/No.\n")

for i in range(0,len(xt)):
    if 'y' in rPlot or 'Y' in rPlot:
        normalizedBackgroundR = plt.plot(freqt[i],rt[i], label='R ' + files[i][:-4])
    if 'y' in xPlot or 'Y' in xPlot:
        normalizedBackgroundX = plt.plot(freqt[i],xt[i], label='X ' + files[i][:-4])
    if 'y' in yPlot or 'Y' in yPlot:
        normalizedBackgroundY = plt.plot(freqt[i],yt[i], label='Y ' + files[i][:-4])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend(loc='upper left')
plt.show()
    
