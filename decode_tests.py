# decode_tests.py -- tests for decoding bencoded data.
# written by Joseph Salisbury -- 11/06/12

from bencode import decode, DecodeError

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

# test that we can decode an integer
def test_decode_int():
	assert decode("i3e") == 3

# test we can decode zero.
def test_decode_zero():
	assert decode("i0e") == 0

# test that we can decode negative numbers.
def test_decode_negative():
	assert decode("i-3e") == -3

# test we can decode numbers of more than one digit.
def test_decode_multiple_digits():
	assert decode("i100e") == 100

# test decode massive numbwe.
def test_decode_massive():
	assert decode("i10000000000000000000e") == 10000000000000000000

# test error on padded zero
def test_error_on_padded_zero():
	error_raised = False

	try:
		decode("i04e")
	except DecodeError:
		error_raised = True

	assert error_raised