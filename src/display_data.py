import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def display_data(df):
    st.write("Diaplay function is being called")
    st.dataframe(df.head())
    st.subheader('Summary')
    st.write(df.describe())
    st.write(df.dtypes)

    # here we identify the categorical and numerical column
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

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
                plt.bar(value_counts.index, value_counts.values)
                plt.title(f"Bar chart of {column}")
                plt.xlabel(column)
                plt.ylabel('Frequency')
                plt.xticks(rotation=60, fontsize=10, ha="right") 
                plt.tight_layout()
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
            numerical_col = numerical_cols[0]
            if plot_type == 'Bar':
                st.write(f"Bar diagram for {column} vs {numerical_col}")
                plt.figure(figsize=(14, 6))
                sns.barplot(x=column, y=numerical_col, data=df)
                plt.title(f"Bar chart of {column} vs {numerical_col}")
                plt.xlabel(column)
                plt.ylabel(numerical_col)
                st.pyplot(plt)

           
            if plot_type == 'Line':
                st.write(f"Line diagram for {column} vs {numerical_col}")
                plt.figure(figsize=(10, 8))
                sns.lineplot(x=column, y=numerical_col, data=df)
                plt.title(f"Line chart of {column} vs {numerical_col}")
                plt.xlabel(column)
                plt.ylabel(numerical_col)
                st.pyplot(plt)

            if plot_type == 'Pie':
                st.write(f"Pie diagram for {column} vs {numerical_col}")
                plt.figure(figsize=(10, 8))
                df_grouped = df.groupby(column)[numerical_col].sum().reset_index()
                plt.pie(df_grouped[numerical_col], labels=df_grouped[column], autopct='%1.1f%%')
                plt.title(f"Pie chart of {column} vs {numerical_col}")
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

        if categorical_cols.empty and data_type == 'Categorical':
            st.warning("No categorical columns available for visualization")
        if numerical_col.empyt and data_type == 'Numerical':
            st.warning("No numerical columnns available for visualization")