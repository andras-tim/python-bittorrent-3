# encode_tests.py -- tests for the encoding function.

from bencode import encode

# test we can encode a list.
def test_encode_list():
	assert encode([]) == "le"

# test we can encode a list with a single number in it.
def test_encode_list_with_number():
	assert encode([0]) == "li0ee"

# test we can encode a list with three numbers in it.
def test_encode_list_with_numbers():
	assert encode([0, 1, 2]) == "li0ei1ei2ee"

# test we can encode a list with a list in it.
def test_encode_nested_list():
	assert encode([[]]) == "llee"

# test we can encode a number.
def test_encode_number():
	assert encode(0) == "i0e"

# test we can encode a string.
def test_encode_string():
	assert encode("spam") == "4:spam"

# test we can encode a list containing a string.
def test_encode_list_with_string():
	assert encode(["spam"]) == "l4:spame"

# test we can encode an empty dictionary.
def test_encode_empty_dictionary():
	assert encode({}) == "de"

# test an assertion is raised if all dictionary keys aren't strings.
def test_error_dictionary_keys_arent_strings():
	error = False

	try:
		encode({1:"a"})
	except AssertionError as e:
		error = True

	assert error