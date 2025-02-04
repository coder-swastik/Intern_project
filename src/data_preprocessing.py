import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

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



##Mean/Mode based imputations
def preprocess_data(df,method ):

    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = df.select_dtypes(include=['object','category']).columns
    """
    Fill missing valus with mean for numerical columns and mode for categorical column
    """

    if method == 'Fill missing values withy Mean/Mode':
        st.write("Processing:filling missing values with mean/mode")
        for column in numerical_cols:
                df[column] = df[column].fillna(df[column].mean())



#here we use linear regression for data preprocessing 
# to clear more concepts in this section still needed
    elif method == 'Linear Regression-Based Imputation':
        '''
        Function to perform model-based imputation using linear regression for numerical columns.
        It predicts missing values based on other features in the dataset.
    '''
        for column in numerical_cols:
         missing_data = df[df[column].isnull()]
         if not missing_data.empty:
                
                    logs.append(f"Processing missing values in column: {column}")
                
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


## KNN-based imputations
    elif method == 'KNN-Based Imputations':
        st.write("KNN-based Imputations")
        imputer = KNNImputer(n_neighbors=5)
        df[numerical_cols] = imputer.fit_transform(df[numerical_cols])

#droping the row based on the user option selection
    elif method == 'Drop Rows With Missing Data':
        st.write("Dropping rows with missing data....")
        df = df.dropna()
    

    #Processing categorical data
    elif method == "Mode Imputation":
        st.write("Processing : Filling categorical missing value mode...")
        for column in categorical_cols:
            mode_value = df[column].mode()
            if not mode_value.empty:
                df[column]= df[column].fillna(mode_value.iloc[0]) ##confirming why this is being used...
    
    elif method == 'Forward Fill':
        st.write("Processing filling categorical missing values")
        df[categorical_cols]=df[categorical_cols].fillna(method='ffill')

    elif method == 'Fill with unkown':
        st.write("Processing: fillinf categorical missing value")
        df[categorical_cols] =df[categorical_cols].fillna("Unkonw ")

    elif method =="Drops rows with missing data":
        st.write("Dropping rows with missing data....")
        df = df.dropna()
    else:
        st.error("Invalid Preprocessing method selected.")
    
    

    ## Categorical data preprocessing
    # fill with unknown

    #drop Row

    #fill with the most frequent values


    #backward fill and forward fill


    #if the data is complex using knn imputation



    return df