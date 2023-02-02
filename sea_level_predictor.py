import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df.Year
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    xo = pd.Series(range(1880, 2051))
    reso = linregress(x, y)
    plt.plot(xo, (reso.intercept + reso.slope*xo), 'r', label='fitted line')

    # Create second line of best fit
    dfn = df.loc[df['Year'] >=2000]
    xn = dfn['Year']
    yn = dfn['CSIRO Adjusted Sea Level']
    xt = pd.Series(range(2000, 2051))
    rest = linregress(xn, yn)
    plt.plot(xt, rest.intercept + rest.slope*xt, 'b', label='fitted line 2')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.xticks(ticks=[1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()