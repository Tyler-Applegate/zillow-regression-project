# This is my prepare module for my Zillow Regression Project

########################### General Imports ####################################
import pandas as pd
import numpy as np

########################### Prepare Imports ####################################
from sklearn.model_selection import train_test_split
import sklearn.preprocessing

########################## Prepare Functions ###################################

def prep_zillow(df):
    '''
    This function will take in my newly acquired zillow dataframe, and prepare it to be split into
    train, validate, and test sets.
    '''

    # we begin with a dataframe with 28,124 observations
    # replaces whitespace with NaN value
    df = df.replace(r'^\s*$', np.nan, regex=True)

    # drops null values (down to 28,048 observations)
    df = df.dropna()

    # drop duplicate observations (down to 28,026 observations)
    df = df.drop_duplicates()

    # let's add a column for the age of the home (not just year built)
    df['age'] = 2017 - df['yearbuilt']

    # let's convert floats to integers where possible
    df['bed'] = df['bed'].astype(int)
    df['sqft_calc'] = df['sqft_calc'].astype(int)
    df['fips'] = df['fips'].astype(int)
    df['yearbuilt'] = df['yearbuilt'].astype(int)
    df['taxvaluedollarcnt'] = df['taxvaluedollarcnt'].astype(int)
    df['age'] = df['age'].astype(int)

    # calculate upper and lower bounds for square_feet
    sqft_25, sqft_75 = df['sqft_calc'].quantile([0.25, 0.75])
    sqft_iqr = sqft_75 - sqft_25
    limit_upper = sqft_75 + (1.5 * sqft_iqr)
    limit_lower = sqft_25 - (1.5 * sqft_iqr)

    # drop everything outside 1.5 time IQR (now down to 26,449 observations)
    df = df[df['sqft_calc'] > limit_lower]
    df = df[df['sqft_calc'] < limit_upper]

