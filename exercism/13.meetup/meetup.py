import datetime

week_count = [1, 2, 3, 4, 5, 6, 7]
max_days = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}


class MeetupDayException(Exception):
	def __str__(self):
		return "Day not in Month"


def is_leap_year(year):
	if(year % 4 != 0):
		return False
	elif(year % 400 == 0):
		return True
	elif(year % 100 == 0):
		return False
	return True


def meetup_day(year, month, day_of_the_week, which):
	which = {"first": 1, "1st": 1, "second": 2, "2nd": 2, "third": 3, "3rd": 3, "fourth": 4, "4th": 4, "fifth": 5, "5th": 5, "teenth": 10, "last": -1}.get(which)
	day_of_the_week = weekday.get(day_of_the_week)
	start = datetime.date(year=year, month=month, day=1)
	start_day = start.isoweekday() - 1
	calendar = [''] + week_count[start_day:] + week_count * 5
	if month == 2:
		if is_leap_year(year):
			calendar = calendar[:29 + 1]
		else:
			calendar = calendar[:28 + 1]
	else:
		calendar = calendar[:max_days[start.month] + 1]

	try:
		if which == 10:
			day = calendar.index(day_of_the_week, 13)
		elif which == -1:
			day = calendar.index(day_of_the_week, -7)
		else:
			day = calendar.index(day_of_the_week, 1 + (which - 1) * 7)
		return datetime.date(year, month, day)
	except ValueError:
		raise MeetupDayException


# print(meetup_day(2018, 5, 'Wednesday', 'first'))
