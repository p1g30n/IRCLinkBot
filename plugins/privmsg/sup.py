import re
def main(data):
	sups = ["ayy", "gday", "good morning", "good night", "hallo", "hello", "hey", "hi", "hiya", "hola", "howdy", "namaste", "sup", "wazzup", "whaddup", "yo"]
	msg = data['recv'].lower().split(":")[2].rstrip("\n\r")
	print msg
	for sup in sups:
		if msg == sup:
			args = argv(sup, data['recv'])
			if len(args['argv']) == 1:
				data['api'].say(args['channel'], sup)
