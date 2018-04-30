def is_pangram(sentence):
	"Use a flags list for each character and check if flags are False at the end"
	flags = [True] * 26
	for c in sentence.lower():
		if 96 < ord(c) < 123:
			flags[ord(c) - 97] = False
	if any(flags):
		return False
	return True
