from myplot import *
import numpy as np

## example points
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

## choose look:
## pretty
p = Plot((8,6)) # size 10 x 8, default one subplot
## default
# plt.subplots(figsize=(8,6))

## plot
plt.plot(x, y1, label='Day 1')
plt.plot(x, y2, label='Day 2')
plt.xlabel('Number of cups of coffee')
plt.ylabel("Sindhuja's productivity")
plt.title('Life in the office')

plt.legend()
p.pretty() # for pretty look
plt.show()
