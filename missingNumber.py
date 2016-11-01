def find_missing(list1, list2):
	if list1 == [] and list2 == []:
		return 0

	if len(list1) == len(list2):
		for num in list1:
			if num in list2:
				return 0
	else:
		if len(list1) < len(list2):
			for num in list2:
				if num not in list1:
					return num
		else:
			for num in list1:
				if num not in list2:
					return num