import streamlit as st
from src.data_processing.knnimputation import KNNImputation
from src.data_processing.linear_regression_imputation import LinearRegressionImputation
from src.data_processing.modeImputation import ModeImputation
from src.data_processing.impute_decorator import imputation_decorator

@imputation_decorator(LinearRegressionImputation)
def linear_regression_imputation(df, column):
    st.write("Linear regression function is being called")

@imputation_decorator(KNNImputation)
def knn_imputation(df, column):
    st.write("KNN-based imputation function is being called")

@imputation_decorator(ModeImputation)
def mode_imputation(df, column):
    st.write("Mode-based imputation is being called.")

def rule_based_preprocess(df):
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    st.write("Rule-Based Data Preprocessing...")

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
