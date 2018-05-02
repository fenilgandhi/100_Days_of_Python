def detect_anagrams(word, candidates):
	list_of_word = sorted(word.lower())
	anagrams = []
	for candidate in candidates:
		if candidate.lower() == word.lower():
			continue
		if sorted(candidate.lower()) == list_of_word:
			anagrams += [candidate]
	return anagrams
