def transform(legacy_data):
	new_data = {}
	for score, characters in legacy_data.items():
		for char in characters:
			new_data[char.lower()] = score
	return new_data
