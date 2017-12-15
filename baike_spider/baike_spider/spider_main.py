# -*- coding:utf-8 -*-  
'''
Created on Dec 14, 2017
爬虫主控
@author: liaot
'''
import url_manager, html_downloader, \
    html_outputer, html_parser
import traceback


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    # 爬虫启动
    def craw(self, root_url):
        count = 1
        # 将root url添加到url管理器
        self.urls.add_new_url(root_url)
        # 循环爬去新的url
        while self.urls.has_new_url():
            try:
                # 获取一个新的url
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                # 下载网页内容
                html_cont = self.downloader.download(new_url)
                # 解析下载的html 返回新的url集合 和解析出来的数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                
                # 将new_urls添加到url管理器中
                self.urls.add_new_urls(new_urls)
                # 输出 解析数据
                self.outputer.collect_data(new_data)
                
                if count == 1000:
                    break
                count += 1
            except Exception as e:
                print 'craw failed'
                # 异常时输出完整的堆栈信息
                print traceback.format_exc()
        # 将爬虫的最终结果输出在html上
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)