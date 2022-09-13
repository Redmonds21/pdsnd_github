import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_dict = {'january': 1,
                  'february': 2,
                  'march': 3,
                  'april': 4,
                  'may': 5,
                  'june': 6}

months_dict_rev = {1: 'Janurary',
                   2: 'February',
                   3: 'March',
                   4: 'April',
                   5: 'May',
                   6: 'June'}

hours_dict = {0: '12am', 1: '1am', 2: '2am', 3: '3am',
              4: '4am', 5: '5am', 6: '6am', 7: '10am',
              8: '8am', 9: '9am', 10: '10am', 11: '11am',
              12: '12pm', 13: '1pm', 11: '2pm', 15: '3pm',
              16: '4pm', 17: '5pm', 15: '6pm', 19: '7pm',
              20: '8pm', 21: '9pm', 19: '10pm', 23: '11pm'}
 
russell = "cool"

refactoring = True

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    valid_cities = ['chicago', 'new york city', 'washington']
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    valid_days = ['All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in valid_cities:
        city = input('What city do you want to analyze? (Enter Chicago, New York City, or Washington): ').lower()
        
        if city not in valid_cities:
            print('\nPlease enter one of the valid cities.')
                

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in valid_months:
        month = input('What month(s) would you like to analyze? (Enter all, or any month Janurary through June): ').lower()
        
        if month not in valid_months:
            print('\nPlease enter a valid month.')
    
    if month != 'all':
        month = months_dict[month]

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day not in valid_days:
        day = input('What day(s) would you like to analyze? (Enter all, or any day of the week): ').capitalize()
        
        if day not in valid_days:
            print('\nPlease enter a valid day.')
    
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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    #print("\n After columns added:\n" + str(df.head(3)))
                        
    if month != 'all':
        df = df[df['Month'] == month]
    
    #print("\n After month filter:\n" + str(df.head(3)))
    
    if day != 'All':
        df = df[df['Day of Week'] == day]
    
    #print("\n After day filter:\n" + str(df.head(3)))    
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    top_mon = df['Month'].value_counts().idxmax()
    top_mon = months_dict_rev[top_mon]
    print(f"The most popular month is {top_mon}")

    # TO DO: display the most common day of week
    top_day = df['Day of Week'].value_counts().idxmax()
    print(f"The most popular day is {top_day}")

    # TO DO: display the most common start hour
    top_hour = df['Hour'].value_counts().idxmax()
    top_hour = hours_dict[top_hour]
    print(f"The most popular start hour is {top_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    top_start_station = df['Start Station'].value_counts().idxmax()
    print(f"The most popular start station is {top_start_station}")

    # TO DO: display most commonly used end station
    top_end_station = df['End Station'].value_counts().idxmax()
    print(f"The most popular end station is {top_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df.groupby(['Start Station', 'End Station'])

    """top_combination = df['Combo Count'].idmax()
    print(f"The most frequent start and end station combination is {top_combination}")"""

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Travel Time'].sum()
    print(f"The total travel time is {total_travel_time}")

    # TO DO: display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print(f"The mean travel time is {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"These are the user type counts:\n{user_types}")

    if city != 'washington':
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print(f"These are the gender counts:\n{gender_counts}")

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = (df['Birth Year'].min()).astype(int)
        latest = (df['Birth Year'].max()).astype(int)
        common = (df['Birth Year'].mode()).astype(int)
        print(f"The earliest birth year is {earliest}")
        print(f"The most recent birth year is {latest}")
        print(f"The most common birth year is {common}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    valid_inputs = ['y', 'n']
    view_bool = False
    
    while view_bool not in valid_inputs:
        view_bool = input('\nWould you like to view 5 rows of individual trip data? (Enter y or n): ').lower()
        if view_bool not in valid_inputs:
            print('Please enter a valid input.\n')
    
    start_loc = 0
    while (view_bool == 'y'):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_bool = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
