def is_palindrome(number):
	s = str(number)
	return s == s[::-1]


def factors(number, min_factor, max_factor):
	facts = set()
	for i in range(min_factor, max_factor + 1):
		if (number % i) == 0:
			j = number // i
			if min_factor <= j <= max_factor:
				facts.add((i, j))
	return facts


# A generator that generates sequential multiplications of numbers without extra time complexity ;-)
def gen_numbers(min_factor, max_factor):
	points = [(min_factor, min_factor)]
	for point in points:
		if point[1] <= max_factor:
			yield point
		else:
			continue
		if point[0] == min_factor:
			points += [(point[0], point[1] + 1)]
		if point[0] != point[1]:
			points += [(point[0] + 1, point[1])]

	raise ValueError("Better luck next time")


def smallest_palindrome(max_factor, min_factor):
	if min_factor > max_factor:
		raise ValueError("Negs not allowed")
	numbers = gen_numbers(min_factor, max_factor)
	for num in numbers:
		number = num[0] * num[1]
		if is_palindrome(number):
			return number, factors(number, min_factor, max_factor)


def rev_gen_numbers(min_factor, max_factor):
	points = [(max_factor, max_factor)]
	for point in points:
		if point[0] >= min_factor:
			yield point
		else:
			continue
		if point[1] == max_factor:
			points += [(point[0] - 1, point[1])]
		if point[0] != point[1]:
			points += [(point[0], point[1] - 1)]
	raise ValueError("Better luck next time")


def largest_palindrome(max_factor, min_factor):
	if min_factor > max_factor:
		raise ValueError("Negs not allowed")
	numbers = rev_gen_numbers(min_factor, max_factor)
	for num in numbers:
		number = num[0] * num[1]
		if is_palindrome(number):
			return number, factors(number, min_factor, max_factor)
