def main(data):
    if data['config']['settings']['botNick'] in data['recv']\
            or data['config']['settings']['botNick'].lower() in data['recv']:
        import requests
        import json
        class CleverBot(object):
            def __init__(self, user, key, nick=None):
                self.user = user
                self.key = key
                self.nick = nick

                body = {
                    'user': user,
                    'key': key,
                    'nick': nick
                }

                requests.post('https://cleverbot.io/1.0/create', json=body)


            def query(self, text):
                body = {
                    'user': self.user,
                    'key': self.key,
                    'nick': self.nick,
                    'text': text
                }

                r = requests.post('https://cleverbot.io/1.0/ask', json=body)
                r = json.loads(r.text)

                if r['status'] == 'success':
                    return r['response']
                else:
                    return False
        args = argv('', data['recv'])
        query = args['message']
        query = query.replace('\n','')
        query = query.replace('\r','')
        client = CleverBot(user='zfGBW2stCf5BgwVn', key='B2zNaEh5upGyWkpvFgvphHkPVinMFthX')
        answer = client.query(query)
        try:
            if answer:
                debug = 'Query: ' + query + ' -- Answer: "' + answer + '"'
                print debug
                data['api'].say(args['channel'], args['nick'] + ': ' + answer)
        except:
            print "error querying cleverbot"
