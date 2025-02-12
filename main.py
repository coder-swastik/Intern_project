import streamlit as st
import pandas as pd
from src import rule_based_preprocess, display_data

def load_csv(file):
    return pd.read_csv(file)

def load_excel(file):
    return pd.read_excel(file)

def main():
    
    st.title("Data Preprocessing and Visualization")
    st.write("Please upload a CSV or Excel file to analyze.")

    upload_file = st.file_uploader("Upload your CSV or xlsx file here", type=['csv', 'xlsx'])

    if upload_file is not None:
        file_type = upload_file.name.split('.')[-1]

        if file_type == 'csv':
            df = load_csv(upload_file)
        elif file_type == 'xlsx': 
            df = load_excel(upload_file)
        else:
            st.error("Unsupported file format")
            st.stop()

        st.write("File uplodaed successfully")
        #here the df is sent for preprocessing for any missing values
        # st.write("Select a method to handle misssing data")
        # preprocess_method = st.selectbox('Choose a preprocessing method',
        #                                  options =[
        #                                      "Fill missing values withy Mean/Mode",
        #                                      'Linear Regression-Based Imputation',
        #                                      'KNN-Based Imputations',
        #                                      "Drop Rows With Missing Data",
        #                                      'Forward Fill',
        #                                      'Fill with unkown',
        #                                      "Drops rows with missing data"
        #                                  ])

        df = rule_based_preprocess(df)
        #here the df is sent for display
        display_data(df)

        # if st.button("Run Preprocessing"):
        #     df= preprocess_data(df,preprocess_method)
        #     st.success("Data preprocessing completed!")
 
        #     st.write("Here is the preprocessed data:")
        #     st.dataframe(df.head())

        # if st.button("Display Visualization"):
        #     st.write("Visualizing the preprocessed Data:")
        #     display_data(df)

main()