# Myplot framework

Consists of two main parts, **myplot** and **xplot** (inherits from myplot)

# myplot

Plot class **```Plot```** for quick prettification of plots. Example:

```python
from myplot import *

p = Plot((10,8)) # canvas size

plt.plot(x, y, label = 'shrubbery')

p.legend(out=True, ncol=2) # create legend
p.pretty() # make everything pretty
p.figure('name.png') # save figure or display plot
```

## Legend

Method ```legend()``` allows quick management of legends. Arguments:

- out [True|False]: legend outside of the plot in the bottom (default False)

- ncol [int]: number of columns in the legend (default 1)

- pos [list of int|string]: position of the legend (default "best"). Important for plotting with a second Y axis (see below)

Compare


```python
p.legend(out=False,ncol=1)
```

(gives ```two_subplots_myplot.png```)

and


```python
p.legend(out=True,ncol=2)
```

(gives ```two_subplots_myplot_outside.png```)


## Pretty

Method ```pretty()``` allows quick beautification:

- add grid

- increase all fontsize

- increase tick labels

Arguments:

- large [int]: controls fontsizes (default 3)

- stretch [None|"float"|"year"] change x axis range (default None). Useful for cases when the automatic ranges makes the leftmost and rightmost point fall right at the frame and get "eaten up"
    None: do not do anything
    "float": increase the range by 10%
    "year": increase the range by 1
    
- grid ["major"|"minor"]: only major grid, or also minor; same as the grid argument of the function ax.grid()


Compare the same plot with (```one_subplot_myplot.png```) and without ```pretty()``` (```one_subplot_default.png```)

## Figure

If you run your plotting function with an argument 'save':

```console
python example.py save
```

It will save the figure with the filename that you provide as the argument. Otherwise it will simply display the plot.

## Second Y axis

Method ```add_axis()``` adds a second Y axis. Arguments:

- col [string]: colour of the axis. Can be useful to differentiate the curves and see which one belongs to which Y axis

- ax [None|pyplot Axis]: axis to add. If None, a second axis is created automatically as a twin of the first axis. In case of two subplots, it will create a second Y axis only for the first subplot. So if you want to add two Y axis for both subplots, create them "externally" and add by passing them to this function. Maybe this should be improved in the future to be automatic as well, by simply asking the number of secondary Y axes

Example usage in ```example_second_axis.py```


# xplot

Plot class ```XPlot``` with an additional method that allows plotting vertical lines at given points. Useful for plots that are "chronological", to show evolution of something in time and correlations with certain events.

Has only one additional method: ```xpoints()```. The method reads an array of x points called ```XP``` which is stored in ```xpoints.py``` (modify as you wish).

Arguments:

- xdate [True|False]: x axis is datetime

- xlim [None|number|string (date)]: starting from which x value we plot the vertical lines (default None means plot all the points in ```XP```)

- axis ['all'|int]: 'all' means the vertical lines will be plotted on each subplot; if an integer is given, they are plotted only on that axis number.


Example usage is shown in ```xplot_example.py``` (```xplot_example.png```)
