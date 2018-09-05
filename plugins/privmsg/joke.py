def main(data):
	import json
	import random
	import requests
	from HTMLParser import HTMLParser
	if '!jew' in data['recv']:
		parser = HTMLParser()
		args = argv('!jew', data['recv'])
		lines = open('etc/jewish-jokes.txt').read().splitlines()
		jew = parser.unescape(random.choice(lines))
		data['api'].say(args['channel'], jew)
	if '!yomama' in data['recv']:
		parser = HTMLParser()
		args = argv('!jew', data['recv'])
		lines = open('etc/yomama.txt').read().splitlines()
		yomama = random.choice(lines)
		data['api'].say(args['channel'], yomama)
	if '!insult' in data['recv']:
		args = argv('!insult', data['recv'])
		if args['argv'][1:]:
			nick = ' '.join(args['argv'][1:])
			insult = nick+": "
		else:
			insult = ''
		parser = HTMLParser()
		lines = open('etc/luther.txt').read().splitlines()
		insult += parser.unescape(random.choice(lines))
		data['api'].say(args['channel'], insult)	
	if '!jok' in data['recv']:
		args = argv('!joke', data['recv'])
		try:
			response = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
			joke = response.json()
			data['api'].say(args['channel'], joke['joke'])
		except:
		    data['api'].say(args['channel'], 'No jok.')