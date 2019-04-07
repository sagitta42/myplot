from myplot import *
import numpy as np
import pandas as pd

class XPlot(Plot):
    def xpoints(self,xlim=None):
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
        for ax in self.axes:
            for x in xlist:
                ax.axvline(pd.to_datetime(x), linestyle='--', label = XP[x][0], zorder=4, color=XP[x][1], linewidth=2)



# X points dictionary = {x point : [label, color]}
XP = {
'2018-03-14': ['Pi day','r'],
'2017-12-25': ['25 dec = 31 oct', 'b'],
'2018-07-22': ['Pi approximation day', 'g']
}
