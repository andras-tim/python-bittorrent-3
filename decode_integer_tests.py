# decode_integer_tests.py -- tests for decoding bencoded integers.

from bencode import decode

# test that we can decode an integer
def test_decode_int():
	assert decode("i3e") == 3

# test we can decode zero.
def test_decode_zero():
	assert decode("i0e") == 0

# test that we can decode negative zero.
# this is not to the specification, but better in case of bad data.
def test_decode_negative_zero():
	assert decode("i-0e") == 0

# test that we can decode negative numbers.
def test_decode_negative():
	assert decode("i-3e") == -3

# test we can decode numbers of more than one digit.
def test_decode_multiple_digits():
	assert decode("i100e") == 100

# test decode massive numbwe.
def test_decode_massive():
	assert decode("i10000000000000000000e") == 10000000000000000000

# test can successfully decode a zero padded number.
# this is technically not correct, but it's better to try to succeed.
def test_error_on_padded_zero():
	assert decode("i04e") == 4