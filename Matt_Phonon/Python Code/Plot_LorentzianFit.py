import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit

## COMMENTS: First, make sure you have this file (Plot_LoretnzianFit.py) saved in the same folder where all
## your data files are that you want to plot. Next, copy the name of your file as you have saved it
## as the filename. Then, if you need to change your axes, you can do so below. I have set it up, so
## you should not actually have to mess with the code.

filename = 'Justin_Freq_5_0p375323vrms_magDrive_Voltage_0p050Vrms1p00HzStep0p300kHzStart_1p400kHzEnd_500ms_Step_100mVSensitivity300mSPre-Filter_TC_NORMALIZED.txt' 
Xlabel = 'Frequency [kHz]'
Ylabel = 'Amplitude'
Title = 'Frequency Scan'


with open(filename) as f:
    lines = (line for line in f if not line.startswith('#'))
    file = np.loadtxt(lines, skiprows=1)

freq = file[10:,0]
amp = np.square(file[10:,1])

# Fitting the data
# Lorentzian fitting function
def lorentz(x, *p):
    I, gamma, x0 = p
    I = max(amp)
    return I * gamma**2 / ((x - x0)**2 + gamma**2)

print('Amplitude not squared', max(amp)**.5)
# initial parameter guesses
# [height, FWHM, shift]
p1 = np.array([.03, 10, 1434])   
 

def fit(p, x, y):
    return curve_fit(lorentz, x, y, p0 = p)

# Get the fitting parameters for the best lorentzian
solp1, ier1 = fit(p1, freq, amp)

# # coefficient of determination
# def calc_r2(y, f):
#     avg_y = y.mean()
#     sstot = ((y - avg_y)**2).sum()
#     ssres = ((y - f)**2).sum()
#     return 1 - ssres/sstot

# # calculate the errors
# err = calc_r2(amp, lorentz(freq, *solp1))

#Calculate R^2 values
residuals = amp- lorentz(freq, *solp1)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((amp - np.mean(amp))**2)
r_sqr = 1 - (ss_res / ss_tot)
print('R^2', r_sqr)

fhwm = solp1[1]*2

fig, ax = plt.subplots()
txtstr = '\n'.join((
	r'$\mathrm{R^2}=%.4f$' % (r_sqr),
	r'$\mathrm{FWHM}=%.4f$' % (fhwm),
      ))

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, txtstr, transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)


# ploting
plt.plot(freq, amp,'r+', label='Experimental data')
plt.plot(freq, lorentz(freq, *solp1), label="Lorentzian Fit")

plt.xlabel(Xlabel)
#plt.xlim(7000,8500)
plt.ylabel(Ylabel)
plt.title(Title)
plt.legend()

amp, gamma, x0 = solp1[0], solp1[1]*2, solp1[2]
print('amp is', amp, ',', 'FWHM is', gamma, ',', 'x0 is', x0)

plt.show()
