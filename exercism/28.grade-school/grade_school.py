import bisect


class School(object):
	def __init__(self, name):
		self.roster = {}

	def _check_grade_exists(self, grade):
		if not self.roster.__contains__(grade):
			self.roster[grade] = []

	def add(self, name, grade):
		self._check_grade_exists(grade)
		bisect.insort_left(self.roster[grade], name)

	def grade(self, n):
		self._check_grade_exists(n)
		return self.roster[n]

	def sort(self):
		return [(grade, tuple(self.roster[grade])) for grade in sorted(self.roster.keys())]
