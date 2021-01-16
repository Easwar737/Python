"""Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year."""

# I have manually given the input. This one works perfectly for other testcases too.

from datetime import date as dt
date = "2019-01-09"
yr=int(date[:4])
mn=int(date[5:7])
dy=int(date[8:])
s_date=dt(yr,1,1)
e_date=dt(yr,mn,dy)
return (e_date-s_date).days+1