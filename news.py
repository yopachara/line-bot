#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import feedparser
from HTMLParser import HTMLParser

link = 'https://www.blognone.com/atom.xml'
x = feedparser.parse(link)

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
        print x.entrie['link'],x.entrie['guid']
        print x.entrie['title'],'\n'
        #text = strip_tags(x.entrie['description'])
        #text = text.strip()
        #print text
#print x.entries[0].summary

getNews()



