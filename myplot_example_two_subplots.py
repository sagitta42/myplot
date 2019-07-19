from myplot import *
import numpy as np

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
    plt.show()
    # plt.savefig('two_subplots_deafult.png')


def pretty():
    ''' "pretty" look '''
    p1 = Plot((10,8),2) # size 10 x 8, default one subplot

    p1.axes[0].plot(x, y1, label='Day 1')
    p1.axes[0].plot(x, y2, label='Day 2')
    p1.axes[0].set_ylabel("Sindhu's Productivity")

    p1.axes[1].plot(x, y1*y1, label='Day 1')
    p1.axes[1].plot(x, y1 + y2, label='Day 2')
    p1.axes[1].set_ylabel("Mariia's Productivity")

    plt.xlabel('Number of cups of coffee')
    plt.suptitle('Myplot')
    # p1.legend() # default: inside, one column
    p1.legend(out=True, ncol=2) # legend outside with two columns

    p1.pretty() # beautification
    # plt.savefig('two_subplots_myplot.png')
    # plt.savefig('two_subplots_myplot_outside.png')
    plt.show()


pretty()
