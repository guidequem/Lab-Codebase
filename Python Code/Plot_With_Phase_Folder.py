import matplotlib.pyplot as plt
import math
import numpy as np
import tkinter as tk
import Basic_Functions as bf
from tkinter import filedialog
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
import os

def elastic(x,t,gamma,f):
    return (f)*((t**2)-(x**2))/((((t**2)-(x**2))**2)+(gamma**2)*(x**2))

def absorb(x,t,gamma,f):
    return (f)*(gamma*x)/((((t**2)-(x**2))**2)+(gamma**2)*(x**2))

def rSquared(x,t,gamma,f):
    return ((f**2)) * 1/(t**4 - 2*(t*x)**2 + (gamma*x)**2 + x**4)

def findGamma(freq,r):
    maxR = max(r)
    maxN = np.where(r==maxR)[0][0]
    resonance = freq[np.where(r==maxR)[0][0]]
    nLeft = 0
    nRight = 0
    for n in range(0,len(r)):
        if r[n] > (1/2)*maxR:
            nLeft = n
            break
    for n in range(maxN,len(r)):
        if r[n] < (1/2)*maxR:
            nRight = n
            break
    fwhm = freq[nRight]-freq[nLeft]

    return (float(fwhm))

def findXGamma(freq,x):
    maxX = max(x)
    maxN = np.where(x==maxX)[0][0]
    minX = min(x)
    minN = np.where(x==minX)[0][0]

    gamma = freq[maxN]-freq[minN]

    return abs(gamma)

def linear(x,m,b):
    return (m*x)+b

def poly(x,a,b,c,d,e,f,g):
    return a + b*x + c*(x**2) + d * (x**3) + e * (x**4) + f * (x**5) + g * (x**6)

def temperature(sh):
    offset = 194.8-179.17
    temp = [70.1452,75.1379,80.1295,85.1255,90.1222,95.1158,100.112,110.114,120.099,130.098,140.099,150.101,160.094,170.092,180.088,190.091,200.086,210.085,220.073,230.089,240.088,250.081,260.062,270.079,280.083,290.069,300.090]
    resistance = [192.421,182.375,173.372,165.230,157.868,151.125,144.957,134.032,124.649,116.502,109.346,103.026,97.4067,92.3675,87.8378,83.7349,80.0122,76.6302,73.5370,70.6910,68.0765,65.6691,63.4445,61.3766,59.4585,57.6737,56.0078]

    temp = np.array(temp)
    resistance = np.array(resistance)

    pars,cov = curve_fit(f = poly, xdata = temp,ydata = resistance,p0=[0,0,0,0,0,0,0],bounds=(-np.inf,np.inf))

    backgroundT = [77,300]
    backgroundR = [194.8-180,77.4-55.7]
    parsL,covL = curve_fit(f = linear, xdata = backgroundT,ydata = backgroundR,p0=[0,0],bounds=(-np.inf,np.inf))
    return(float(fsolve(poly,0,args=(parsL[1] + pars[0]-sh, parsL[0] + pars[1], pars[2],pars[3],pars[4],pars[5],pars[6]))))

inp = 'YES'
try:
    root = 'C:\\Users\\labuser\\Desktop\\Data\\7_23_2023\\LN2 Data\\Warming Up\\'
    #root = 'C:\\Users\\ifeel\\Box\\Currently Analyzing\\recent\\7_13_Curated\\Mag\\'
    files = os.listdir(root)
except:
    root = 'C:\\Users\\Matt\\Box\\Currently Analyzing\\recent\\7_13_Curated\\RC\\'
    files = os.listdir(root)
outputString = ''

for f in files:
    ### Get Conversion to nm ###
    indexVpp = f.index('Vpp')
    indexmA = f.index('mA_')
    vpp = float(f[indexmA + 3:indexVpp])
    con = float(1310/(4*vpp))
    ### Get Data ###
    allData = bf.importDataManual(str(root+f))
    freq = np.array(allData[0])
    rr = np.array(allData[1]) * con
    xx = np.array(allData[2]) * con
    yy = np.array(allData[3]) * con
    filePath = str(allData[5])
    indexPath = filePath.find('Ohm')

    labelOhm = filePath[indexPath-5:indexPath].replace('_','')
    print('\n' + str(labelOhm) + ' Ohms\n')
    print('\n' + str(vpp) + ' Vpp\n')
    print('\n' + str(con) + ' Conversion Factor\n')
    print(str(filePath) + '\n')
    testIndex = labelOhm.find('_')
    if testIndex > 0:
        labelOhm = labelOhm[testIndex+1:]

    ### Truncate some jumps from the start and end ###

    xx = xx[5:len(xx)-5]
    freq = freq[5:len(freq)-5]
    yy = yy[5:len(yy)-5]
    rr = rr[5:len(rr)-5]

    '''
    ### Get bounds for fitting and subtract linear background noise ###
    bounds = bf.getLinearBounds()
    xx = bf.linearBackground(freq,xx,bounds)
    yy = bf.linearBackground(freq,yy,bounds)
    rr = bf.linearBackground(freq,rr,bounds)
    '''
    #plt.plot(freq,xx,label='Elastic Normal')

    phaseFixed = False
    for x in range(0,1800,1):
        ### Do the adjustment for phase ###
        theta = (x/3600) * 2 * 3.14
        yyAdjusted = (yy*np.cos(theta) - xx*np.sin(theta))
        xxAdjusted = (yy *np.sin(theta) + xx*np.cos(theta))
        rrAdjusted = (np.sqrt(xxAdjusted**2 + yyAdjusted**2))

        if abs(abs(min(xxAdjusted)) - max(xxAdjusted)) < 0.01 * max(xxAdjusted):
            phaseFixed = True
            if abs(min(yyAdjusted)) > max(yyAdjusted):
                yyAdjusted = -(yy*np.cos(theta) - xx*np.sin(theta))
                xxAdjusted = -(yy *np.sin(theta) + xx*np.cos(theta))
                rrAdjusted = np.sqrt(xxAdjusted**2 + yyAdjusted**2)

            '''
            ### Get bounds for plotting over and analysis ###
            leftW = int(input('Leftmost Frequency to analyze?\n'))
            rightW = int(input('Rightmost Frequency to analyze? 0 if all data.\n'))


            ### Shorten data ###
            leftI = np.where(freq==leftW)[0][0]

            if rightW == 0:
                rightI = len(freq)
            else:
                rightI = np.where(freq==rightW)[0][0]

            freq = freq[leftI:rightI]
            xx = xx[leftI:rightI]
            yy = yy[leftI:rightI]
            rr = rr[leftI:rightI]

            '''
            ### Find parameters ###
            gamma = findGamma(freq,rrAdjusted)
            resonance = freq[np.where(abs(yy)==max(abs(yy)))[0][0]]
            fm = max(yyAdjusted) * gamma * resonance

            indexOfResonance = np.where(abs(yy)==max(abs(yy)))[0][0]
            '''
            xxAdjusted = xxAdjusted[indexOfResonance-100:indexOfResonance + 100]
            yyAdjusted = yyAdjusted[indexOfResonance-100:indexOfResonance + 100]
            rrAdjusted = rrAdjusted[indexOfResonance-100:indexOfResonance + 100]
            freqAdjusted = freq[indexOfResonance-100:indexOfResonance + 100]
            '''
            rs = bf.getRSquared(xx,yy)

            parsx,covx = curve_fit(f=elastic,xdata = freq,ydata = xxAdjusted,p0=[resonance-1,gamma,fm],bounds = (0,np.inf))
            parsy,covy = curve_fit(f=absorb,xdata = freq,ydata = yyAdjusted,p0=[resonance-5,gamma,fm],bounds = (0,np.inf))
            parsr,covr = curve_fit(f=rSquared, xdata=freq,ydata = rrAdjusted,p0=[resonance-5,gamma,fm],bounds = (0,np.inf))

            print("Elastic Fitting:")
            print("Resonance Frequency = " + str(parsx[0]) + "\nGamma = " +
                  str(parsx[1]) + "\nForce = " + str(parsx[2]) + "\nMass = " + str(parsx[2]))
            print("Possible Q-Value of : " + str(parsx[0]/parsx[1]))
            print('Absorptive Peak = ' + str(max(yy)))
            print('F/m = ' + str(parsx[2]))
            print()
            print("Absorptive Fitting:")
            print("Resonance Frequency = " + str(parsy[0]) + "\nGamma = " +
                  str(parsy[1]) + "\nForce = " + str(parsy[2]) + "\nMass = " + str(parsy[2]))
            print("Possible Q-Value of : " + str(parsy[0]/parsy[1]))
            print('Absorptive Peak = ' + str(max(yy)))
            print('F/m = ' + str(parsy[2]))

            #customPars = [importantPars[0],1.16,51]
            
            plt.plot(freq,yyAdjusted,label=str(labelOhm) + ' Absorptive ' + str(x/10))
            plt.plot(freq,absorb(freq,*parsy),label='Absorptive Fit')
            #plt.plot(freq,absorb(freq,*customPars),label='R'+r'$^2$' + ' custom')
            
            plt.plot(freq,xxAdjusted,label=str(labelOhm) + ' Elastic ' + str(x/10))
            plt.plot(freq,elastic(freq,*parsx),label='Elastic Fit')
            #plt.plot(freq,elastic(freq,*customPars),label='R'+r'$^2$' + ' custom')

            
            break

    # Add data to output list #
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.legend(loc='upper right')
    plt.title(f)
    plt.show()
    addData = input('Plot and fit good to add?\n').upper()
    labelOhm = temperature(float(labelOhm))
    print(labelOhm)
    mag = False
    if 'MAG' in str(f).upper():
        mag = True
    if 'Y' in addData:
        outputString += '\n'
        outputString += str(parsx[1]) + ',' + str(parsx[2]) + ',' + str(parsy[1]) + ',' + str(parsy[2]) + ',' + str(labelOhm)
        if mag:
            outputString += ',Mag'
        else:
            outputString += ',Cap'

print()
f = open('output.txt','a')
f.write(outputString)
f.close()
print(outputString)




