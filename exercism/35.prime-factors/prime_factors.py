def next_prime():
	yield 2
	number = 3
	while True:
		for i in range(3, int(number ** 0.5), 2):
			if (number % i) == 0:
				break
		else:
			yield number
		number += 2


def prime_factors(natural_number):
	if natural_number < 2:
		return []
	if natural_number == 2:
		return [2]

	factors = []
	while natural_number > 1:
		for prime in next_prime():
			if (natural_number % prime) == 0:
				factors.append(prime)
				natural_number = natural_number / prime
				break
	return factors
