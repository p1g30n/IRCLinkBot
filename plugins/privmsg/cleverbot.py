### cleverbot "free" ###
def main(data):
    import subprocess
    import base64
    import re
    if data['config']['settings']['botNick'] in data['recv']\
            or data['config']['settings']['botNick'].lower() in data['recv']:
            if base64.b64decode("OkFub25PcHMzMTM2MiE=") not in data['recv']:
                args = argv('', data['recv'])
                query = args['message'].replace('\n','').replace('\r','')
                query = re.sub(data['config']['settings']['botNick'].lower()+" ", "", query)
                cbpath = "../cleverbot-free/cleverbot.js"
                histfile = "../cleverbot-free/history.txt"
                try:
                    answer = subprocess.check_output(["node", cbpath, query])
                except subprocess.CalledProcessError as e:
                    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
                data['api'].say(args['channel'], args['nick'] + ': ' + answer)
                with open(histfile, "a") as history:
                    history.write(query+"\n")

### botlibre.com ###
# def main(data):
#     import requests
#     import random
#     import base64
#     import json
#     import bs4
#     from xml.etree import ElementTree as ET

#     if data['config']['settings']['botNick'] in data['recv']\
#             or data['config']['settings']['botNick'].lower() in data['recv']:
#             if base64.b64decode("OkFub25PcHMzMTM2MiE=") not in data['recv']:
#                 args = argv('', data['recv'])
#                 query = args['message'].replace('\n','').replace('\r','')
#                 instance = data['config']['settings']['botlibreid'].lower()
#                 reply = requests.get("https://www.botlibre.com/rest/api/form-chat?&application=7400176344752699109&instance="+instance+"&message="+query)
#                 root = ET.fromstring(reply.text)
#                 answer = root[0].text
#                 data['api'].say(args['channel'], args['nick'] + ': ' + answer)

### cleverbot.io ###
# def main(data):
#     import requests
#     import random
#     import json
#     import bs4
#     class CleverBot(object):
#         def __init__(self, user, key, nick=None):
#             self.user = user
#             self.key = key
#             self.nick = nick

#             body = {
#                 'user': user,
#                 'key': key,
#                 'nick': nick
#             }

#             requests.post('https://cleverbot.io/1.0/create', json=body)


#         def query(self, text):
#             body = {
#                 'user': self.user,
#                 'key': self.key,
#                 'nick': self.nick,
#                 'text': text
#             }

#             r = requests.post('https://cleverbot.io/1.0/ask', json=body)
#             r = json.loads(r.text)

#             if r['status'] == 'success':
#                 return r['response']
#             else:
#                 return False

#         def dialectize(self, text, dialect):
#             params = {"text": text, "dialect": dialect}
#             target_url = "http://www.rinkworks.com/dialect/dialectt.cgi"
#             resp = requests.post(target_url, data=params)
#             #print resp.text;
#             soup = bs4.BeautifulSoup(resp.text, "lxml")
#             result = soup.find("div", {"class":"dialectized_text"}).find('p').text;
#             result = result.strip("\r\n")
#             #giz_text = giz[39].strip("\r\n")  # Hacky, but consistent.
#             return result

#     if data['config']['settings']['botNick'] in data['recv']\
#             or data['config']['settings']['botNick'].lower() in data['recv']:
#         args = argv('', data['recv'])
#         query = args['message']
#         query = query.replace('\n','')
#         query = query.replace('\r','')
#         client = CleverBot(user='zfGBW2stCf5BgwVn', key='B2zNaEh5upGyWkpvFgvphHkPVinMFthX', nick=data['config']['settings']['botNick'].lower())
#         answer = client.query(query)
#         try:
#             if answer:
#                 debug = 'Query: ' + query + ' -- Answer: "' + answer + '"'
#                 print debug
#                 dialect = data['config']['settings']['dialect'].lower()
#                 dialects = ['redneck' , 'jive', 'hckr', 'fudd', 'bork', 'cockney', 'moron', 'piglatin', 'censor']
#                 if dialect == "random":
#                     dialect = dialects[random.randint(0,4)]
#                 if dialect in dialects:
#                     diaquery = answer
#                     dianswer = client.dialectize(diaquery, dialect)
#                     try:
#                         if dianswer:
#                             debug = 'Query: ' + diaquery + ' with dialect: "' + dialect + '" -- Answer: "' + dianswer + '"'
#                             print debug
#                             data['api'].say(args['channel'], args['nick'] + ': ' + dianswer)
#                     except Exception as diaerr:
#                         print diaerr
#                         print "error querying dialectizr"
#                         data['api'].say(args['channel'], args['nick'] + ': ' + answer)
#                 else:
#                     data['api'].say(args['channel'], args['nick'] + ': ' + answer)
#         except Exception as err:
#             print err
#             print "error querying cleverbot"