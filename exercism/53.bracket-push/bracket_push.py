def is_paired(input_string):
	stack = []
	for char in input_string:
		if char in "{([":
			stack += [char]
		elif(char == "}"):
			if (stack[-1:] == ["{"]):
				stack.pop()
			else:
				return False
		elif(char == ")"):
			if (stack[-1:] == ["("]):
				stack.pop()
			else:
				return False
		elif(char == "]"):
			if (stack[-1:] == ["["]):
				stack.pop()
			else:
				return False
	if len(stack) < 1:
		return True
	return False
