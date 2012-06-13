# decode_list_tests.py -- tests for decoding lists.

from bencode import decode

def test_decode_empty_list():
	assert decode("le") == []