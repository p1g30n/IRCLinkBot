def main(data):
    import urllib2
    from bs4 import BeautifulSoup
    if '!gg ' in data['recv']:
        args = argv('!gg', data['recv'])
        query = urllib2.quote(' '.join(args['argv'][1:]), safe='')
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:73.0) Gecko/20100101 Firefox/73.0')]
        url = 'https://www.google.com/search?hl=en&q=' + query
        page = opener.open(url).read()
        soup = BeautifulSoup(page, "lxml")
        text = soup.find_all("span", {"class": "st"})[1].getText()
        link = soup.find_all("div", {"class": "r"})[0].find("a")
        if len(text) == 0:
            data['api'].say(args['channel'], args['nick'] + ': ' + "Nothing bro")
            return
        else:
            data['api'].say(args['channel'], text + " ^ "+ link["href"] +" | "+ url +" ^")