# -*- coding:utf-8 -*-  
'''
Created on Dec 14, 2017
hmtl下载器
@author: liaot
'''
import urllib2
class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return
        # 设置超时时间 反正访问速度慢造成程序假死
        response = urllib2.urlopen(url, timeout=5)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
