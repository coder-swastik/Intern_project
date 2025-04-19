import streamlit as st
import pandas as pd
from .knnimputation import KNNImputation
from .linear_regression_imputation import LinearRegressionImputation
from .modeImputation import ModeImputation
from .impute_decorator import imputation_decorator
from .time_stamp import preprocess_timestamp

@imputation_decorator(LinearRegressionImputation)
def linear_regression_imputation(df, column):
    st.write("Linear regression function is being called")

@imputation_decorator(KNNImputation)
def knn_imputation(df, column):
    st.write("KNN-based imputation function is being called")

@imputation_decorator(ModeImputation)
def mode_imputation(df, column):
    st.write("Mode-based imputation is being called.")

# def is_timestamp_column(column):
#     try:
#         pd.to_datetime(column, errors='raise')
#         return True
#     except (ValueError, TypeError):
#         return False

def rule_based_preprocess(df):
    timestamp_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
    df = df.drop(columns=timestamp_cols, errors='ignore')

    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = df.select_dtypes(include=['object',  'category']).columns
    
    
    st.write("Rule-Based Data Preprocessing...")

    # for column in timestamp_cols:
    #     st.write(f"Processing timestamp column: {column}")
    #     preprocess_timestamp(df,column)
    #     st.write(f"Processed {column} successfully")

    # Processing numerical columns
    for column in numerical_cols:
            missing_count = df[column].isnull().sum()
            st.write(f"Processing numerical column: {column}, Missing values: {missing_count}")
            if missing_count > 0:
                row_count = len(df)
                if row_count < 1000:
                    linear_regression_imputation(df, column)
                elif 1000 <= row_count <= 5000:
                    knn_imputation(df, column)
                else:
                    st.write(f"Dropping rows with missing values in column: {column}")
                    df.dropna(subset=[column], inplace=True)

    # Processing categorical columns
    for column in categorical_cols:
  
            missing_count = df[column].isnull().sum()
            st.write(f"Processing categorical column: {column}, Missing values: {missing_count}")
            if missing_count > 0:
                row_count = len(df)
                if row_count < 1000:
                    mode_imputation(df, column)
                elif 1000 <= row_count <= 5000:
                    st.write(f"Using Forward Fill for column: {column}")
                    df[column].fillna(method='ffill', inplace=True)
                else:
                    st.write(f"Dropping rows with missing values in column: {column}")
                    df.dropna(subset=[column], inplace=True)



    return df
