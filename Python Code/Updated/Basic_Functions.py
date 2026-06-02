import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
from tkinter import filedialog
from scipy.optimize import curve_fit

def linear(x,m,b):
    return (m*x)+b

def getRSquared(xx,yy):
    rs = []

    for i in range(0,len(xx)):
        rs.append(xx[i]**2 + yy[i]**2)

    return np.array(rs)
    

def getLinearBounds():
    LLBound = int(input('Leftmost Frequency of left wing for normalization? Input an integer frequency from your data (No decimals).\n'))
    LRBound = int(input('Rightmost Frequency of left wing for normalization? Input an integer frequency from your data (No decimals).\n'))
    RLBound = int(input('Leftmost Frequency of right wing for normalization? Input an integer frequency from your data (No decimals).\n'))
    RRBound = int(input('Rightmost Frequency of right wing for normalization? Input an integer frequency from your data (No decimals).\n'))

    return [LLBound,LRBound,RLBound,RRBound]

def getLinearBoundsTest():
    return [2010,2050,2250,2290]

def linearBackground(freq,data,bounds):

    LLI = np.where(freq==bounds[0])[0][0]
    LRI = np.where(freq==bounds[1])[0][0]
    RLI = np.where(freq==bounds[2])[0][0]
    RRI = np.where(freq==bounds[3])[0][0]

    freq1 = freq[LLI:LRI]
    freq2 = freq[RLI:RRI]

    data1 = data[LLI:LRI]
    data2 = data[RLI:RRI]

    backgroundFreq = np.concatenate((freq1,freq2),axis=None)
    backgroundData = np.concatenate((data1,data2),axis=None)

    pars,cov = curve_fit(f = linear, xdata = backgroundFreq,ydata = backgroundData,p0=[0,0],bounds=(-np.inf,np.inf))

    print(str(pars))

    newData = []
    for i in range(0,len(freq)):
        newData.append(data[i] - linear(freq[i],*pars))

    return np.array(newData)

def importDataAuto(file_path):
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
    theta = []


    for x in lines:
        freq.append(float(x[0]))
        xx.append(float(x[2]))
        yy.append(float(x[3]))
        r.append(float(x[1]))
        theta.append(float(x[4]))

    f.close()

    return[freq,r,xx,yy,theta,file_path]

def importData():
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
    theta = []


    for x in lines:
        freq.append(float(x[0]))
        xx.append(float(x[2]))
        yy.append(float(x[3]))
        r.append(float(x[1]))
        theta.append(float(x[4]))

    f.close()

    return[freq,r,xx,yy,theta,file_path]

def findGamma(freq,yData,xData):
    resonanceY = max(yData)
    resonanceI = np.where(yData == resonanceY)[0][0]
    left = 0
    right = 0
    for i in range(0,len(freq)):
        if (yData[i]**2 + xData[i]**2) > (1/2)*(resonanceY**2):
            left = yData[i]
            break

    for i in range(resonanceI,len(freq)):
        if (yData[i]**2 + xData[i]**2) < (1/2)*(resonanceY**2):
            right = yData[i]
            break

    rightW = freq[np.where(yData == right)[0][0]]
    leftW = freq[np.where(yData == left)[0][0]]
    
    delW =  rightW - leftW

    return [delW,(1/2)*resonanceY]

def rGamma(freq,rData):
    resonanceR = max(rData)
    resonanceI = np.where(rData == resonanceR)[0][0]
    left = 0
    right = 0
    for i in range(0,len(freq)):
        if rData[i] > (1/2)*resonanceR:
            left = rData[i]
            break

    for i in range(resonanceI,len(freq)):
        if rData[i] < (1/2)*resonanceR:
            right = rData[i]
            break

    rightW = freq[np.where(rData == right)[0][0]]
    leftW = freq[np.where(rData == left)[0][0]]
    
    delW =  rightW - leftW

    return delW

