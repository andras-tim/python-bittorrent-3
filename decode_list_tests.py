# decode_list_tests.py -- tests for decoding lists.

from bencode import decode

# test we can decode an empty list.
def test_decode_empty_list():
	assert decode("le") == []