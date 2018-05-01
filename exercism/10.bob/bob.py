def hey(phrase):
	phrase = phrase.strip()
	if phrase.isspace() or phrase == "":
		return "Fine. Be that way!"
	elif phrase.endswith('?') and phrase.isupper():
		return "Calm down, I know what I'm doing!"
	elif phrase.endswith('?'):
		return "Sure."
	elif phrase.isupper():
		return "Whoa, chill out!"
	else:
		return "Whatever."


