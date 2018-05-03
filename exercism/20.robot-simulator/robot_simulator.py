# Globals for the bearings
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot(object):
	def __init__(self, bearing=NORTH, x=0, y=0):
		self.coordinates = (x, y)
		self.bearing = bearing

	def turn_right(self):
		self.bearing = {
			EAST: SOUTH,
			SOUTH: WEST,
			WEST: NORTH,
			NORTH: EAST
		}.get(self.bearing)

	def turn_left(self):
		self.bearing = {
			SOUTH: EAST,
			EAST: NORTH,
			NORTH: WEST,
			WEST: SOUTH
		}.get(self.bearing)

	def advance(self):
		self.coordinates = (self.coordinates[0] + self.bearing[0], self.coordinates[1] + self.bearing[1])

	def simulate(self, commands):
		for chr in commands:
			if chr == 'R':
				self.turn_right()
			elif chr == 'L':
				self.turn_left()
			elif chr == 'A':
				self.advance()
