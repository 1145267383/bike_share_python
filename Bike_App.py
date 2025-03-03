import streamlit as st
import pandas as pd
import bikeshare  # Importing the existing bikeshare script

# Streamlit page config
st.set_page_config(page_title="BikeShare Data Explorer", layout="wide")

# Title
st.title("🚲 Hello! Let\'s Explore Some US Bikeshare Data!")
st.markdown("Analyze bike share data from **Chicago, New York City, and Washington**.")

# Sidebar for filters
st.sidebar.header("🔍 Select Filters")

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
months = [ "All",'January', 'February', 'March', 'April', 'May', 'June']
days= [ "All", 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

filters= ["No Filter", "Day", "Month", "Day & Month"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (c) city - name of the city to analyze
        (m) month - name of the month to filter by, or "all" to apply no month filter
        (d) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington).
    city = st.sidebar.selectbox("🏙️ Choose a city:", list(CITY_DATA.keys())).lower()

    # Filter options
    filter_type = st.sidebar.radio("🛠️ Choose filter type:", filters)


    # Month selection
    if filter_type in ["Month", "Day & Month"]:

        month = st.sidebar.selectbox("📅 Choose a month:", months).lower()
    else:
        month = "all"

    # Day selection
    if filter_type in ["Day", "Day & Month"]:

        day = st.sidebar.selectbox("📆 Choose a day:", days).lower()
    else:
        day = "all"


    return city, month, day


# Load data
city, month, day = get_filters()
df = bikeshare.load_data(city, month, day)

# Display dataset summary
st.subheader("📊 Data Overview")
st.write(df.head())

# Display statistics
st.subheader("📈 Time Statistics")
bikeshare.time_stats(df)

st.subheader("🚉 Station Statistics")
bikeshare.station_stats(df)

st.subheader("⏳ Trip Duration Statistics")
bikeshare.trip_duration_stats(df)

st.subheader("👥 User Statistics")
bikeshare.user_stats(df)


# Display raw data option
if st.checkbox("👀 Show Summary of data"):
    st.write(df.describe())

# Restart button
if st.button("🔄 Restart Analysis"):
    st.rerun()
