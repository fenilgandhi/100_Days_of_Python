def sum_of_factors(number):
    factors = set()
    for i in range(2, int(number ** 0.5) + 1):
        if (number % i) == 0:
            factors.add(i)
            factors.add(number // i)
    return sum(factors) + 1


def classify(number):
    # Handling Special Case
    if number < 1:
        raise ValueError("Only positive integers allowed")
    elif number == 1:
        return "deficient"  # Neither Prime nor composite

    # Process normal input
    sum_of_digits = sum_of_factors(number)
    if sum_of_digits == number:
        return "perfect"
    elif sum_of_digits < number:
        return "deficient"
    else:
        return "abundant"
