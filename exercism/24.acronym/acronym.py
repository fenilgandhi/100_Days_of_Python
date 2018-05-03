def abbreviate(words):
	abv = ''
	words = words.replace('-', ' ')
	for word in words.split(' '):
		abv += word[0].upper()
	return abv
