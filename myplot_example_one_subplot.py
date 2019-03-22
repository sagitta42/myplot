''' example of using the Plot class with one subplot '''

from myplot import *
import numpy as np

## example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

### default look

plt.subplots(figsize=(8,6))
plt.plot(x, y1, label='Day 1')
plt.plot(x, y2, label='Day 2')
plt.xlabel('Number of cups of coffee')
plt.ylabel("Sindhuja's productivity")
plt.title('Default')
plt.legend()
plt.savefig('one_subplot_deafult.png')


### "pretty" look
p1 = Plot((8,6)) # size 10 x 8, default one subplot

p1.ax.plot(x, y1, label='Day 1')
p1.ax.plot(x, y2, label='Day 2')

plt.xlabel('Number of cups of coffee')
plt.ylabel("Sindhuja's productivity")
plt.title('Myplot')

p1.legend() # default: inside, one column
p1.pretty() # beautification
plt.savefig('one_subplot_myplot.png')

plt.show()
