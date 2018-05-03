alphabets = 'abcdefghijklmnopqrstuvwxyz'


def encode(plain_text):
	cipher_text = ''
	idx = 0
	for c in plain_text.lower():
		if not c.isalnum():
			continue
		if idx == 5:
			cipher_text += ' '
			idx = 0
		if c.isdigit():
			cipher_text += c
		else:
			cipher_text += alphabets[-1 - alphabets.index(c)]
		idx += 1

	return cipher_text


def decode(ciphered_text):
	decipher_text = ''
	for c in ciphered_text:
		if c == ' ':
			continue
		if c.isdigit():
			decipher_text += c
		else:
			decipher_text += alphabets[-1 - alphabets.index(c)]
	return decipher_text
