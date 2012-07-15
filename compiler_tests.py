# compiler_tests.py -- tests for the bencode compiler_tests

from bencode_compiler import tokenise, parse, node, emit

# test we can tokenise a bencoded integer.
def test_tokenise_integer():
	assert tokenise("i0e") == ["i0e"]

# test we can parse an integer into a tree (albeit with one node).
def test_parse_integer():
	integer_node = node("i0e")
	assert parse(["i0e"]) == integer_node

# test we can convert a parse tree into a python object.
def test_emit_integer():
	integer_node = node("i0e")
	assert emit(integer_node) == 0