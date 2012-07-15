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

# turn a string of bencoded data into a tokenised list.
def tokenise(data):
	# if the data is a bencoded integer.
	if data.startswith("i"):
		# find the end, and splice it out.
		end_index = data.find("e")
		return [data[:end_index + 1]]

# turn a list of tokens into a parse tree.
def parse(tokens):
	# if the first token is an integer,
	if tokens[0].startswith("i"):
		# then just make a node out of the token.
		return node(tokens[0])

# turn a parse tree into a python object.
def emit(parse_tree):
	# just go through the tree.
	return parse_tree.emit_python_object()