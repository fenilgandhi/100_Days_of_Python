class Matrix(object):
    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        
        # Parsing and adding individual value to matrix
        self.matrix = []
        for row in rows:
        	this_row = [int(value) for value in row.split()]
        	self.matrix.append(this_row)


    def row(self, index):
        if len(self.matrix) > index:
        	return self.matrix[index]
        else:
        	raise IndexError

    def column(self, index):
        if self.matrix[0] and len(self.matrix[0]) > index:
        	return [row[index] for row in self.matrix]
        else:
        	raise IndexError
