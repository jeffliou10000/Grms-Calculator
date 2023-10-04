import numpy as np
import matplotlib.ticker as mticker
from scipy.integrate import quad
import matplotlib.pyplot as plt

def loglogslope(x1, x2, y1, y2):
    return (np.log(y1)-np.log(y2)) / (np.log(x1)-np.log(x2))

def loglogintercept(x1, y1, m):
    return y1 / (x1**m)

def integral(x1, x2, m, b):
    return b/(m+1)*x2**(m+1)-b/(m+1)*x1**(m+1)

def GRMS(area):
    return round(np.sqrt(np.sum(area)), 2)

def PSDplot(frequency, PSD, label):
    maximumfrequency = np.max(frequency)
    plt.plot(frequency, PSD, label=label)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which='both')
    plt.xlim(1, maximumfrequency)
    plt.ylabel('Frequency (Hz)')
    plt.ylabel('PSD (G^2/Hz)')
    ax = plt.gca()
    plt.xticks([1, maximumfrequency/10, maximumfrequency])
    ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
    plt.legend()
    plt.show()
    
frequency = [1, 4, 100, 200]
PSD = [0.0001, 0.01, 0.01, 0.001]
label = 'Vib Event 1'

area = []

for i in range(len(frequency) - 1):
    m = loglogslope(frequency[i], frequency[i+1], PSD[i], PSD[i+1])
    b = loglogintercept(frequency[i], PSD[i], m)
    area.append(integral(frequency[i], frequency[i+1], m, b))
    
print(f'{GRMS(area)} Grms')
PSDplot(frequency, PSD, label)