# bencode.py -- module for dealing with bencoded data.
# written by Joseph Salisbury -- 11/06/12

import re

# Exception for decoding errors.
class DecodeError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

# regular expression to match a bencoded integer.
BENCODED_INTEGER_RE = re.compile("i-*[0-9]+e")

# function to decode bencoded strings.
def decode(data):
	# check to see if the data is an integer.
	if BENCODED_INTEGER_RE.match(data):
		# remove the start and end delimeters.
		number_string = data[1:-1]

		# check no padding zeros.
		if len(number_string) > 1 and number_string[0] == "0":
			raise DecodeError("Padding zeros is not allowed.")

		# return an integer.
		return int(number_string)