from datetime import date  # Classes to work with day and time
import calendar  # Has useful functions related to dates

date = date.today()  # Fetches current date in full, as in datetime.date(2022, 7, 8)
# Uses indexing to fetch abbreviated form of day
day_today = calendar.day_abbr[date.weekday()]
# calendar.day_abbr is a localized day containing abbreviations from 'Mon' to 'Sun.'
# date_today.weekday() returns an integer that corresponds to the current date.
# For example, if today is Friday, date_today.weekday() will return 4, and Monday will return 0.
# List indexes start from 0, so it makes sense that the first day of the week (Monday) is 0.

if day_today == 'Sun':
    fare = 80
elif day_today == 'Sat':
    fare = 60
else:
    fare = 100


# strftime is a method that return the date in a specified format
print(f'Date: {date.strftime("%Y-%m-%d")}')
print(f'Day: {day_today}')
print(f'Fare: {fare}')
