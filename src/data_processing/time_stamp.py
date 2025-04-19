import pandas as pd
import streamlit as st

def preprocess_timestamp(df,timestamp_column,timezone ='UTC',resample_freq= None):
    if timestamp_column not in df.columns:
        st.warning(f'Timestamp column {timestamp_column} not found in the dataset')
        return df
    
    #convert to datetime
    df[timestamp_column] = pd.to_datetime(df[timestamp_column], errors='coerce')

    #drop missing timestamps
    df = df.dropna(subset =[timestamp_column])

    #conver to UTC 
    df[timestamp_column] = df[timestamp_column].dt.tz_localize(None).dt.tz_localize(timezone)

     # Extract useful features
    df['year'] = df[timestamp_column].dt.year
    df['month'] = df[timestamp_column].dt.month
    df['day'] = df[timestamp_column].dt.day
    df['hour'] = df[timestamp_column].dt.hour
    df['minute'] = df[timestamp_column].dt.minute
    df['second'] = df[timestamp_column].dt.second
    df['weekday'] = df[timestamp_column].dt.day_name()


    # Remove duplicates
    df = df.drop_duplicates(subset=[timestamp_column])

    # Sort by timestamp
    df = df.sort_values(by=timestamp_column)

    # Resample if needed
    if resample_freq:
        df = df.set_index(timestamp_column).resample(resample_freq).first().reset_index()

    return df