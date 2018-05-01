import re

pattern = "([a-z0-9][a-z0-9']*[a-z0-9]|[a-z0-9]+)"


def word_count(phrase):
	words = re.findall(pattern, phrase.lower())
	count = {}
	for word in words:
		if not count.__contains__(word):
			count[word] = 1
		else:
			count[word] += 1
	return count


# word_count("rah rah ah ah ah\troma roma ma\tga ga oh la la\t want your bad romance")
