# decode_list_tests.py -- tests for decoding lists.

from bencode import decode

# test we can decode an empty list.
def test_decode_empty_list():
	assert decode("le") == []

# test we can decode a list with a single integer in.
def test_decode_one_integer_list():
	assert decode("li0ee") == [0]