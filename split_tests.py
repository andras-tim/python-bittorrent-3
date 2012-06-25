# split_tests.py -- tests for split

from bencode import split

# test we can split an empty string.
def test_empty_string():
	assert split("") == []

# test we can split one integer.
def test_split_one_integer():
	assert split("i0e") == ["i0e"]

# test we can split two strings.
def test_split_two_strings():
	assert split("4:spam4:spam") == ["4:spam", "4:spam"]

# test we can split a list. ish.
def test_split_list():
	assert split("llee") == ["le"]

# test we can split multiple nested lists.
def test_split_multiple_nested_lists():
	assert split("llllleeeee") == ["lllleeee"]