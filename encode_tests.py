# encode_tests.py -- tests for the encoding function.

from bencode import encode

# test we can encode a list.
def test_encode_list():
	assert encode([]) == "le"