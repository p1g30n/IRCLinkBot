import re
import time
def main(data):
	sups = ["ayy", "g'day", "gday", "good morning", "good night", "greetings", "hallo", "hello", "hey", "hey there", "heya", "heyo", "hi", "hiya", "hola", "howdy", "konichiwa", "namaste", "oyasumi", "sup", "wazzup", "whaddup", "yo"]
	msg = data['recv'].lower().split(":")[2].rstrip("\n\r")
	print msg
	for sup in sups:
		if msg == sup:
			args = argv(sup, data['recv'])
			if len(args['argv']) == 1:
				time.sleep(4.2)
				data['api'].say(args['channel'], sup)
