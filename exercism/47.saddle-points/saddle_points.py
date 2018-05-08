from sys import maxsize


def saddle_points(matrix):
	if not matrix:
		return set()
	# Preprocess max of row and min of col
	size_of_matrix = len(matrix)
	max_of_rows = [0] * size_of_matrix
	min_of_cols = [maxsize] * size_of_matrix
	for j in range(size_of_matrix):
		for i in range(size_of_matrix):
			try:
				element = matrix[j][i]
			except IndexError:
				raise ValueError("Irregular Matrix")
			if max_of_rows[j] < element:
				max_of_rows[j] = element
			if min_of_cols[i] > element:
				min_of_cols[i] = element

	# Finding the saddle points from the preprocessed matrix
	saddle_points = set()
	for j in range(size_of_matrix):
		for i in range(size_of_matrix):
			element = matrix[j][i]
			if (element == max_of_rows[j]) and (element == min_of_cols[i]):
				saddle_points.add((j, i,))
	return saddle_points
