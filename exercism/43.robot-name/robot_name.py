index = 0
counter = 0

# Return a name
def gen_name():
	global index
	global counter
	first_char = chr((index // 26) + 65)
	second_char= chr((index % 26) + 65)
	name = f"{first_char}{second_char}{str(counter).zfill(3)}"
	
	# Increment chars if counter is full
	counter += 1
	if counter >= 999:
		counter = 0
		index += 1

	return name

class Robot(object):
	def __init__(self):
		self.name = gen_name()        

	def reset(self):
		self.name = gen_name()