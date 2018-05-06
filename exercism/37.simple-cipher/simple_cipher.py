alphabets = 'abcdefghijklmnopqrstuvwxyz'
key = alphabets[3:] + alphabets[:3]


class Cipher(object):
	def __init__(self, key=None):
		if key:
			if not (key.isalpha() and key.islower()):
				raise ValueError("Wrong Key")
			self.key = key
		else:
			self.key = 'a' * 101

	def iter_key(self):
		while True:
			for c in self.key:
				yield c

	def encode(self, text):
		cipher = ''
		for char, kchar in zip(text, self.iter_key()):
			idx = (alphabets.index(char) + alphabets.index(kchar)) % 26
			cipher += alphabets[idx]
		return cipher

	def decode(self, cipher):
		text = ''
		for char, kchar in zip(cipher, self.iter_key()):
			idx = (alphabets.index(char) - alphabets.index(kchar)) % 26
			text += alphabets[idx]
		return text


class Caesar(object):
	def __init__(self):
		pass

	def encode(self, text):
		return "".join([key[alphabets.index(char.lower())] for char in text if char.isalpha()])

	def decode(self, text):
		return "".join([alphabets[key.index(char.lower())] for char in text if char.isalpha()])
