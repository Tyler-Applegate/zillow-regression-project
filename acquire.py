# This is my acquire module for my Zillow Regression Project

# This is my acquire module for my Zillow Regression Project

########################### General Imports ####################################
import pandas as pd
import numpy as np
import os

############### Connection #####################################################

# Enables access to my env.py file in order to use sensitive info to access Codeup DB
from env import host, user, password

# sets up a secure connection to the Codeup db using my login infor
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my env file to create a connection url to access
    the Codeup database.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

########### Acquisition ##################################################

def new_zillow_data():
    '''
    gets zillow information from CodeUp db using SQL query
    and creates a dataframe
    '''

    # SQL query
    zillow_query = '''
                    SELECT parcelid AS parcel_id,
                    bathroomcnt AS bath, 
                    bedroomcnt AS bed, 
                    calculatedfinishedsquarefeet AS sqft_calc, 
                    fips, 
                    yearbuilt, 
                    taxvaluedollarcnt AS appraised_value, 
                    taxamount AS tax_amount
                    FROM properties_2017
                    JOIN predictions_2017 USING (parcelid)
                    WHERE transactiondate BETWEEN "2017-05-01" AND "2017-08-31"
                    AND propertylandusetypeid IN 261
                    '''
    
    # reads SQL query into a DataFrame            
    df = pd.read_sql(zillow_query, get_connection('zillow'))
    
    return df

def get_zillow_data():
    '''
    checks for existing csv file
    loads csv file if present
    if there is no csv file, calls new_zillow_data
    '''
    
    if os.path.isfile('zillow.csv'):
        
        df = pd.read_csv('zillow.csv', index_col=0)
        
    else:
        
        df = new_zillow_data()
        
        df.to_csv('zillow.csv')

    return df