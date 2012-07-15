# compiler_tests.py -- tests for the bencode compiler_tests

from bencode_compiler import tokenise

# test we can tokenise a bencoded integer.
def test_tokenise_integer():
	assert tokenise("i0e") == ["i0e"]