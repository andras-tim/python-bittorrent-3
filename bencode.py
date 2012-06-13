# bencode.py -- module for dealing with bencoded data.

import re

# regular expression to match a bencoded string.
BENCODED_STRING_RE = re.compile("[0-9]*:[a-zA-Z]*")

# regular expression to match a bencoded integer.
BENCODED_INTEGER_RE = re.compile("i-*[0-9]+e")

# function to decode bencoded strings.
def decode(data):
	# check to see if the data is a string
	if BENCODED_STRING_RE.match(data):
		return data.partition(":")[2]

	# check to see if the data is an integer.
	elif BENCODED_INTEGER_RE.match(data):
		# remove the start and end delimeters, and return an integer.
		return int(data[1:-1])