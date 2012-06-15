# split_bencode_string_tests.py -- tests for splitting a bencoded string up.

from bencode import split

# test we can split a one integer bencoded string to itself.
def test_split_one_integer_string():
	assert split("i0e") == ["i0e"]

# test we can split a one string bencoded string to itself.
def test_split_one_string():
	assert split("4:spam") == ["4:spam"]

# test we can split two integers into a list of integer components.
def test_split_two_integers():
	assert split("i0ei0e") == ["i0e", "i0e"]

# test we can split two strings into a list of string components.
def test_split_two_strings():
	assert split("4:spam4:spam") == ["4:spam", "4:spam"]

# test we can split three integers into a list of integer components.
def test_split_three_integers():
	assert split("i0ei0ei0e") == ["i0e", "i0e", "i0e"]

# test we can split three strings into a list of string components.
def test_split_three_strings():
	assert split("4:spam4:spam4:spam") == ["4:spam", "4:spam", "4:spam"]

# test we can split an integer and a string.
def test_split_integer_string():
	assert split("i0e1:a") == ["i0e", "1:a"]