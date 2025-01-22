import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def preprocess_data(df):
    '''
    if there is missing data and the row needed to be dropped, we can uncomment this code.
    original = df.isnull()
    df = df.dropna()
    '''

    ##the below code check whether there is any missing data and if there is any it fills the mising row with 0 or NaN
    missing_values = df.isnull()
    if missing_values.any().any():
        st.write("Missing Values")
    else:
         st.write("No missing value")

    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:  
            df[column] = df[column].fillna(0)
        else:
            df[column] = df[column].fillna(pd.NA)

        '''
        filling missing value with previous or before row's value
        for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:  
            df[column] = df[column].fillna(method='pad')
            or 
            df[column] = df[column].replace(to_replace=np.na, value= 99)
        else:
            df[column] = df[column].fillna(method='bfill') 
        '''


    return df
