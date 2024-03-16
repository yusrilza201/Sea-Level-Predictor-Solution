import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(20,16))

    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', alpha=1, cmap='Spectral')
    plt.colorbar()


    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = list(range(1880, 2051))
    y = [slope * xi + intercept for xi in x]

    plt.plot(x, y, color='red')

    # Create second line of best fit
    df_filter = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_filter['Year'], df_filter['CSIRO Adjusted Sea Level'])
    
    x = list(range(2000, 2051))
    y = [slope * xi + intercept for xi in x]

    plt.plot(x, y, color='red')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()