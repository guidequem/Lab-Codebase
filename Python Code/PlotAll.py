import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
import Basic_Functions as bf
from tkinter import filedialog
from scipy.optimize import curve_fit
from os import listdir
from os.path import isfile, join

mainfile = "C:\\Users\\labuser\\Desktop\\Data\\"

for x in listdir(mainfile):
    current = listdir(mainfile+x)
    for y in current:
        if (('Run' in str(y) or 'run' in str(y) or 'mA' in str(y)) and 'Voltage' in str(y) and not 'png' in str(y)) and not (y[:-4]+'.png') in str(current):
            print('Plotting')
            allData = bf.importDataAuto(mainfile+x+'\\'+y)
            
            freq = np.array(allData[0])
            rr = np.array(allData[1])
            xx = np.array(allData[2])
            yy = np.array(allData[3])
            tt = np.array(allData[4])

            plt.plot(freq,rr,label='R')
            plt.plot(freq,xx,label='X')
            plt.plot(freq,yy,label='Y')
            plt.xlabel("Frequency (Hz)")
            plt.ylabel("Amplitude")
            plt.legend(loc='upper left')
            plt.savefig(mainfile+x+'\\'+y[:-4]+'.png')
            plt.close()


