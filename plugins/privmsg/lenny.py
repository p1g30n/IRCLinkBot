# -*- coding: utf8 -*-
def main(data):
    if '!lenny' in data['recv']:
        args = argv('!lenny', data['recv'])
        data['api'].say(args['channel'], '( ͡° ͜ʖ ͡°)')