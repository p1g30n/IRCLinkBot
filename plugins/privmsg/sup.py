import re
def main(data):
	sups = ["sup", "hi", "yo", "hey", "hello", "hola", "gday", "good morning", "good night"]
	msg = data['recv'].lower().split(":")[2].rstrip("\n\r")
	print msg
	for sup in sups:
		if msg == sup:
			args = argv(sup, data['recv'])
			if len(args['argv']) == 1:
				data['api'].say(args['channel'], sup)
