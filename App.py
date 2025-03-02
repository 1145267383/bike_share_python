import streamlit as st
import pandas as pd
from bikeshare import get_filters, load_data, time_stats, station_stats, trip_duration_stats, user_stats

def main():
    st.title("US Bikeshare Data Analysis")
    st.write("Explore bikeshare data for Chicago, New York City, and Washington.")
    
    # User inputs
    city_options = {'Chicago': 'chicago', 'New York City': 'new york city', 'Washington': 'washington'}
    city = st.selectbox("Select a city:", list(city_options.keys()))
    city = city_options[city]
    
    filter_option = st.radio("Select a filter type:", ['No Filter', 'Month', 'Day', 'Both'])
    month, day = 'all', 'all'
    
    if filter_option in ['Month', 'Both']:
        month_options = {'January': 'january', 'February': 'february', 'March': 'march', 'April': 'april', 'May': 'may', 'June': 'june'}
        month = st.selectbox("Select a month:", list(month_options.keys()))
        month = month_options[month]
    
    if filter_option in ['Day', 'Both']:
        day_options = {'Sunday': 'Sunday', 'Monday': 'Monday', 'Tuesday': 'Tuesday', 'Wednesday': 'Wednesday', 'Thursday': 'Thursday', 'Friday': 'Friday', 'Saturday': 'Saturday'}
        day = st.selectbox("Select a day:", list(day_options.keys()))
        
    # Load and display data
    df = load_data(city, month, day)
    
    if st.checkbox("Show raw data"):
        st.write(df.head())
    
    st.subheader("Statistics")
    if st.button("Show Time Stats"):
        time_stats(df)
    if st.button("Show Station Stats"):
        station_stats(df)
    if st.button("Show Trip Duration Stats"):
        trip_duration_stats(df)
    if st.button("Show User Stats"):
        user_stats(df)

if __name__ == "__main__":
    main()
