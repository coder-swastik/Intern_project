import streamlit as st
import pandas as pd
from src import preprocess_data, display_data


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


        #here the df is sent for preprocessing for any missing values
        df = preprocess_data(df)
    
        #here the df is sent for display
        display_data(df)

main()