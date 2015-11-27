#coding: utf-8

__author__ = 'wsdevotion'


import urllib2
import json


the_url = 'http://www.tuling123.com/openapi/api?key=ef504bf4ad2860f8bbc98e97426bb9f3&info='

import urllib2
import cStringIO
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def assistant(str):
    while True:
        html = urllib2.urlopen(the_url + str)
        hjson = json.loads(html.read())
        if hjson['code'] == 100000:
            return hjson['text']
        elif hjson['code'] == 200000:
            return hjson['text']
            # ImageScale(hjson['url'])
        elif hjson['code'] == 302000:
            str = ""
            for m in hjson['list']:
                str = str + m['article'] + "\n"
                str = str + "=====>" + m['source'] + "\n"
                str = str + "链接:" + m['detailurl'] + "\n"

            return str
        elif hjson['code'] == 308000:
            for m in hjson['list']:
                str = str + "=====>" + m['name'] + "\n"
                str = str + "=====>" + m['info'] + "\n"
                str = str + "链接:" + m['detailurl'] + "\n"

            return str
    # print hjson['images']['large']
    # print hjson['summary']



