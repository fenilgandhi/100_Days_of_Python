def is_armstrong(number):
	cube = number
	factor = len(str(number))
	while number > 0:
		number, last_digit = number // 10, number % 10
		cube -= last_digit ** factor
	return (cube == 0)
