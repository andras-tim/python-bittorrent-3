# compiler.py -- bencode compiler

# turn a string of bencoded data into a tokenised list.
def tokenise(data):
	# if the data is a bencoded integer.
	if data.startswith("i"):
		# find the end, and splice it out.
		end_index = data.find("e")
		return [data[:end_index + 1]]