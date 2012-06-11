# bencode.py -- module for dealing with bencoded data.
# written by Joseph Salisbury -- 11/06/12

import re

BENCODED_INTEGER_RE = re.compile("i-*[0-9]+e")

def decode(data):
	if BENCODED_INTEGER_RE.match(data):
		return int(data[1:-1])