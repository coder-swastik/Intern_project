from sklearn.impute import KNNImputer
import streamlit as st
from src.abc.impute_abc import Imputation

class KNNImputation(Imputation):
    def apply(self, df, column):
        st.write(f"Applying KNN Imputation on column: {column}")
        imputer = KNNImputer(n_neighbors=5)
        df[column] = imputer.fit_transform(df[[column]])
