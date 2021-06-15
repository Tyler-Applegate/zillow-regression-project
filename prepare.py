# This is my prepare module for my Zillow Regression Project

########################### General Imports ####################################
import pandas as pd
import numpy as np

########################### Prepare Imports ####################################
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import scipy.stats as stats
import acquire

########################## Prepare Functions ###################################

def initial_setup(df):
    '''
    This function takes in the zillow Dataframe, and does some intial cleaning.
    '''
    # we begin with a dataframe with 28,053 observations

    # set index to parcelid (no statistical value)
    df.set_index('parcel_id', drop=True, inplace=True)

    # replaces whitespace with NaN value
    df = df.replace(r'^\s*$', np.nan, regex=True)

    # drops null values (zero nulls to drop)
    df = df.dropna()

    # drop duplicate observations (dropped 32, down to 28,021 observations)
    df = df.drop_duplicates()
    
    return df

def change_columns(df):
    '''
    This function adds an 'age' column and converts floats to integers.
    '''

    # let's add a column for the age of the home (not just year built)
    df['age'] = 2017 - df['yearbuilt']

    # let's convert floats to integers where possible
    df['bed'] = df['bed'].astype(int)
    df['sqft_calc'] = df['sqft_calc'].astype(int)
    df['fips'] = df['fips'].astype(int)
    df['yearbuilt'] = df['yearbuilt'].astype(int)
    df['appraised_value'] = df['appraised_value'].astype(int)
    df['age'] = df['age'].astype(int)

    return df

def drop_outliers(df, col_list):
    '''
    This function takes in a dataframe and removes outliers that are 1.5 * the IQR
    '''
    for col in col_list:

        q_25, q_75 = df[col].quantile([0.25, 0.75])
        q_iqr = q_75 - q_25
        q_upper = q_75 + (1.5 * q_iqr)
        q_lower = q_25 - (1.5 * q_iqr)
        df = df[df[col] > q_lower]
        df = df[df[col] < q_upper]
    return df
    


def prep_zillow():
    '''
    This function will take in my newly acquired zillow dataframe, and prepare it to be split into
    train, validate, and test sets.
    '''
    col_list = ['bath', 'bed', 'sqft_calc', 'yearbuilt', 'appraised_value',
       'tax_amount', 'age']
    
    df = acquire.get_zillow_data()
    # we begin with a dataframe with 28,053 observations
    df = initial_setup(df)
    df = change_columns(df)
    
    # after dropping duplicates and null values, we now have 28,021 observations
    df = drop_outliers(df, col_list)
    
    # after dropping outliers, we now have 23,937 observations
    
    return df

def zillow_split(df, target):
    '''
    args: df
    This function take in the zillow DataFrame after it has gone through prep_zillow,
    and splits into train, validate, and test X_df(features) and y (target).
    '''
    # first we need to drop 'tax_amount'
    df = df.drop(columns='tax_amount')
    
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=1221)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=1221)
    # Split into X and y
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test

def scale_zillow(X_train, X_validate, X_test, scaler, scaler_name):
    '''
    This function takes in train, validate, and test dataframes, as well as a list of columns to scale,
    the particular scaler to use, and the string name of the scaler to be added to the new dataframe. This will add scaled columns to the train, validate, and test DFs. Outputs the scaler so inverse transform can be performed later. outputs a list of the new column names.
    '''
    
    # define the scaler to be used...In this case MinMaxScaler
    mm_scaler = scaler
    
    # make empty list for return
    scaled_cols_list = []
    
    # What columns do we want to scale...
    cols_to_scale = ['sqft_calc', 'yearbuilt', 'age']
    
    # Run a loop through cols_to_scale
    for col in cols_to_scale:
        
        # fit and transform on X_train
        X_train[f'{col}_{scaler_name}'] = mm_scaler.fit_transform(X_train[[col]]) 
        
        # transform on X_validate and X_test
        X_validate[f'{col}_{scaler_name}']= mm_scaler.transform(X_validate[[col]])
        X_test[f'{col}_{scaler_name}']= mm_scaler.transform(X_test[[col]])
        
        #add new column name to the list that will get returned
        scaled_cols_list.append(f'{col}_{scaler_name}')
                     
        # returns the scaler, and list of scaled columns
    return scaler, scaled_cols_list
    
    
  

  





