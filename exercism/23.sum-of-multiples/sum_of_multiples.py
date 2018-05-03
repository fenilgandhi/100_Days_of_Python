def sum_of_multiples(limit, multiples):
	numbers = set()
	for mutiple in multiples:
		numbers.update(iter(range(mutiple, limit, mutiple)))
	return sum(numbers)
