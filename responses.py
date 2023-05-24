import csv
import os
import sys
import calendar
import pandas as pd
from datetime import date, timedelta

dir_path = os.getcwd()
date_string_format = '%B %-d %Y'

# generate all dates for next month's Sundays
current_date = date.today()

# Calculate the first day of the next month
next_month = current_date.replace(day=1) + timedelta(days=32)
next_month_first_day = next_month.replace(day=1)

next_month_calendar = calendar.monthcalendar(next_month_first_day.year, next_month_first_day.month)
sundays = [date(next_month_first_day.year, next_month_first_day.month, day).strftime(date_string_format) for week in next_month_calendar for day in week if day != 0 and week[calendar.SUNDAY] == day]

# filters NaN dates and adds dates to nested list available_dates
def process_dates(date_list: list):
    new_date_list = []
    i = 0
    for date in date_list:
        if (pd.isna(date) != True):
            available_dates = []
            string_date_list = date.split(",")
            for i in range(1, len(string_date_list), 2):
                available_dates.append(string_date_list[i].strip(" "))
            new_date_list.append(available_dates)
        else:
            new_date_list.append([''])
    return new_date_list

# groups names of volunteers to the dates they are available to serve
def process_availability(name_list: list, date_list: list):
    dates_dict = {}
    index = 0
    always_avail = []

    # initialize dictionary with this month's Sunday dates
    for date in sundays:
        dates_dict[date] = []
    
    for unavail_dates in date_list:
        if len(unavail_dates) == 0:
            always_avail.append(index)
            continue
        for date in sundays:
            if date not in unavail_dates:
                dates_dict[date].append(name_list[index])
        index += 1

    # add up volunteers with no unavailable dates
    if len(always_avail) > 0:
        for key in dates_dict.keys():
            for avail_name in always_avail:
                dates_dict[key].append(avail_name) 
    return dates_dict

# writes out a CSV file based on the dictionary result
def create_csv(output_dict: dict):
    with open(dir_path + '/responses/june_avail.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Volunteers'])
        for date, volunteers in output_dict.items():
            writer.writerow([date] + volunteers)

if __name__ == "__main__":
    n = len(sys.argv)

    if (n == 1):
        raise Exception("No arguments passed!")

    if (n >= 2):
        df = pd.read_excel(dir_path + "/responses/" + sys.argv[1])
        names = df['Name'].tolist()
        availability = df['Available'].tolist()
        unavail_dates = df['Dates'].tolist()
        for i in range(0, len(availability)):
            if availability[i].lower() == "no":
                names.pop(i)
                unavail_dates.pop(i)
        filtered_dates = process_dates(unavail_dates)
        available_peeps = process_availability(names, filtered_dates)
        create_csv(available_peeps)