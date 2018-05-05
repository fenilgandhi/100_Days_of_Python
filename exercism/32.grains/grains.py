chessboard = [1]


def fill_until(integer_number):
	global chessboard
	while len(chessboard) < integer_number:
		chessboard += [chessboard[-1] * 2]


def on_square(integer_number):
	if not (0 < integer_number < 65):
		raise ValueError("A chessboard has 64 squares")
	if len(chessboard) < integer_number:
		fill_until(integer_number)
	return chessboard[integer_number - 1]


def total_after(integer_number):
	if not (0 < integer_number < 65):
		raise ValueError("A chessboard has 64 squares")
	if len(chessboard) < integer_number:
		fill_until(integer_number)
	return sum(chessboard[:integer_number])
