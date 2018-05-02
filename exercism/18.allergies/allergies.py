allergies = {
	1: 'eggs',
	2: 'peanuts',
	4: 'shellfish',
	8: 'strawberries',
	16: 'tomatoes',
	32: 'chocolate',
	64: 'pollen',
	128: 'cats',
}


class Allergies(object):

	def __init__(self, score):
		if score > 255:
			score = score % 256
		self.score = score
		self.allergies = []
		self.set_lst()

	def set_lst(self):
		score = self.score
		counter = 256
		while counter > 0:
			if (score // counter) > 0:
				score = score % counter
				self.allergies += [allergies[counter]]
			counter = counter // 2

	def is_allergic_to(self, item):
		return bool(item in self.allergies)

	@property
	def lst(self):
		return self.allergies
