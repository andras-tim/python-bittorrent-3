# split_bencode_string_tests.py -- tests for splitting a bencoded string up.

from bencode import split

# test we can split a one integer bencoded string to itself.
def test_split_one_integer_string():
	assert split("i0e") == "i0e"

# test we can split a one string bencoded string to itself.
def test_split_one_string():
	assert split("4:spam") == "4:spam"

# test we can split two integers into a list of integer components.
def test_split_two_integers():
	assert split("i0ei0e") == ["i0e", "i0e"]