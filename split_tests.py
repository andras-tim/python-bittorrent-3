# split_tests.py -- tests for split

from bencode import split

# test we can split an empty string.
def test_empty_string():
	assert split("" == [])