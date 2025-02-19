import streamlit as st
from src.abc.impute_abc import Imputation

class ModeImputation(Imputation):
    def apply(self, df, column):
        st.write(f"Applying Mode Imputation on column: {column}")
        mode_value = df[column].mode()
        if not mode_value.empty:
            df[column].fillna(mode_value.iloc[0], inplace=True)
