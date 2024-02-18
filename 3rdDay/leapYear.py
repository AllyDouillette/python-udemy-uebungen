def is_leap_year(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				print(f"Leap year")
			else:
				print(f"Not leap year")
		else:
				print(f"Leap year")
	else:
		print(f"Not leap year")

is_leap_year(1900)
is_leap_year(1996)
is_leap_year(2000)
is_leap_year(2002)
is_leap_year(2004)
