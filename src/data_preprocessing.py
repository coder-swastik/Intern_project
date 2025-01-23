import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# def preprocess_data(df):
#     '''
#     if there is missing data and the row needed to be dropped, we can uncomment this code.
#     original = df.isnull()
#     df = df.dropna()
#     '''

#     ##the below code check whether there is any missing data and if there is any it fills the mising row with 0 or NaN
#     missing_values = df.isnull()
#     if missing_values.any().any():
#         st.write("Missing Values")
#     else:
#          st.write("No missing value")

#     for column in df.columns:
#         if df[column].dtype in ['float64', 'int64']:  
#             df[column] = df[column].fillna(df[column].mean())
#         else:
#             df[column] = df[column].fillna(df[column].mode([0]))

#         '''
#         filling missing value with previous or before row's value
#         for column in df.columns:
#         if df[column].dtype in ['float64', 'int64']:  
#             df[column] = df[column].fillna(method='pad')
#             or 
#             df[column] = df[column].replace(to_replace=np.na, value= 99)
#         else:
#             df[column] = df[column].fillna(method='bfill') 

#         '''


# here we use linear regression for data preprocessing 
def preprocess_data(df):
    '''
    Function to perform model-based imputation using linear regression for numerical columns.
    It predicts missing values based on other features in the dataset.
    '''
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:
            missing_data = df[df[column].isnull()]
            
            if not missing_data.empty:
                
                st.write(f"Processing missing values in column: {column}")
                
                # Drops rows where the target column is missing
                df_non_missing = df.dropna(subset=[column])
                
                # Features
                x = df_non_missing.drop(columns=[column])
                y = df_non_missing[column]

                # Handle missing values in features
                imputer = SimpleImputer(strategy='mean')
                x_imputed = imputer.fit_transform(x)
                
                # Train-test split
                X_train, X_test, y_train, y_test = train_test_split(x_imputed, y, test_size=0.2, random_state=42)

                # Create and fit the model
                model = LinearRegression()
                model.fit(X_train, y_train)

                # Predict missing values in the original data
                missing_data_x = missing_data.drop(columns=[column])
                missing_data_x_imputed = imputer.transform(missing_data_x)
                predicted_values = model.predict(missing_data_x_imputed)

                # Fill the missing values in the original DataFrame
                df.loc[missing_data.index, column] = predicted_values
                st.write("The values being feed into the tables are:")
                st.write(predicted_values)
            else:
                st.write(f"No missing values in column: {column}")

    return df
