import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    res1 = linregress(x, y)
    future_x = pd.Series(np.arange(x.max() + 1, 2051))
    new_x = pd.concat([x, future_x])
    plt.plot(new_x, res1.intercept + res1.slope * new_x, color='red')

    # # Create second line of best fit
    x2 = x[x >= 2000]
    y2 = y[x >= 2000]
    res2 = linregress(x2, y2)
    new_x2 = pd.concat([x2, future_x])
    plt.plot(new_x2, res2.intercept + res2.slope * new_x2, color='orange')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
