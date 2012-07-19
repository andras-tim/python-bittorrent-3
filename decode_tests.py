# decode_tests.py -- generic suite of tests for bencoded decoding

from bencode_compiler import decode

decode_test_data = [
	["i3e", 3],
	["i0e", 0],
	["i-0e", 0],
	["i-3e", -3],
	["i100e", 100],
	["i10000000000000000000e", 10000000000000000000],
	["i04e", 4],

	["le", []],
	["li0ee", [0]],
	["l4:spame", ["spam"]],
	["l4:spam4:spame", ["spam", "spam"]],
	["li0ei0ee", [0, 0]],
	["li0ei0ei0ee", [0, 0, 0]],
	["li0e4:spame", [0, "spam"]],
	["llee", [[]]],
	["li0eli0ei0eee", [0, [0, 0]]]
]

# spin through the decode test data, and generate tests.
def test_decode():
	for i in decode_test_data:
		yield check_decode, i[0], i[1]

def check_decode(x, y):
		assert decode(x) == y