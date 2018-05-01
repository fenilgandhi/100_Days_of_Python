def decode(string):
	decoded_string = ""
	ls = len(string)
	if ls < 1:
		return ''
	i = 0
	while i < ls:
		count = ''
		char = string[i]
		while char.isdigit():
			count += char
			i += 1
			char = string[i]
		if count != '':
			decoded_string += char * int(count)
		else:
			decoded_string += char
		i += 1
	return decoded_string


def encode(string):
	if len(string) < 1:
		return ''
	current_char = string[0]
	count = 0
	encoded_string = ""
	for char in string:
		if char == current_char:
			count += 1
		else:
			if count > 1:
				encoded_string += f"{count}{current_char}"
			else:
				encoded_string += f"{current_char}"
			count = 1
			current_char = char
	if count > 1:
		encoded_string += f"{count}{current_char}"
	else:
		encoded_string += f"{current_char}"
	return encoded_string
