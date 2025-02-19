import streamlit as st
import pandas as pd
from docx import Document
from src.data_processing.data_preprocessing import rule_based_preprocess
from src.data_display.display_data import display_data

def load_csv(file):
    return pd.read_csv(file)

def load_excel(file):
    return pd.read_excel(file)

def load_docx(file):
    doc = Document(file)
    st.write("Reading docx file")
    return doc

def main():
    st.title("Data Preprocessing and Visualization")
    st.write("Please upload a CSV or Excel or Docs file to analyze.")

    upload_file = st.file_uploader("Upload your CSV or xlsx file here", type=['csv', 'xlsx','docx'])

    if upload_file is not None:
        file_type = upload_file.name.split('.')[-1]

        if file_type == 'csv':
            df = load_csv(upload_file)
        elif file_type == 'xlsx': 
            df = load_excel(upload_file)
        elif file_type == 'docx':
            doc_text = load_docx(upload_file)
        else:
            st.error("Unsupported file format")
            st.stop()

        st.write("File uploaded successfully")
        df = rule_based_preprocess(df)
        display_data(df)

main()
