def sieve(limit):
	numbers = list(range(2, limit + 1))
	primes = []
	for number in numbers:
		if number == 0:
			continue
		primes.append(number)
		for i in range(number - 2, limit - 1, number):
			numbers[i] = 0
	return primes
