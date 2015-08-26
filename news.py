#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import feedparser
from HTMLParser import HTMLParser
from time import sleep
import pprint
import json

link = 'https://www.blognone.com/atom.xml'
x = feedparser.parse(link)
data = open('data.json')
y = json.load(data)
feedData = {}


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def getNews():
    for x.entrie in x.entries:
        #print len(x.entries)
        print x.entrie['guid'].split()[0]
        print x.entrie['link']
        print x.entrie['title'],'\n'
        #sleep(0.15)
        #feedData[id] = {'link': link,'title': title}
#       feedData = {'id': id,'link': link,'title': title}
        #pprint.pprint(feedData)
        text = strip_tags(x.entrie['description'])
        text = text.strip()
        print text
    #print x.entries[0]x.summaryx

def checkNews():
    for x.entrie in x.entries:
        #print len(x.entries)
        id = x.entrie['guid'].split()[0]
        link = x.entrie['link']
        title = x.entrie['title'],'\n'
        #sleep(0.15)
        feedData['result'] = {'id': id,'link': link,'title': title}
#       feedData = {'id': id,'link': link,'title': title}
    pprint.pprint(feedData)
    with open('data.json', 'w') as outfile:
        json.dump(feedData, outfile)




checkNews()
#getNews()



