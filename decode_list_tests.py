# decode_list_tests.py -- tests for decoding lists.

from bencode import decode

# test we can decode an empty list.
def test_decode_empty_list():
	assert decode("le") == []

# test we can decode a list with a single integer in.
def test_decode_one_integer_list():
	assert decode("li0ee") == [0]

# test we can decode a list with a string in it.
def test_decode_one_string_list():
	assert decode("l4:spame") == ["spam"]

# test we can decode a list with two strings in it.
def test_decode_two_string_list():
	assert decode("l4:spam4:spame") == ["spam", "spam"]

# test we can decode a list with two integers in it.
def test_decode_two_integer_list():
	assert decode("li0ei0ee") == [0, 0]

# test we can decode a list with three integers in it.
def test_decode_three_integer_list():
	assert decode("li0ei0ei0ee") == [0, 0, 0]

# test we can decode a list with an integer and a string.
def test_decode_integer_string_list():
	assert decode("li0e4:spame") == [0, "spam"]

# test we can decode an empty list within a list.
def test_decode_empty_list_in_list():
	assert decode("llee") == [[]]