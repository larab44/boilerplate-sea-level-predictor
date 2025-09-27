import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    data_points = plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'], label = 'data points')

    # Create first line of best fit
    years_future = np.arange(df['Year'].min(), 2051)
plt.plot(years_future, line_fit.intercept + line_fit.slope * years_future, 
         color='purple', linestyle='-', label='Previsão até 2050')

    # Create second line of best fit
    years_from_2000 = np.arange(2000, 2051)
plt.plot(years_from_2000, line_fit.intercept + line_fit.slope * years_from_2000, 
         color='pink', linestyle='--', label='Previsão até 2050 a partir de 2000')

    # Add labels and title
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()