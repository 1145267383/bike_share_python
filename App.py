import streamlit as st
import pandas as pd
import bikeshare  # Importing the existing bikeshare script

# Streamlit page config
st.set_page_config(page_title="BikeShare Data Explorer", layout="wide")

# Title
st.title("🚲 US BikeShare Data Explorer")
st.markdown("Analyze bike share data from **Chicago, New York City, and Washington**.")

# Sidebar for filters
st.sidebar.header("🔍 Select Filters")

# City selection
city_map = {
    "Chicago": "chicago",
    "New York City": "new york city",
    "Washington": "washington"
}
city = st.sidebar.selectbox("🏙️ Choose a city:", list(city_map.keys()))

# Filter options
filter_type = st.sidebar.radio("🛠️ Choose filter type:", ["No Filter", "Month", "Day", "Month & Day"])

# Month selection
month = "all"
if filter_type in ["Month", "Month & Day"]:
    month_map = {
        "January": "january", "February": "february", "March": "march",
        "April": "april", "May": "may", "June": "june"
    }
    month = st.sidebar.selectbox("📅 Choose a month:", list(month_map.keys()))

# Day selection
day = "all"
if filter_type in ["Day", "Month & Day"]:
    day_map = {
        "Sunday": "Sunday", "Monday": "Monday", "Tuesday": "Tuesday",
        "Wednesday": "Wednesday", "Thursday": "Thursday", "Friday": "Friday", "Saturday": "Saturday"
    }
    day = st.sidebar.selectbox("📆 Choose a day:", list(day_map.keys()))

# Load data
df = bikeshare.load_data(city_map[city], month, day)

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
if st.checkbox("👀 Show Raw Data"):
    st.write(df.head(10))

# Restart button
if st.button("🔄 Restart Analysis"):
    st.experimental_rerun()
