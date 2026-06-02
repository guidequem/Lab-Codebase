import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
from tkinter import filedialog

def xBackground(w):
    m = -1.4326 * (10**(-10))
    b = 1.3217 * (10**(-5))

    return m*w + b

def yBackground(w):
    m = -1.7908 * (10**(-9))
    b = -9.328 * (10**(-6))

    return m*w + b

def rBackground(w):
    m = 1.5433 * (10**(-9))
    b = 1.4282 * (10**(-5)) - 1.0959 * (10**(-5))

    return m*w + b

def normalize(freq,data,typ):
    normalizedData = []
    for i in range(0,len(freq)):
        w = freq[i]

        if 'x' in typ or 'X' in typ:
            normalizedData.append(data[i]-xBackground(w))

        if 'y' in typ or 'Y' in typ:
            normalizedData.append(data[i]-yBackground(w))

        if 'r' in typ or 'R' in typ:
            normalizedData.append(data[i]-rBackground(w))

    return np.array(normalizedData)

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


    for x in lines:
        freq.append(float(x[0]))
        xx.append(float(x[2]))
        yy.append(float(x[3]))
        r.append(float(x[1]))

    f.close()

    return[freq,r,xx,yy]


