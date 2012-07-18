# compiler_tests.py -- tests for the bencode compiler_tests

from bencode_compiler import tokenise, parse, emit, node, list_node

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

# test we can parse a list into a list node.
def test_parse_empty_list():
	result = parse(["l", "e"])

	assert result == list_node()
	assert result.children == []	# test the list node has no children.

# test we can convert a parse tree of an empty list into a python object/
def test_emit_empty_list():
	assert emit(list_node()) == []

# test we can tokenise a list containing a bencoded integer.
def test_tokenise_list_with_integer():
	assert tokenise("li0ee") == ["l", "i0e", "e"]

# test we can parse the tokens of a list with an integer.
def test_parse_list_with_integer():
	result = parse(["l", "i0e", "e"])

	assert result == list_node()
	assert result.children == [node("i0e")]