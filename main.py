import streamlit as st
import pandas as pd
from docx import Document
from src.data_processing import rule_based_preprocess,text_preprocessing
from src.data_display import display_data
from src.data_processing.text_preprocessing import preprocess

def load_csv(file):
    return pd.read_csv(file)

def load_excel(file):
    return pd.read_excel(file)

def load_text(file):
    text = file.read().decode('utf-8')
    return text

def load_docx(file):
    doc = Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def main():
    st.title("Data Preprocessing and Visualization")
    st.write("Please upload a CSV or Excel or Docs file to analyze.")

    upload_file = st.file_uploader("Upload your CSV or xlsx or docx or txt file here", type=['csv', 'xlsx','docx','txt'])

    if upload_file is not None:
        file_type = upload_file.name.split('.')[-1]

        if file_type in ['csv','xlsx']:
            df = load_csv(upload_file) if file_type =='csv' else load_excel(upload_file)
            st.write("File uploaded successfully")
            df= rule_based_preprocess(df)
            display_data(df)
        elif file_type in ['docx','txt']:
            text = load_docx(upload_file) if file_type == 'docx' else load_text(upload_file)
            processed_text = preprocess(text)
            st.write("Processing Text output:")
            st.write(processed_text)
        else:
            st.error("Unsupported file format")
            st.stop()
main()
