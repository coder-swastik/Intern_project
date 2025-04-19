import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def display_data(df):
    st.write("Display function is being called")
    st.dataframe(df.head())
    st.subheader('Summary Statistics')
    st.write(df.describe())

    # here we identify the categorical and numerical column
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns


    data_type = st.selectbox("Select data type for visualization", ['Categorical', 'Numerical', 'Correlation Heatmap', 'Pair Plot'])

    if data_type == 'Categorical' and not categorical_cols.empty:
        column = st.selectbox("Select the categorical column", categorical_cols)
        plot_type = st.selectbox("Select the plot type", ['Bar', 'Line', 'Pie','Count Plot'])

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
                plt.pie(value_counts.values, labels=value_counts.index,autopct='%1.1f%%',startangle=140)
                plt.title(f"Pie chart of {column}")
                st.write("### Insights:")
                total_values = value_counts.sum()
                top_value = value_counts.index[0]
                top_percentage = (value_counts.values[0] / total_values) * 100
                st.write(f"- The most frequent category is **{top_value}**, making up **{top_percentage:.2f}%** of the total.")
                st.pyplot(plt)
            
            if plot_type == 'Count Plot':
                st.write(f"Count plot for {column}")
                plt.figure(figsize=(12,6))
                sns.countplot(x=column,data=df)
                plt.title(f"Count plot of {column}")
                plt.xticks(rotation=60, fontsize=10, ha="right")
                plt.tight_layout()
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
                plt.xticks(rotation=60, fontsize=10, ha="right") 
                plt.tight_layout()
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

            if plot_type == 'Count Plot':
                st.write(f"Count plot for {column}")
                plt.figure(figsize=(12,6))
                sns.countplot(x=column,data=df)
                plt.title(f"Count plot of {column}")
                plt.xticks(rotation=60, fontsize=10, ha="right")
                plt.tight_layout()
                st.pyplot(plt)

    elif data_type == 'Numerical' and not numerical_cols.empty:
        column = st.selectbox("Select the numerical data column", numerical_cols)
        plot_type = st.selectbox("Select the plot type", ['Histogram', 'Box Plot', 'Line Plot'])

        if plot_type =="Histogram":
            st.write(f"Displaying Histogram for {column}")
            plt.figure(figsize=(10, 8))
            plt.hist(df[column].dropna(), bins=20)
            plt.title(f"Histogram of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            st.pyplot(plt)

        if plot_type == 'Box Plot':
            st.write(f"Displaying Box Plot for {column}")
            plt.figure(figsize=(10, 6))
            sns.boxplot(y=df[column])
            plt.title(f"Box plot of {column}")
            st.pyplot(plt)

        if plot_type == 'Line Plot':
            st.write(f"Displaying Line Plot for {column}")
            plt.figure(figsize=(12, 6))
            plt.plot(df[column].dropna(), marker='o', linestyle='-')
            plt.title(f"Line plot of {column}")
            plt.xlabel('Index')
            plt.ylabel(column)
            st.pyplot(plt)

    elif data_type == 'Correlation Heatmap':
        st.write("Correlation Heatmap for Numerical Features")
        corr = df[numerical_cols].corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Correlation Heatmap")
        st.pyplot(plt)

    elif data_type == 'Pair Plot':
        st.write("Pair Plot for Numerical Features")
        selected_cols = st.multiselect("Select numerical columns for pair plot (2 or more)", numerical_cols)
        if len(selected_cols) >= 2:
            sns.pairplot(df[selected_cols])
            st.pyplot(plt)
        else:
            st.warning("Please select at least two numerical columns for the pair plot.")

   