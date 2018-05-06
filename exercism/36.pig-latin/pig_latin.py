import re


def convert(word):
	consonants = "bcdfghjklmnpqrstvwxz"

	# Rule 1
	if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
		return word + 'ay'

	pattern = f"(^[{consonants}]+|y)([a-z]+)$"
	consonants = re.findall(pattern, word)[0]
	if consonants:
		if consonants[1][0] == 'y':
			return consonants[1] + consonants[0] + 'ay'
		if (consonants[0][-1] == 'q') and (consonants[1][0] == 'u'):
			return consonants[1][1:] + consonants[0] + 'uay'
		return consonants[1] + consonants[0] + 'ay'

	return word


def translate(text):
	return ' '.join([convert(word) for word in text.split()])
