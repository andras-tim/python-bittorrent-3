# decode_tests.py -- tests for decoding bencoded data.
# written by Joseph Salisbury -- 11/06/12

from bencode import decode

def test_decode_int():
	assert decode("i3e") == 3

# test we can decode zero.
def test_decode_zero():
	assert decode("i0e") == 0

# test that we can decode negative numbers.
def test_decode_negative():
	assert decode("i-3e") == -3