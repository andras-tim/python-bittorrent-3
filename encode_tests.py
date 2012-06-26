# encode_tests.py -- tests for the encoding function.

from bencode import encode

# test we can encode a list.
def test_encode_list():
	assert encode([]) == "le"

# test we can encode a list with a single number in it.
def test_encode_list_with_number():
	assert encode([0]) == "li0ee"