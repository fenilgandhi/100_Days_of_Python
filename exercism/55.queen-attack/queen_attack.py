class Queen(object):
	def __init__(self, row, column):
		if (0 <= row < 8) and (0 <= column < 8):
			self.row = row
			self.column = column
		else:
			raise ValueError("Virtual indexes not allowed")

	def can_attack(self, another_queen):
		a = self.row == another_queen.row
		b = self.column == another_queen.column
		c = abs(self.column - another_queen.column) == abs(self.row - another_queen.row)
		if a and b:
			raise ValueError("Suicide not allowed")
		if a or b or c:
			return True
		return False
