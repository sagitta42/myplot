from myplot import *
from xpoints import *
import numpy as np
import pandas as pd

class XPlot(Plot):
    def xpoints(self, xlim=None, axis='all'):
        '''
        Plot special points as vertial lines.
        Intended for time series, but can be modified for any x axis (just remove pd.to_datetime)
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
                ax.axvline(pd.to_datetime(x), linestyle='--', label = XP[x][0], zorder=4, color=XP[x][1], linewidth=2)
