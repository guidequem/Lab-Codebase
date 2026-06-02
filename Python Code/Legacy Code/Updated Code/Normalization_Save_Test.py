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
XX = []


for x in lines:
    XX.append(float(x[2]))
    freq.append(float(x[0]))


backgroundTestX = []
for w in freq:
    backgroundX = 1.3217*(10**(-5)) + (-1.4326*(10**(-10)))*w
    backgroundTestX.append(backgroundX)

newX = []
for x in range(0,len(freq)):
    newXValue = XX[x] - backgroundTestX[x]
    newX.append(newXValue)

f.close()

f = open('test_normalized_data.txt','w+')

for x in range(0,len(freq)):
    f.write(str(freq[x]) + ',' + str(newX[x]) + '\n')
f.close()


    
