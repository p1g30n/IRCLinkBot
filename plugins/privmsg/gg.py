def main(data):
    import urllib2
    from bs4 import BeautifulSoup
    if '!gg ' in data['recv']:
        args = argv('!gg', data['recv'])
        query = ' '.join(args['argv'][1:])
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:73.0) Gecko/20100101 Firefox/73.0')]
        search_url = 'https://www.google.com/search?hl=en&q=' + query
        page = opener.open(search_url).read()
        soup = BeautifulSoup(page, "lxml")
        text = soup.find_all("span", {"class": "st"})
        link = soup.find_all("div", {"class": "r"})
        text = text[1].getText()
        link = link[0].find("a")
        if len(text) == 0:
            data['api'].say(args['channel'], args['nick'] + ': ' + "Nothing bro")
            return
        else:
            data['api'].say(args['channel'], args['nick'] + ': ' + text + " ^ "+ link["href"] +" ^")