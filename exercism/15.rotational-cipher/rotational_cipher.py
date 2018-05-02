alphabets = "abcdefghijklmnopqrstuvwxyz"


def rotate(text, key):
	key = alphabets[key:] + alphabets[:key]
	ciphered_text = ''
	for char in text:
		if not char.isalpha():
			ciphered_text += char
			continue
		if char.isupper():
			idx = alphabets.index(char.lower())
			ciphered_text += key[idx].upper()
		else:
			idx = alphabets.index(char)
			ciphered_text += key[idx]
	return ciphered_text
