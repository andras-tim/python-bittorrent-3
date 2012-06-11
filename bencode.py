# bencode.py -- module for dealing with bencoded data.
# written by Joseph Salisbury -- 11/06/12

import re

class DecodeError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

# regular expression to match a bencoded integer.
BENCODED_INTEGER_RE = re.compile("i-*[0-9]+e")

def decode(data):
	if BENCODED_INTEGER_RE.match(data):
		number_string = data[1:-1]

		# check no padding zeros.
		if len(number_string) > 1 and number_string[0] == "0":
			raise DecodeError("Padding zeros is not allowed.")

		return int(number_string)