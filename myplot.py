''' Class for convenient and pretty plotting '''

import matplotlib
import matplotlib.pyplot as plt
import sys

save = 'save' in sys.argv

class Plot:
    def __init__(self,figsize,n=1,sharex=True):
        '''
        figsize: [tuple|list] figure size (e.g. (10,8))
        n: [int] number of subplots
        '''
        fig, ax = plt.subplots(n,figsize=figsize, sharex=sharex)
        self.fig = fig
         # convenient if only have one subplot (not ty type axes[0] all the time)
        self.ax = ax
        # array of all our axes; new axes get added here too (e.g. two subplots, one has 2 y axes, means in total 5 axes in the list)
        self.axes = ax if n > 1 else [ax]


    def legend(self, out=False, ncol=1, pos=None):
        '''
        out: [True|False] If True, draw one legend outside of the plot, else inside (on each subplot)
        ncol: [int] number of columns
        '''

        if out:
            # draw legend at the bottom
            self.axes[-1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), fancybox=True, shadow=False, ncol=ncol,fontsize=15)
            # remove legends from all other subplots
            for ax in self.axes[:-1]:
                legend = ax.legend()
                legend.remove()
        else:
            # draw legend on each axis
            # in case these are not subplots, but one plot with two y axes, legends might crash
            # -> choose given location
            for i in range(len(self.axes)):
                loc = pos[i] if pos else None
                self.axes[i].legend(ncol=ncol, loc=loc)


    def pretty(self, large=3, grid='major'):
        ''' Increase font size everywhere, add grid lines '''

        for ax in self.axes:
            ## make better x and y limits
            xlim = ax.get_xlim()
            ylim = ax.get_ylim()
            ax.set_xlim(xlim[0]*0.9, xlim[1]*1.1)
            ax.set_ylim(ylim[0]*0.9, ylim[1]*1.1)

            ## increase tick sizes (numbers)
            for t in ax.get_xaxis().get_ticklabels():
                t.set_fontsize(15 + large)
            for t in ax.get_yaxis().get_ticklabels():
                t.set_fontsize(15 + large)

            ## increase title sizes
            ax.get_xaxis().get_label().set_fontsize(17 + large)
            ax.get_yaxis().get_label().set_fontsize(17 + large)
            ax.title.set_fontsize(20)

            ## increase legend font
            if ax.get_legend():
                for t in ax.get_legend().get_texts():
                    t.set_fontsize(17 + large)

            ## add gridlines
            if grid: ax.grid(linestyle='--',zorder=0, which=grid)

        ## increase fontsize of texts on the figure
        for t in self.fig.get_children():
            if type(t) == matplotlib.text.Text:
                t.set_fontsize(20)



        ## remove white borders around the plot
        self.fig.tight_layout(rect=[0,0,1,0.97])


    def figure(self, name=None):
        self.pretty(2)
        print 'Image:', name

        if save:
            self.fig.savefig(name)
            print '(saved)'
        else:
            print '(NOT SAVED)'
            plt.show()


    def add_axis(self, ax):
        ''' Used in case a plot has two y axes and we create one additionally externally '''
        self.axes.append(ax)
