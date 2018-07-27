def main(data):
    import requests
    import json
    import bs4
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

        def gizoogle(self, text):
            params = {"translatetext": text}
            target_url = "http://www.gizoogle.net/textilizer.php"
            resp = requests.post(target_url, data=params)
            soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text)
            soup = bs4.BeautifulSoup(soup_input, "lxml")
            giz = soup.find_all(text=True)
            giz_text = giz[39].strip("\r\n")  # Hacky, but consistent.
            return giz_text

    if data['config']['settings']['botNick'] in data['recv']\
            or data['config']['settings']['botNick'].lower() in data['recv']:
        args = argv('', data['recv'])
        query = args['message']
        query = query.replace('\n','')
        query = query.replace('\r','')
        client = CleverBot(user='zfGBW2stCf5BgwVn', key='B2zNaEh5upGyWkpvFgvphHkPVinMFthX', nick=data['config']['settings']['botNick'].lower())
        answer = client.query(query)       
        try:
            if answer:
                debug = 'Query: ' + query + ' -- Answer: "' + answer + '"'
                print debug
                if data['config']['settings']['gizoogle'] == 'True':
                    gizquery = answer
                    gizanswer = client.gizoogle(gizquery)
                    try:
                        if gizanswer:
                            debug = 'Query: ' + gizquery + ' -- Answer: "' + gizanswer + '"'
                            print debug
                            data['api'].say(args['channel'], args['nick'] + ': ' + gizanswer)
                    except Exception as gizerr:
                        print gizerr
                        print "error querying gizoogle"
                        data['api'].say(args['channel'], args['nick'] + ': ' + answer)
                else:
                    data['api'].say(args['channel'], args['nick'] + ': ' + answer)
        except Exception as err:
            print err
            print "error querying cleverbot"
