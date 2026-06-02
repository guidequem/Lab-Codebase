import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
from tkinter import filedialog

####################################################################################################
### Automatically plot an inputted .txt file with the specifics of the lab's save file structure ###
####################################################################################################
'''
root = tk.Tk()


filename = filedialog.askopenfilename()
'''

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



fig = plt.figure()
plt.plot(freq,r)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (V)")
fig.savefig('graph.png')
    
