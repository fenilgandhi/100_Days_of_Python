roman_numerals = {
	1: "I",
	5: "V",
	10: "X",
	50: "L",
	100: "C",
	500: "D",
	1000: "M",
	5000: "",
	10000: ""
}


def gen_numerals(digit, factor):
	one = roman_numerals[factor]
	five = roman_numerals[factor * 5]
	ten = roman_numerals[factor * 10]
	return {
		1: f"{one}",
		2: f"{one}{one}",
		3: f"{one}{one}{one}",
		4: f"{one}{five}",
		5: f"{five}",
		6: f"{five}{one}",
		7: f"{five}{one}{one}",
		8: f"{five}{one}{one}{one}",
		9: f"{one}{ten}",
		10: f"{ten}",
	}.get(digit)


def numeral(number):
	result = ""
	factor = 1000
	while number > 1:
		if (number > factor):
			digit = (number // factor)
			result += gen_numerals(digit, factor)
		number = number % factor
		factor = factor // 10
	if number == 1:
		result += 'I'
	return result
