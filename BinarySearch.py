class BinarySearch(list):
	def __init__(self, a, b):
		self.a = a
		self.b = b

		for num in range(self.a):
			list.append(self, self.b)
			self.b += b
			num += 1

		self.length = num


	def search(self, num):
		frst = 0
		lst = self.length - 1
		fnd = False
		count = 0
		in_the_list = False
		try:
			index = self.index(num)
			in_the_list = True
		except ValueError:
			index = -1
			in_the_list = False

		while frst <= lst and not fnd and in_the_list and num != self[lst]:
			mid_point = (frst + lst) // 2
			mid_value = self[mid_point]
			if mid_value == num:
				fnd = True
				count += 1
				index = mid_point
			else:
				if num < mid_value:
					lst = mid_point - 1
					count += 1
				else:
					frst = mid_point + 1
					count += 1
		return {"count": count, "index": index}

print (BinarySearch(20, 2).search(16))