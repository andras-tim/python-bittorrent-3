# compiler_tests.py -- tests for the bencode compiler_tests

from bencode_compiler import tokenise, parse, node, emit

# test we can tokenise a bencoded integer.
def test_tokenise_integer():
	assert tokenise("i0e") == ["i0e"]

# test we can parse an integer into a tree (albeit with one node).
def test_parse_integer():
	assert parse(["i0e"]) == node("i0e")

# test we can convert a parse tree into a python object.
def test_emit_integer():
	assert emit(node("i0e")) == 0

# test we can tokenise an empty list.
def test_tokenise_empty_list():
	assert tokenise("le") == ["l", "e"]