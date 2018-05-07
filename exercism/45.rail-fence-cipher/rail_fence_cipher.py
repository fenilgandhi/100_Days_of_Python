def iter_index(rails):
	while True:
		for i in range(rails):
			yield i
		for i in range(rails-2,0, -1):
			yield i

def encode(message, rails, index=False):
	indexes = iter_index(rails)
	if index:
		cipher = [[] for _ in range(rails)]
	else:
		cipher = [""] * rails
	for char in message:
		idx = next(indexes)
		if index:
			cipher[idx] += [char]
		else:
			cipher[idx] += char
	if index:
		result = []
		for ls in cipher:
			result += ls
	else:
		result = "".join(cipher)
	return result

def decode(encoded_message, rails):
	lc = len(encoded_message)
	
	indexes = list(range(lc))
	ciphered_indexes = encode(indexes, rails, True)
	
	message = [''] * lc
	for i in range(lc):
		message[ciphered_indexes[i]] = encoded_message[i]
	return "".join(message)
	