import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df.info()
        
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig,ax = plt.subplots(figsize=(6, 6))
    plt.scatter(x, y)


    # Create first line of best fit
    #Instantiate the Linear Regression Algorithm
    linreg = linregress(x,y)
    
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = (linreg.slope * x_pred) + linreg.intercept 
    
    #Extract Coefficient and Intercept
    print(('Slope: %.2f') %linreg.slope)
    print(('Intercept: %.2f') %linreg.intercept)
    print(('y = %.2fx + %.2f') %(linreg.slope,
                                 linreg.intercept))
    
    plt.plot(x_pred, y_pred, 'r')


    # Create second line of best fit

    df_2 = df.loc[df['Year'] >= 2000]
    x_2 = df_2['Year']
    y_2 = df_2['CSIRO Adjusted Sea Level']
    #Instantiate the Linear Regression Algorithm
    linreg_2 = linregress(x_2,y_2)
    
    x_pred2= pd.Series([i for i in range(2000,2051)])
    y_pred2 = (linreg_2.slope * x_pred2) + linreg_2.intercept 
    
    #Extract Coefficient and Intercept
    print(('Slope: %.2f') %linreg_2.slope)
    print(('Intercept: %.2f') %linreg_2.intercept)
    print(('y = %.2fx + %.2f') %(linreg_2.slope,
                                 linreg_2.intercept))
    
    plt.plot(x_pred2, y_pred2, 'b')
  


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')


    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()