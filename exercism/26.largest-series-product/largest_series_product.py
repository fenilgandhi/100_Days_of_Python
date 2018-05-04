def largest_product(series, size):
	if (len(series) < size) or (size < 0):
		raise ValueError("Wrong Input")
	series = list(map(int, series))
	maxim = 0
	for idx in range(len(series) - size + 1):
		seq = 1
		for val in series[idx: idx + size]:
			seq *= val
		if seq > maxim:
			maxim = seq
	return maxim
