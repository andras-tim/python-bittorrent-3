# bencode.py -- module for dealing with bencoded data.

import re

# regular expression to match a bencoded string.
BENCODED_STRING_RE = re.compile("[0-9]*:[a-zA-Z]*")

# regular expression to match a bencoded integer.
BENCODED_INTEGER_RE = re.compile("i-*[0-9]+e")

# regular expression to match a bencoded list.
BENCODED_LIST_RE = re.compile("l[:0-9a-zA-Z]*e")

# function to decode bencoded strings.
def decode(data):
	# check to see if the data is a string
	if BENCODED_STRING_RE.match(data):
		return data.partition(":")[2]

	# check to see if the data is an integer.
	elif BENCODED_INTEGER_RE.match(data):
		# remove the start and end delimeters, and return an integer.
		return int(data[1:-1])

	# check to see if the data is a list.
	elif BENCODED_LIST_RE.match(data):
		# if it's an empty list,
		if data == "le":
			# return an empty list.
			return []
		else:
			# recursively decode the data,
			# after removing the list delimeters,
			# and add the returning data to the list.
			return [decode(data[1:-1])]

# function to split a bencoded string into its components.
def split(data):
	# if data is only one number, just return it.
	if len(BENCODED_INTEGER_RE.findall(data)) == 1:
		return [data]

	# if data is just a string, return it.
	elif len(BENCODED_STRING_RE.findall(data)) == 1:
		return [data]

	# the data is some compound, so we'll have to work out the first part.
	else:
		# if the data is an integer,
		if data[0] == "i":
			# split it up, then recursively return.
			partitioned_data = data.partition("e")
			first_piece = partitioned_data[0] + partitioned_data[1]

			response = []
			response.append(first_piece)
			response.extend(split(partitioned_data[2]))

			return response

		# if the data is a string,
		if BENCODED_STRING_RE.match(data):
			# partition the data, then recursively return.
			p_d = data.partition(":")
			first_piece = p_d[0] + p_d[1] + p_d[2][:int(p_d[0])]

			response = []
			response.append(first_piece)
			response.extend(split(data[len(first_piece):]))

			return response
