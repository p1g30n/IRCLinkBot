def main(data):
    import requests
    import re
    from bs4 import BeautifulSoup
    if '!gg ' in data['recv']:
        args = argv('!gg', data['recv'])
        query = requests.utils.quote(' '.join(args['argv'][1:]))
        print query
        headers = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:73.0) Gecko/20100101 Firefox/73.0',
        'Accept-Language': 'en-US,en;q=0.5'}
        payload = {'query': query, 'lui': 'english', 'language': 'english', 'qsr': 'en_US'}
        url = 'https://startpage.com/do/metasearch.pl?query=' + query
        display_url = 'https://www.google.com/search?q=' + query
        page = requests.post(url, data=payload, headers=headers)
        soup = BeautifulSoup(page.text, "lxml")
        text = soup.find_all("p", {"class": "w-gl__description"})[0].getText()
        link = soup.find_all("a", {"class": "w-gl__result-title"})[0]
        # count = re.findall("([0-9.]*[0-9]+)", soup.find_all("div", {"id": "result-stats"})[0].getText());
        results = "(over 9000 results)"
        if len(text) == 0:
            data['api'].say(args['channel'], args['nick'] + ': ' + "Nothing bro")
            return
        else:
            data['api'].say(args['channel'], text + " ^ "+ link["href"] +" | "+ display_url +" ^  "+results)