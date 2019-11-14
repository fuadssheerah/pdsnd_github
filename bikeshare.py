import pandas as pd
import itertools
import time

# CITY_DATA is a dictionary that connect city name with their CSV data file.
CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}
# months and days are a list that provides all options that user can chose from .
months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_filters():
    """
      Asks user to specify a city, month, and day to analyze.

      Returns:
          (str) city - name of the city to analyze
          (str) month - name of the month to filter by, or "all" to apply no month filter
          (str) day - name of the day of week to filter by, or "all" to apply no day filter
      """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("\nPlease choose from available cities provides !!!\n")
            pass
    while True:
        month = input('\nWhich month? January, February, March, April, May, June or all?\n').title()
        if month in months:
            break
        else:
            print('Please choose from available months provides !!!')
            pass
    while True:
        day = input("Which day ? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday , Sunday or All to "
                    "display data of all days?\n").title()
        if day in days:
            break
        else:
            print('Please choose from available days provides !!!')
            pass
    print('-' * 40)
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
    df['Month'] = df['Start Time'].dt.month_name()
    df['Start hour'] = df['Start Time'].dt.hour
    df['End hour'] = df['End Time'].dt.hour
    df['day of week'] = df['Start Time'].dt.weekday_name
    if month != 'All':
        df = df[df['Month'] == month]
    if day != 'All':
        df = df[df['day of week'] == day]
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    if month == 'All':
        most_common_month = df['Month'].mode()[0]
        print('Most common month is ( {} ) .'.format(most_common_month))
    if day == 'All':
        most_common_day = df['day of week'].mode()[0]
        print('Most common day is ( {} ) .'.format(most_common_day))
    most_common_start_hour = df['Start hour'].mode()[0]
    print('Most popular hour is ( {} ) .'.format(most_common_start_hour))
    most_common_end_hour = df['End hour'].mode()[0]
    print('Most common end hour is ( {} ) .'.format(most_common_end_hour))
    print ( "\nThis took %s seconds." % (time.time () - start_time) )
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    most_common_start_station = df['Start Station'].mode()[0]
    print('\nMost common start station used is ( {} ) .'.format(most_common_start_station))
    most_common_end_station = df['End Station'].mode()[0]
    print('\nMost common end station used is ( {} ) .'.format(most_common_end_station))
    combination_trip = df['Start Station'].astype(str) + ' to ' + df['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().index[0]
    print('\nMost popular trip is from ( {} ) .\n'.format(most_frequent_trip))
    print ( "\nThis took %s seconds." % (time.time () - start_time) )
    print('-' * 40)


def trip_duration_state(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is ( {} ).'.format(total_travel_time))
    mean_travel_time = int(df['Trip Duration'].mean())
    print('The mean of travel time is ( {} ).'.format(mean_travel_time))
    print ( "\nThis took %s seconds." % (time.time () - start_time) )
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    user_type = df['User Type'].value_counts()
    print('\nThe counts of user types :\n\n {} '.format(user_type))
    print('-' * 40)
    if city !=  'washington':
        gender_count = df['Gender'].value_counts()
        print('\nThe counts of gender types :\n\n {} '.format(gender_count))
        print('-' * 40)
        earliest_year = int(df['Birth Year'].min())
        print('\nThe earliest year of birth is ( {} ).\n'.format(earliest_year))
        most_recent_year = int(df['Birth Year'].max())
        print('\nThe most recent year of birth is ( {} ).\n'.format(most_recent_year))
        most_common_year = int(df['Birth Year'].mode())
        print('\nThe most common year of birth is ( {} ).\n'.format(most_common_year))
        print('-' * 40)
    else:
        pass



def more_raw_data(df) :
    '''
    This function take the data frame and take user input to display 5 rows of
    raw data
    :param df:take data frame that already chosen from  get_filters() function.
    :return:return 5 rows from the data frame
    '''
    count_x = itertools.count(start=0, step=5)
    count_y = itertools.count(start=5, step=5)
    while True:
        more_raws_data = input('\nDo you want to view 5 rows of raw data? Enter yes or No.\n').lower()
        if more_raws_data == 'yes' or more_raws_data == 'y':
            print(df.iloc[next(count_x):next(count_y)])
            print('-' * 40)
        else:
            print('\nThanks for using US bikeshare Data !\n')
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        ask_more_1 = input('\nDo you want to see more Data? Enter Yes or No ?\n').lower()
        if ask_more_1 == 'yes' or ask_more_1 == 'y':
            station_stats(df)
            ask_more_2 = input('\nDo you want to see more Data? Enter Yes or No?\n').lower()
            if ask_more_2 == 'yes' or ask_more_2 == 'y':
                trip_duration_state(df)
                ask_more_3 = input('\nDo you want to see more Data? Enter Yes or No?\n').lower()
                if ask_more_3 == 'yes' or ask_more_3 == 'y':
                    user_stats(df, city)
                    more_raw_data(df)
                    restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
                    if restart != 'yes' or restart != 'y':
                        print('\nThanks for using US bikeshare Data !\n')
                        break
        else:
            print('\nThanks for using US bikeshare Data !\n')
            break


if __name__ == "__main__":
    main()
