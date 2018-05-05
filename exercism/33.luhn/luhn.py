class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", '')

    def is_valid(self):
        # Non-digit characters are not allowed
        if not self.card_num.isdigit():
            return False

        # Strings of length 1 or less are invalid
        if len(self.card_num) < 2:
            return False

        # Divide the digits in two and double the one containing second last digit
        def reduce(digit):
            return (digit * 2) if digit < 5 else (digit * 2) - 9

        digits = list(map(int, self.card_num))
        even_digits, odd_digits = digits[::2], digits[1::2]
        if (len(digits) % 2) != 0:
            sum_of_digits = sum([reduce(digit) for digit in odd_digits])
            sum_of_digits += sum(even_digits)
        else:
            sum_of_digits = sum([reduce(digit) for digit in even_digits])
            sum_of_digits += sum(odd_digits)

        # Only evenly divisible by 10 --> valid
        if (sum_of_digits % 10) == 0:
            return True
        return False
