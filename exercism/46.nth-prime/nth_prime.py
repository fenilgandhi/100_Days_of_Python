def next_prime():
	yield 2
	number = 3
	while True:
		for factor in range(3, int(number ** 0.5) + 1, 2):
			if(number % factor) == 0:
				break
		else:
			yield number
		number += 2


def nth_prime(positive_number):
	if positive_number < 1:
		raise ValueError("Not a positive number")
	primes = next_prime()
	[next(primes) for i in range(1, positive_number)]
	return next(primes)
