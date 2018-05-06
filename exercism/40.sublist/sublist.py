check_lists = 0
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def check_lists(first_list, second_list):
	first_list = "#".join(map(str, first_list))
	second_list = "#".join(map(str, second_list))
	
	ainb = (first_list in second_list)
	bina = (second_list in first_list)

	if ainb and bina :
		return EQUAL
	elif ainb:
		return SUBLIST
	elif bina:
		return SUPERLIST
	else:
		return UNEQUAL
