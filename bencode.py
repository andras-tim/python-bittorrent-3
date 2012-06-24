# bencode.py -- module for dealing with bencoded data.

def decode(data):
	# If the data is an empty bencoded list,
	if data == "le":
		# return an empty python list.
		return []

	# If the data is a bencoded list,
	elif data[0] == "l" and data[-1] == "e":
		return [decode(data[1:-1])]

	# If the data is a bencoded integer,
	elif data[0] == "i":
		# find the end of the integer,
		length = data.find("e")

		# then cut the string, and return a python integer.
		return int(data[1:length])

	# If the data is a bencoded string,
	elif data[0] in list(map(str, list(range(10)))):
		# work out how long the string is,
		partitioned = data.partition(":")
		offset = len(partitioned[0]) + 1
		string_length = int(partitioned[0])

		# then slice it out, and return a python string.
		return data[offset:offset + string_length]
