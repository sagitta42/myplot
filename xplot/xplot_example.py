from xplot import *

### read dataframe
df = pd.read_csv('example.csv', parse_dates=['Date'], index_col=[0])

p = XPlot((10,8))

df.plot(ax = p.ax, style='.-')

p.xpoints()
p.legend(True,2)
p.pretty()

p.figure('xplot_example.png')
