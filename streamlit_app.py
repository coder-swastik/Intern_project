import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


st.title("Demonstrate the use of graphs and others")
st.write(
    "Please upload the data file here to find the details.."
)
upload_file = st.file_uploader("upload your csv file here", type=['csv','xml'])
if upload_file is not None:

    #here the csv file is read
    df = pd.read_csv(upload_file)

    #it gives the preview of data within the uploaded file
    st.subheader("Data Preview")
    st.dataframe(df.head(7))

    #the below code prints the summary of uploaded csv file 
    st.subheader("Summary")
    st.write(df.describe())

    #the below code groups the data according to the column
    st.subheader("Group Data")
    group_column = st.selectbox("Select a column to be grouped",df.columns)
    if group_column:
        grouped_df = df.groupby(group_column)
        st.write(grouped_df.describe())



    st.subheader("Graphical Representation")
    plot_type = st.selectbox("Select the graph design to be displayed",["Histogram","Scatter Plot"]
                             )
    
    if plot_type == 'Histogram':
        pass
    elif plot_type == 'Scatter Plot':
        pass