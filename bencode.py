# bencode.py -- module for dealing with bencoded data.

def decode(data):
	# If the data is an empty bencoded list,
	if data == "le":
		# return an empty python list.
		return []

	# If the data is a bencoded list,
	elif data.startswith("l") and data.endswith("e"):
		items = split(data[1:-1])

		return list(map(decode, items))

	# If the data is a bencoded integer,
	elif data.startswith("i") and data.endswith("e"):
		# find the end of the integer,
		length = data.find("e")

		# then cut the string, and return a python integer.
		return int(data[1:length])

	# If the data is a bencoded string,
	# (so, it starts with a number)
	elif data[0] in list(map(str, list(range(10)))):
		# work out how long the string is,
		partitioned = data.partition(":")
		offset = len(partitioned[0]) + 1
		string_length = int(partitioned[0])

		# then slice it out, and return a python string.
		return data[offset:offset + string_length]

def split(string):
	# If the string is empty,
	if string == "":
		# return an empty list.
		return []

	# If the data starts with a number,
	elif string.startswith("i"):
		length = string.find("e")

		items = []
		items.append(string[:length + 1])
		items.extend(split(string[length + 1:]))
		return items

	# If the data starts with a bencoded string,
	elif string[0] in list(map(str, list(range(10)))):
		partitioned = string.partition(":")
		offset = len(partitioned[0]) + 1
		string_length = int(partitioned[0])

		items = []
		items.append(string[:offset + string_length])
		items.extend(split(string[offset + string_length:]))
		return items

	# If the data starts with a bencoded list,
	elif string.startswith("l"):
		# find the end of this list:
		list_count = 1
		index = 1
		while list_count != 0:
			if string[index] == "l":
				list_count += 1
			elif string[index] == "e":
				list_count -= 1

			index += 1

		return [string[1:index - 1]]