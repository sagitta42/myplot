from myplot import *
import numpy as np

## example points
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.cos(x)**2

def automatic():
    ''' one subplot, adding second y axis '''
    p = Plot((10,8))
    p.add_axis('b')

    p.axes[0].plot(x, y1, label = 'y1', color = 'r')
    p.axes[1].plot(x, y2, label = 'y2', color = 'b')

    p.legend(pos=[3,1])
    p.pretty()
    p.figure('second_yaxis.png')


automatic()
