# -*- coding:utf-8 -*-  
'''
Created on Dec 14, 2017
结果html 输出器
@author: liaot
'''

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output.txt', 'w')
        
        for data in self.datas:
            fout.write(data['url'].encode('utf-8') + ", " + data['title'].encode('utf-8') + "\n")
    
    
    
    
