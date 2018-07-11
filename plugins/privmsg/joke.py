def main(data):
	import json
	import random
	import requests
	from HTMLParser import HTMLParser
	if '!jew' in data['recv']:
		parser = HTMLParser()
		args = argv('!jew', data['recv'])
		lines = open('etc/jew.txt').read().splitlines()
		jew = parser.unescape(random.choice(lines))
		data['api'].say(args['channel'], jew)
	if '!yomama' in data['recv']:
		parser = HTMLParser()
		args = argv('!jew', data['recv'])
		lines = open('etc/yomama.txt').read().splitlines()
		yomama = random.choice(lines)
		data['api'].say(args['channel'], yomama)
	if '!jok' in data['recv']:
		args = argv('!joke', data['recv'])
		try:
			response = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
			joke = response.json()
			data['api'].say(args['channel'], joke['joke'])
		except:
		    data['api'].say(args['channel'], 'No jok.')