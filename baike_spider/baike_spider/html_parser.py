# -*- coding:utf-8 -*-  
'''
Created on Dec 14, 2017
html解析器
@author: liaot
'''
import re

from bs4 import BeautifulSoup
import urlparse


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # <a target="_blank" href="/item/GPL">GPL</a>
        links = soup.find_all('a', href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
                               
    
    
    def _get_new_data(self, page_url, soup):
        new_data = {}
        new_data['url'] = page_url
    
        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_data['title'] = title_node.get_text()
        
        return new_data
        
        
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls, new_data
        
    
    
