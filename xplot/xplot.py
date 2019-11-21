from myplot import *
from xpoints import *
import numpy as np
import pandas as pd

class XPlot(Plot):
    def xpoints(self, xdate=True, xlim=None, axis='all'):
        '''
        Plot special points as vertial lines.

        xdate [True|False]: x axis is datetime
        xlim [None|number|string (date)]: starting from which x value we plot
            the vertical lines (default None means plot all the points in ```XP```)
        axis ['all'|int]: 'all' means the vertical lines will be plotted on
            each subplot; if an integer is given, they are plotted only on
            that axis number.
        '''

        xlist = list(XP.keys())
        xlist.sort()
        xlist = np.array(xlist)
        # select only the ones in our region
        if xlim: xlist = xlist[xlist > xlim]
        # plot
        axes = self.axes if axis == 'all' else [self.axes[axis]]
        for ax in axes:
            for x in xlist:
                xpnt = pd.to_datetime(x) if xdate else x
                ax.axvline(xpnt, linestyle='--', label = XP[x][0], zorder=4, color=XP[x][1], linewidth=2)
