import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def display_data(df):
    st.dataframe(df.head())
    st.subheader('Summary')
    st.write(df.describe())

    category_col = df.columns[0]
    value_col = df.columns[1]  

    data_type = st.selectbox("Select data type for visualization", ['Categorical', 'Numerical'])

    if data_type == 'Categorical':
        categorical_columns = df.select_dtypes(include=['object']).columns
        column = st.selectbox("Select the categorical column", categorical_columns)

        plot_type = st.selectbox("Select the plot type", ['Bar', 'Line', 'Pie'])

        if df[column].duplicated().any():  
            if plot_type == 'Bar':
                st.write(f"Bar diagram for {column}")
                plt.figure(figsize=(14, 6))
                value_counts = df[column].value_counts()  
                plt.bar(value_counts.index, value_counts.values, width=0.6)
                plt.title(f"Bar chart of {column}")
                plt.xlabel(column)
                plt.ylabel('Frequency')
                st.pyplot(plt)

            
            if plot_type == 'Line':
                st.write(f"Line diagram for {column}")
                plt.figure(figsize=(10, 8))
                value_counts = df[column].value_counts()
                plt.plot(value_counts.index, value_counts.values, marker='o', linestyle='dashed')
                plt.title(f"Line chart of {column}")
                plt.xlabel(column)
                plt.ylabel('Frequency')
                st.pyplot(plt)

            
            if plot_type == 'Pie':
                st.write(f"Pie diagram for {column}")
                plt.figure(figsize=(10, 8))
                value_counts = df[column].value_counts()
                plt.pie(value_counts.values, labels=value_counts.index)
                plt.title(f"Pie chart of {column}")
                st.pyplot(plt)

        else:  
            if plot_type == 'Bar':
                st.write(f"Bar diagram for {column}")
                plt.figure(figsize=(14, 6))
                plt.bar(df[category_col], df[value_col], width=0.6)
                plt.title(f"Bar chart of {column}")
                plt.xlabel(column)
                plt.ylabel('Frequency')
                st.pyplot(plt)

           
            if plot_type == 'Line':
                st.write(f"Line diagram for {column}")
                plt.figure(figsize=(10, 8))
                plt.plot(df[category_col], df[value_col], marker='o', linestyle='dashed')
                plt.title(f"Line chart of {column}")
                plt.xlabel(column)
                plt.ylabel('Frequency')
                st.pyplot(plt)

            if plot_type == 'Pie':
                st.write(f"Pie diagram for {column}")
                plt.figure(figsize=(10, 8))
                plt.pie(df[value_col], labels=df[category_col], autopct='%1.1f%%')
                plt.title(f"Pie chart of {column}")
                st.pyplot(plt)

    elif data_type == 'Numerical':
        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
        column = st.selectbox("Select the numerical data column", numerical_columns)

        st.write(f"Displaying Histogram for {column}")
        plt.figure(figsize=(10, 8))
        plt.hist(df[column].dropna(), bins=20)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        st.pyplot(plt)
