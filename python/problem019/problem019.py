# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""
import pandas as pd


def the_easy_way() -> int:
    dates = pd.date_range("1901-01-01", "2000-12-31", freq="D")
    return ((dates.day_of_week == 6) & (dates.day == 1)).sum()


DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def the_hard_way() -> int:
    sundays = 0

    day_of_week = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            is_leap_year = (year % 4 == 0) & ((year % 100 != 0) | (year % 400 == 0))
            days = DAYS[month]
            if month == 2 and is_leap_year:
                days += 1

            for day in range(days):
                if day == 1 and day_of_week == 6 and year >= 1901:
                    sundays += 1
                day_of_week = 0 if day_of_week == 6 else day_of_week + 1

    return sundays


if __name__ == "__main__":
    easy_result = the_easy_way()
    print(easy_result)
    hard_result = the_hard_way()
    print(hard_result)
