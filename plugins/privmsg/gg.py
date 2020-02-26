def main(data):
    import urllib2
    from bs4 import BeautifulSoup
    if '!gg ' in data['recv']:
        args = argv('!google', data['recv'])
        query = ' '.join(args['argv'][1:])
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:73.0) Gecko/20100101 Firefox/73.0')]
        search_url = 'https://www.google.com/search?hl=en&q=' + query + '&hl=en'
        page = opener.open(search_url).read()
        soup = BeautifulSoup(page, "lxml")
        souptext = soup.find_all("span", {"class": "st"})
        link = soup.find_all("div", {"class": "r"})[0].find("a")
        text = souptext[1].getText()
        if len(text) == 0:
            data['api'].say(args['channel'], args['nick'] + ': ' + "Nothing bro")
            return
        else:
            data['api'].say(args['channel'], args['nick'] + ': ' + text + " ^ "+ link["href"] +" ^")