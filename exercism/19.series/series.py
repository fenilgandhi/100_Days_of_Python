def slices(series, length):
	series = list(map(int, series))
	ls = len(series)
	if (ls < length) or (length == 0):
		raise ValueError("Incorrect value of length")
	return [series[i:i + length] for i in range(ls - length + 1)]
