# compiler_tests.py -- tests for the bencode compiler_tests

from bencode_compiler import tokenise, parse, emit, node, list_node, rindex

tokenise_test_data = [
	["i0e",	["i0e"]],
	["le",	["l", "e"]],
	["li0ee", ["l", "i0e", "e"]],
	["li0ei0ei0ee", ["l", "i0e", "i0e", "i0e", "e"]],
	["llee", ["l", "l", "e", "e"]],
	["li0elei0ee", ["l", "i0e", "l", "e", "i0e", "e"]],
	["1:a", ["1:a"]]
]

# spin through the tokenised test data, and generate tests.
def test_tokenise():
	for i in tokenise_test_data:
		yield lambda x, y: tokenise(x) == y, i[0], i[1]

class TestParse():
	# test we can parse an integer into a tree (albeit with one node).
	def test_parse_integer(self):
		assert parse(["i0e"]) == node("i0e")

	# test we can parse a list into a list node.
	def test_parse_empty_list(self):
		assert parse(["l", "e"]) == list_node([])

	# test the empty list node has no children
	def test_parse_empty_list_children(self):
		result = parse(["l", "e"])
		assert result.children == []

	# test we can parse the tokens of a list with an integer.
	def test_parse_list_with_integer(self):
		expected = list_node([])
		expected.children.append(node("i0e"))

		assert parse(["l", "i0e", "e"]) == expected

	# test the integer list node has one child.
	def test_parse_integer_list_children(self):
		assert parse(["l", "i0e", "e"]).children == [node("i0e")]

	# test we can parse embedded lists.
	def test_parse_embedded_list(self):
		assert parse(["l", "l", "e", "e"]) == list_node([list_node([])])

	# test we can parse a triply embedded list.
	def test_parse_triply_embedded_list(self):
		expected = list_node([list_node([list_node([])])])
		assert parse(["l", "l", "l", "e", "e", "e"]) == expected

class TestEmit():
	# test we can convert a parse tree into a python object.
	def test_emit_integer(self):
		assert emit(node("i0e")) == 0

	# test we can convert a parse tree of an empty list into a python object/
	def test_emit_empty_list(self):
		assert emit(list_node([])) == []

	# test we can convert a tree of a list with an integer into a python object.
	def test_emit_list_with_integer(self):
		assert emit(parse(["l", "i0e", "e"])) == [0]

	# test we can convert an embedded list into a python object.
	def test_emit_embedded_list(self):
		assert emit(parse(["l", "l", "e", "e"])) == [[]]

class TestListRindex():
	# test we can get the index on a simple list.
	def test_one_item_list(self):
		rindex(1, [1]) == 0

	# test we can get the index on a larger list.
	def test_three_item_list(self):
		rindex(1, [1, 2, 1, 2]) == 2

	# test a ValueError is raised if the target is not in the list.
	def test_item_not_in_list(self):
		exceptionRaised = False

		try:
			rindex(0, [1])
		except ValueError:
			exceptionRaised = True

		assert exceptionRaised