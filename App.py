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

def get_filters():
    city = st.sidebar.selectbox("🏙️ Choose a city:", list(city_map.keys()))

    # Filter options
    filter_type = st.sidebar.radio("🛠️ Choose filter type:", ["No Filter", "Day", "Month", "Day & Month"])

    # Month selection
    month = "all"
    if filter_type in ["Month", "Day & Month"]:
        month_map = {
            "January": "january", "February": "february", "March": "march",
            "April": "april", "May": "may", "June": "june"
        }
        month = st.sidebar.selectbox("📅 Choose a month:", list(month_map.keys()))

    # Day selection
    day = "all"
    if filter_type in ["Month", "Day & Month"]:
        day_map = {
            "Sunday": "Sunday", "Monday": "Monday", "Tuesday": "Tuesday",
            "Wednesday": "Wednesday", "Thursday": "Thursday", "Friday": "Friday", "Saturday": "Saturday"
        }
        day = st.sidebar.selectbox("📆 Choose a day:", list(day_map.keys()))


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

restart = st.sidebar.selectbox("Would you like to restart?", ['yes' ,'no'])
if restart == 'yes':
    bikeshare.main()

# Display raw data option
if st.checkbox("👀 Show Raw Data"):
    st.write(df.head(10))

# Restart button
if st.button("🔄 Restart Analysis"):
    st.experimental_rerun()
