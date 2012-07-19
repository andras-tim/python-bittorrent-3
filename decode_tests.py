# decode_tests.py -- generic suite of tests for bencoded decoding

from bencode_compiler import decode

decode_test_data = [
	["i3e", 3],
	["i0e", 0],
	["i-0e", 0],
	["i-3e", -3],
	["i100e", 100],
	["i10000000000000000000e", 10000000000000000000],
	["i04e", 4]
]

# spin through the decode test data, and generate tests.
def test_decode():
	for i in decode_test_data:
		yield lambda x, y: decode(x) == y, i[0], i[1]