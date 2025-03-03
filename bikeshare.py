import time
import pandas as pd
import numpy as np
import streamlit as st

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (c) city - name of the city to analyze
        (m) month - name of the month to filter by, or "all" to apply no month filter
        (d) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    citys = {'co': 'chicago', 'nyc': 'new york city', 'wn': 'washington'}
    c = input("Choose which city you want to see its data('co=chicago', 'nyc=new york city', 'wn=washington') ?").lower()
    while c not in citys.keys():
        print("this is invalid value")
        c = input("Choose which city you want to see its data('co=chicago', 'nyc=new york city', 'wn=washington') ?").lower()
        
    city = citys[c]
        
    filters = {'mh': 'month', 'dy': 'days', 'to': 'together', 'no': 'nofilter'}
    f = input("Choose the filter you like betown from ('mh=month', 'dy=days', 'to=together', 'no': 'nofilter')? ").lower()
    while f not in filters.keys():
        print("this is invalid value")
        f = input("Choose the filter you like betown from('mh=month', 'dy=days', 'to=together', 'no': 'nofiler') ? ").lower()
    filter = filters[f]

 # get user input for month (all, january, february, ... , june)
   
    if filter == ('month') or filter == ('together'): 
        months = {'jy': 'january', 'fy': 'february', 'mh': 'march', 'al':'april', 'my': 'may', 'je': 'june'}
        m = input("Choose a day {'jy=January', 'fy=February', 'mh=March', 'al=April', 'my=May', 'je=June', ) ? ").lower()
        while m not in months.keys():
            print("this is invalid value")
            m = input("Choose betown {'jy=January', 'fy=February', 'mh=March', 'al=April', 'my=May', 'je=June', ) ? ").lower()
        month = months[m]
    else:
        month = ('all')
  # get user input for day of week (all, monday, tuesday, ... sunday)
    if filter == ('day') or filter == ('together'):
        days = {'SU': 'Sunday', 'MO': 'Monday', 'TU': 'Tuesday', 'WE': 'Wednesday', 'TH': 'Thursday', 'FR': 'Friday', 'SA': 'Saturday'}
        d = input("Choose betown ('SU=Sunday', 'MO=Monday', 'TU=Tuesday', 'WE=Wednesday', 'TH=Thursday', 'FR=Friday', 'SA=Saturday') ? ").upper()
        while d not in days.keys():
            print("this is invalid value")
            d = input("Choose betown ('SU=Sunday', 'MO=Monday', 'TU=Tuesday', 'WE=Wednesday', 'TH=Thursday', 'FR=Friday', 'SA=Saturday') ? ").upper()    
        day = days[d]
    else:
        day = ('all')
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month']==month] 

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    st.write('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    popular_month = df['month'].mode()[0]
    st.write('Most Frequent month: ', months[popular_month-1])
    
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    st.write('Most Frequent day of weeek:', popular_day)
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    st.write('Most Frequent Start Hour: ', popular_hour)
    
    st.write("\nThis took %s seconds." % (time.time() - start_time))
    st.write('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    st.write('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    st.write('Most Frequent start station: ', start_station)
    
    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    st.write('Most Frequent end station: ', end_station)
    
    # display most frequent combination of start station and end station trip
    if end_station < start_station:
        start_end_station = start_station
    else:
        start_end_station = end_station

    st.write('Most Frequentcombination of start station and end station trip: ', start_end_station)

    st.write("\nThis took %s seconds." % (time.time() - start_time))
    st.write('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    st.write('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    st.write('Total travel time is: ', total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    st.write('Mean travel time is: ', mean_travel_time)

    st.write("\nThis took %s seconds." % (time.time() - start_time))
    st.write('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    st.write('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    st.write('The numbers of users types is: ', counts_user_types)
    
    # Display counts of gender
    if 'Gender' in(df.columns): 
        counts_gender = df['Gender'].value_counts()
        st.write('The numbers of users gender is: ', counts_gender)
    # Display earliest, most recent, and most common year of birth
    if 'Gender' in(df.columns):
        earliest = df['Birth Year'].min()
        st.write('Earliest year of birth is: ',earliest)
        most_recent = df['Birth Year'].max()
        st.write('Most recent year of birth is: ',most_recent)
        most_common = df['Birth Year'].mode()[0]
        st.write('Most common year of birth is: ',most_common)   

    
    st.write("\nThis took %s seconds." % (time.time() - start_time))
    st.write('-'*40)
    # save the output to a file

def display(df):
    """Displays 5 rows of individual trip data."""
    
    print('\nview 5 rows of trip data...\n')
    view_data = input("\nWould you like to view 5 rows of individual trip data? Enter 'yes' or 'no' ?\n").lower()
    start_loc = 0
    while (view_data == "yes"):
        print(df.iloc[(start_loc): (start_loc+5)])
        start_loc += 5
        view_data = input("\nDo you wish to continue? Enter 'yes' or 'no' ?\n").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)

        restart = input("\nWould you like to restart? Enter 'yes' or 'no'?\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
