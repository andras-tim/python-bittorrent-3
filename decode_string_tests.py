# decode_tests.py -- tests for decoding bencoded data.

from bencode2 import decode

# test that we can decode the empty string
def test_decode_empty_string():
	assert decode("0:") == ""

# test that we can decode a simple string.
def test_decode_simple_string():
	assert decode("4:spam") == "spam"

# test that we can decode a longer string.
def test_decode_long_string():
	LONG_STRING = "antidisestablishmentarianism"

	assert decode("28:" + LONG_STRING) == LONG_STRING

# test that we can decode a string with capital letters.
def test_decode_capital_letters():
	assert decode("13:camelCaseTest") == "camelCaseTest"