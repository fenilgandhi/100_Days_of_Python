class Flat():
	def __init__(self):
		self.result = []

	def run(self, collection):
		self.loop(collection)
		return self.result

	def add(self, item):
		self.result += [item]

	def loop(self, collection):
		for item in collection:
			if item is None:
				continue
			if getattr(item, '__iter__', False):
				# Strings, even single chars , have __iter__ method
				if type(item) == str:
					self.result += [item]
				else:
					self.loop(item)
			else:
				self.result += [item]


def flatten(collection):
	return Flat().run(collection)
