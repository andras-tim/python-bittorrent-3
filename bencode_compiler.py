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
	def __init__(self, children = None):
		self.children = children

	# two lists are equal if they contain the same items.
	def __eq__(self, other):
		return self.children == other.children

	# emit the node as a python object.
	def emit_python_object(self):
		return []

# turn a string of bencoded data into a tokenised list.
def tokenise(data):
	pointer = 0
	tokens = []

	# while the pointer is within the string,
	while pointer < len(data):
		# if the pointer is a bencoded integer,
		if data[pointer] == "i":
			# find the end, add it to the tokens,
			end_index = data.find("e") + 1
			tokens.append(data[:end_index])
			# and add the length of the integer to the pointer.
			pointer += end_index

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
		# return an empty node, to represent a list.
		return list_node()

# turn a parse tree into a python object.
def emit(parse_tree):
	# just go through the tree.
	return parse_tree.emit_python_object()