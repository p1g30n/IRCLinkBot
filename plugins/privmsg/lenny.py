# -*- coding: utf8 -*-
def main(data):
	if '!lenny' in data['recv']:
		if any(word.lower() in data['recv'].lower() for word in data['config']['settings']['blocklist']):
			return
		args = argv('!lenny', data['recv'])
		data['api'].say(args['channel'], '( ͡° ͜ʖ ͡°)')