import re
def main(data):
	sups = ["sup", "hi", "yo", "hola", "hello", "gday", "good morning", "good night", "kek", "lol", "wat"]
	msg = data['recv'].lower().split(":")[2].rstrip("\n\r")
	print msg
	for sup in sups:
		if msg and msg in sup:
			args = argv(sup, data['recv'])
			if len(args['argv']) == 1:
				data['api'].say(args['channel'], sup)
