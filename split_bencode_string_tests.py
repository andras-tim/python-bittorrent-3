# split_bencode_string_tests.py -- tests for splitting a bencoded string up.

from bencode import split

# test we can split a one integer bencoded string to itself.
def split_one_integer_string():
	assert split("i0e") == "i0e"