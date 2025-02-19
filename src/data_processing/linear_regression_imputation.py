import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import streamlit as st
from src.abc.impute_abc import Imputation

class LinearRegressionImputation(Imputation):
    def apply(self, df, column):
        numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
        missing_data = df[df[column].isnull()]
        if not missing_data.empty:
            df_non_missing = df.dropna(subset=[column])
            X = df_non_missing.drop(columns=column)
            y = df_non_missing[column]

            imputer = SimpleImputer(strategy='mean')
            X_imputed = imputer.fit_transform(X)

            X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)
            model = LinearRegression()
            model.fit(X_train, y_train)

            missing_data_X = missing_data.drop(columns=[column])
            missing_data_X_imputed = imputer.transform(missing_data_X)
            predicted_values = model.predict(missing_data_X_imputed)

            df.loc[missing_data.index, column] = predicted_values
