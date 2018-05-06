def verify(isbn: str) -> bool:
	isbn = isbn.replace('-', '')
	# Reject invalid length isbn, return False
	if len(isbn) != 10:
		return False

	# If check digit is not correct, return False
	sum = 0
	if isbn[9].isdigit():
		sum += int(isbn[9])
	elif isbn[9] == "X":
		sum += 10
	else:
		return False

	for index in range(9):
		if not isbn[index].isdigit():
			return False
		sum += int(isbn[index]) * (10 - index)

	sum = sum % 11
	if sum == 0:
		return True
	return False
