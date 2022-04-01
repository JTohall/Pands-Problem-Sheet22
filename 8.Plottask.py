# Programme that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range[0,4]
# on the one set of axes
# Author: Jamie Tohall

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array (range(0,5))
# Setting the variables, this will show a range of 0-4 on the X axies

# Calculating the functions and plotting below

# First function F(x)=X
ypoints = xpoints
plt.plot (xpoints, ypoints, label="F(x)=X", marker='D', mec='r', color="pink", linewidth=3)

# Second function G(x)=X2
ypoints = (xpoints ** 2)
plt.plot (xpoints, ypoints, label="G(x)=X2", marker='D', mec='r', color="lime", linewidth=3)

# Third function H(x)=X3
ypoints = (xpoints ** 3)
plt.plot (xpoints, ypoints, label="H(x)=X3", marker='D', mec='r', color="orange", linewidth=3)

# With all the functions above I have labelled them, set a diamond marker with a red edge, edited
# the colours of the lines and increased the line width. 

plt.title ("Functions", fontsize=25, color="grey") 
# Added a title to the graph, edited the colour and increased the font size
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
# Labelled the X and Y axies
plt.legend()
# Added a legend, which incoporated the labels of the functions above
plt.grid()
# I also added a grid to the background of the graph, for easier viewing

plt.savefig('Plottask.png')
plt.show()
# Shows final plot and saves it

