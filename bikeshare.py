import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#----------------------------------------------------------------------------------------------------------------

    while True:
        city=input("choose city from the following chicago, new york city, washington \n" )
        city= city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("please enter city from the following chicago, new york city, washington")
        else:
            break
        
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    Months=['January','February','March','April','May','June']
    
    while True:    
        month=input("choose month you need to filter with from January to June or all\n")
        month= month.lower()
        if month not in ('january','february','march','april','may','june','all'):
            print("please enter month from the following January,February,March,April,May,June,all")  
        else:
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:    
        day=input("choose a week day that you need to filter saturday,sunday,monday,tuesday,wednesday,thrusday,friday,all \n" )
        day= day.lower()
        if day not in ('saturday','sunday','monday','tuesday','wednesday','thrusday','friday','all'):
            print("please enter a vaild day in a week")
        else:
            break
    
    print('-'*40)
    
    return city, month, day

#-----------------------------------------------------------------------------------------------------------------

def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    

    return df

#--------------------------------------------------------------------

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\n the most common month was: {} ".format(df['month'].mode()[0]))
    
    # TO DO: display the most common day of week
    
    print("\n the most common day of a week was: {} ".format(df['day_of_week'].mode()[0]))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("\n the most common start hour was: ",(df['hour'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#--------------------------------------------------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\n the most common start station used was:{}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("\n the most common end station used was:{}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print("\n the most frequent Start and End station combination was:{}".format((df['Start Station']+''+df ['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#--------------------------------------------------------------------------

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("the total travel time is:{}".format(int(df['Trip Duration'].sum())))

    # TO DO: display mean travel time
    print("the mean travel time is:{}".format(int(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#--------------------------------------------------------------------------
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("the count of users types is: ", df.groupby(['User Type'])['User Type'].count())

    # TO DO: Display counts of gender
    if 'Gender' in df:
    # Only access Gender column in this case
        print("the count of gender is: ", df.groupby(['Gender'])['Gender'].count())
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
  

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("the most recent is: ", df['Birth Year'].max())
        print("the earlist is: ",df['Birth Year'].min())
        print("the most common year of birth is: ", df['Birth Year'].mode()[0])
    else:
        print(' all Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

       
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        start_loc = 0
        while (view_data.lower()=='yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            if view_display.lower() == 'yes':
                continue
            else:   
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()