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

        def dialectize(self, text, dialect):
            params = {"text": text, "dialect": dialect}
            target_url = "http://www.rinkworks.com/dialect/dialectt.cgi"
            resp = requests.post(target_url, data=params)
            #print resp.text;
            soup = bs4.BeautifulSoup(resp.text, "lxml")
            result = soup.find("div", {"class":"dialectized_text"}).find('p').text;
            result = result.strip("\r\n")
            #giz_text = giz[39].strip("\r\n")  # Hacky, but consistent.
            return result

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
                dialectsetting = data['config']['settings']['dialect'].lower() 
                dialects = ['redneck' , 'jive', 'cockney', 'fudd', 'bork', 'moron', 'piglatin', 'hckr', 'censor']
                if dialectsetting in dialects:
                    dialectquery = answer
                    dialectanswer = client.dialectize(dialectquery, dialectsetting)
                    try:
                        if dialectanswer:
                            debug = 'Query: ' + dialectquery + ' with dialect: "' + dialectsetting + '" -- Answer: "' + dialectanswer + '"'
                            print debug
                            data['api'].say(args['channel'], args['nick'] + ': ' + dialectanswer)
                    except Exception as gizerr:
                        print gizerr
                        print "error querying gizoogle"
                        data['api'].say(args['channel'], args['nick'] + ': ' + answer)
                else:
                    data['api'].say(args['channel'], args['nick'] + ': ' + answer)
        except Exception as err:
            print err
            print "error querying cleverbot"
