# compiler.py -- bencode compiler

# a node for the bencode parse tree
class node():
	# initialise the node with the token data.
	def __init__(self, data):
		self.data = data

	# two nodes are equal if they contain the same token.
	def __eq__(self, other):
		return self.data == other.data

	# emit the node as a python object.
	def emit_python_object(self):
		# if the data is an integer,
		if self.data.startswith("i"):
			# return a python integer
			end_index = self.data.find("e")
			return int(self.data[1:end_index])

# a node for a list in the bencode parse tree
class list_node():
	# initialise the node with the children's data.
	def __init__(self, children):
		self.children = children

	# two lists are equal if they contain the same items.
	def __eq__(self, other):
		return self.children == other.children

	# emit the node as a python object.
	def emit_python_object(self):
		return map(lambda x: x.emit_python_object(), self.children)

# like list.index(), but give the highest index.
def rindex(needle, haystack):
	i = len(haystack) - 1

	while i != -1:
		if haystack[i] == needle:
			return i

		i -= 1

	raise ValueError

# turn a string of bencoded data into a tokenised list.
def tokenise(data):
	pointer = 0
	tokens = []

	# while the pointer is within the string,
	while pointer < len(data):
		# if the pointer is a bencoded integer,
		if data[pointer] == "i":
			# find the end, add it to the tokens,
			end_index = data.find("e", pointer) + 1
			tokens.append(data[pointer:end_index])
			# and as find returns us an index in relation to the
			# entire string, just set the pointer to the end index.
			pointer = end_index

		# if the pointer is a bencoded string,
		elif data[pointer] in map(str, list(range(10))):
			partitioned_string = data.partition(":")
			offset = len(str(partitioned_string[0])) + 1
			string_length = int(partitioned_string[0])

			print partitioned_string
			print offset
			print string_length

			string = data[pointer + offset:pointer + offset + string_length]
			tokens.append(string)
			pointer += offset + string_length

		# if the data is a list,
		elif data[pointer] == "l":
			# add the token,
			tokens.append("l")
			# and move the pointer on one.
			pointer += 1

		# if the data is the end of a list or dict,
		elif data[pointer] == "e":
			# add the token,
			tokens.append("e")
			# and move the pointer on one.
			pointer += 1

	return tokens

# turn a list of tokens into a parse tree.
def parse(tokens):
	# if the first token is an integer,
	if tokens[0].startswith("i"):
		# then just make a node out of the token.
		return node(tokens[0])

	# if the first token is a list,
	if tokens[0] == "l":
		# and is an empty list, return a node.
		if tokens[1] == "e":
			return list_node([])

		# otherwise, find the other end of this list,
		associated_end = rindex("e", tokens)

		# construct an empty node, to represent the list,
		l = list_node([])

		# and then parse all the tokens inside, and add them to the node.
		parsed_inner_tokens = parse(tokens[1:associated_end])
		l.children.append(parsed_inner_tokens)

		return l

# turn a parse tree into a python object.
def emit(parse_tree):
	# just go through the tree.
	return parse_tree.emit_python_object()

# decode a bencoded string.
def decode(bencoded_string):
	tokens = tokenise(bencoded_string)
	parse_tree = parse(tokens)
	return emit(parse_tree)