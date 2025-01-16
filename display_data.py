import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def display_data(df):
    st.dataframe(df.head())
    st.subheader('Summary')
    st.write(df.describe())



    data_type = st.selectbox("Select data type for visulization",['Categorial','Numerical'])

    if data_type == 'Categorial':
        categorical_columns = df.select_dtypes(include =['object']).columns
        column = st.selectbox("Select the categorical column",categorical_columns)

        plot_type = st.selectbox("Select the plot type",['Bar','Line','pie'])

        if plot_type == 'Bar':
            st.write(f"Bar diagram for {column}")
            plt.figure(figsize=(10,8))
            df[column].value_counts().plot(kind='bar')
            plt.title(f"Bar chart of {column}")
            plt.xlabel(column)
            plt.ylabel('Frequency')
            st.pyplot(plt)

        elif plot_type == 'Line':
            st.write(f"Line diagram for {column}")
            plt.figure(figsize=(10,8))
            df[column].value_counts().plot(kind='line', marker='o')
            plt.title(f"Line chart of {column}")
            plt.xlabel(column)
            plt.ylabel('Frequency')
            st.pyplot(plt)

        elif plot_type == 'pie':
            st.write(f"Pie diagram for {column}")
            plt.figure(figsize=(10,8))
            df[column].value_counts().plot(kind='pie')
            plt.title(f"Pie chart of {column}")
            plt.xlabel(column)
            plt.ylabel('Frequency')
            st.pyplot(plt)
    elif data_type == 'Numerical':
        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
        column = st.selectbox("Select the numerical data column", numerical_columns)

        st.write(f"Displaying Histogram for {column}")
        plt.figure(figsize=(10,8))
        plt.hist(df[column].dropna(),bins=20)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        st.pyplot(plt)