from myplot import *
import numpy as np

### -----------

#/3 pretty style: True, standard style: False
mystyle = True
# mystyle = False
## legend outside or inside the plot, for myplot
legout = True
# legout = False

### -----------


## example points
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

def default():
    ''' default look '''
    fig, ax = plt.subplots(2, figsize=(10,8), sharex=True)
    ax[0].plot(x, y1, label='Day 1')
    ax[0].plot(x, y2, label='Day 2')
    ax[0].set_ylabel("Sindhu's Productivity")
    ax[0].legend()

    ax[1].plot(x, y1*y1, label='Day 1')
    ax[1].plot(x, y1 + y2, label='Day 2')
    ax[1].set_ylabel("Mariia's Productivity")
    ax[1].legend()

    plt.xlabel('Number of cups of coffee')
    plt.suptitle('Default')
    # plt.show()
    plt.savefig('two_subplots_default.png')


def pretty():
    ''' "pretty" look '''
    p = Plot((10,8),2) # size 10 x 8, default one subplot

    p.axes[0].plot(x, y1, label='Day 1')
    p.axes[0].plot(x, y2, label='Day 2')
    p.axes[0].set_ylabel("Sindhu's Productivity")

    p.axes[1].plot(x, y1*y1, label='Day 1')
    p.axes[1].plot(x, y1 + y2, label='Day 2')
    p.axes[1].set_ylabel("Mariia's Productivity")

    plt.xlabel('Number of cups of coffee')
    plt.suptitle('Myplot')

    ncol = 2 if legout else 1
    p.legend(out=legout, ncol=ncol) # legend outside with two columns

    p.pretty() # beautification
    imgname = 'two_subplots_myplot'
    if legout: imgname += '_outside'
    p.figure(imgname + '.png')


if mystyle:
    pretty()
else:
    default()
