# This is my Zillow explore module

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import pearsonr, spearmanr
import acquire
import prepare

############################## plot the cat and continous variables ##############################

def explore_univariate(df, figsize = (18,3)):
    '''
    This function is for exploring. Takes in a dataframe with variables you would like to see the box plot of.
    Input the dataframe (either fully, or using .drop) with ONLY the columns you want to see plotted.
    Optional arguement figsize. Default it's small.    
    '''

    for col in list(df):
        plt.figure(figsize=figsize)
        plt.subplot(121)
        sns.boxplot(y = col, data = df)
        plt.title(f'Box Plot of {col}')

        plt.subplot(122)
        sns.histplot(data = df, x = col, kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()
        
def zillow_heat(df):
    '''
    This function returns a heatmap of the chosen columns from the train DataFrame.
    '''
    # correlation matrix
    zillow_corr = df.drop(columns=['appraised_value', 'fips', 'yearbuilt']).corr()
    
    # plot the heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(zillow_corr, cmap='Purples', annot=True, linewidth=0.5, mask= np.triu(zillow_corr))
    plt.show()
    