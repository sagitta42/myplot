from myplot import *
import numpy as np

### -----------

# pretty style: True, standard style: False
# mystyle = True
mystyle = False

### -----------

## example points
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.cos(x)**2

# size 10 x 8
if mystyle:
    p = Plot((10,6))
else:
    plt.subplots(figsize=(10,6))

## plot
plt.plot(x, y1, label='Day 1')
plt.plot(x, y2, label='Day 2')
plt.plot(x, y3, label='Day 3')

plt.xlabel('Number of cups of coffee')
plt.ylabel("Sindhuja's productivity")
plt.title('Life in the office')

if mystyle:
    p.legend(ncol=1, out=False)
    p.pretty(large=3) # for pretty look
    p.figure('one_subplot_myplot.png') # if 'save' is in argv, it will save the figure instead of showing
else:
    plt.legend()
    plt.savefig('one_subplot_default.png')
    # plt.show()
