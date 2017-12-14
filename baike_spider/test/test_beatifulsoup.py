# -*- coding:utf-8 -*-  
'''
Created on Dec 14, 2017

@author: liaot
'''
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print "get all links"
links = soup.findAll('a')
print links

print 'get lacie`link'
link = soup.find('a', href='http://example.com/lacie')
print link

print '正则匹配'
link = soup.find('a', href=re.compile(r'ill'))
print link

print '获取p段落文字'
link = soup.find('p', class_="title")
print link



