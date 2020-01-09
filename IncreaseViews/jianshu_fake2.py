# -*- coding:utf-8 -*-
import sys
import random
import requests
import pycurl
import urllib
import json
import re
import time
import datetime
import io

# class definition

#判断是否刷新次数

class flash_judge:
    def isFlash(self):
        count = 2
        if self.isWeekend():
            count = 5
        return count
    def isWeekend(self):
        if datetime.datetime.now().weekday() > 4:
            return 1
        return 0

class flash_view:
    def __init__(self):
        self.c = None
        # self.init()
    def getArticleList(self, listUrl):
        buffer = io.BytesIO()
        self.c.setopt(pycurl.URL, listUrl)
        self.c.setopt(pycurl.POST, 0)
        self.c.setopt(self.c.WRITEDATA, buffer)
        self.c.perform()
        body = buffer.getvalue().decode('utf-8')
        listUrl = re.findall(r'<a class="title" target="_blank" href=\"(.*)\">(.*)</a>', body)
        return listUrl
    #首次请求得到uuid和次数
    # def firstRequest(self, isView = 1):
    #     buffer = io.BytesIO()
    #     self.c.setopt(pycurl.URL, self.website)
    #     self.c.setopt(pycurl.POST, 0)
    #     self.c.setopt(self.c.WRITEDATA, buffer)
    #     self.c.perform()
    #     body = buffer.getvalue().decode('utf-8')
    #     if isView is not None:
    #         view_count = re.search(r"views_count\":(\d+)", body).group(1)
    #         self.uuid = re.search(r"uuid\":\"(.+)\"}", body).group(1)
    #         self.data_note_id = re.search(r'<div data-vcomp="recommended-notes" data-lazy="1.5" data-note-id=\"(.*)\"></div>', body).group(1)
    #         print("time: ".time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+" url:" + self.website + " flash before:" + str(view_count) + ' uuid:' + self.uuid + ' data_id:' + str(self.data_note_id))
    #     else:
    #         view_count = re.search(r"views_count\":(\d+)", body).group(1)
    #         print("time: ".time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+" url:" + self.website + " flash after:" + str(view_count))
    # def setReferer(self,link):
    #     self.website = str(link)
    #     self.c.setopt(pycurl.HTTPHEADER, ['Origin: http://www.jianshu.com','Referer: ' + self.website])  # this line is very important to if we can succeed!
    #
    # def init(self):#程序初始化
    #     self.c = pycurl.Curl()
    #     USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    #
    #     self.c.setopt(self.c.FOLLOWLOCATION, 1)
    #     self.c.setopt(pycurl.VERBOSE, 0)
    #     self.c.setopt(pycurl.FAILONERROR, True)
    #     self.c.setopt(pycurl.USERAGENT, USER_AGENT)
    #     #self.c.setopt(pycurl.COOKIEFILE, "cookie_file_name")
    #     #self.c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
    #
    # def flashView(self):#刷次数
    #     data_form = {
    #         'uuid': self.uuid,
    #     }
    #     url = self.website.replace("/p/", "/notes/") + '/mark_viewed.json'
    #     # print data_form
    #     buffer = io.BytesIO()
    #     data_post = urllib.parse.urlencode(data_form)
    #
    #     self.c.setopt(pycurl.URL, url)
    #     self.c.setopt(pycurl.POST, 1)
    #     self.c.setopt(pycurl.POSTFIELDS, data_post)
    #     self.c.setopt(self.c.WRITEFUNCTION, buffer.write)
    #     self.c.perform()
    #
    #     #response = buffer.getvalue()
        #print(response)
        #response_json = json.loads(response)
    # def praise(self):#点赞 需要登录
    #     data_form = {
    #     'uuid': self.uuid,
    #     }
    #     url ='https://www.jianshu.com/notes/' + str(self.data_note_id) + '/like'
    #     buffer = StringIO()
    #     data_post = urllib.urlencode(data_form)
    #
    #     self.c.setopt(pycurl.URL, url)
    #     self.c.setopt(pycurl.POST, 1)
    #     self.c.setopt(pycurl.POSTFIELDS, data_post)
    #     self.c.setopt(self.c.WRITEFUNCTION, buffer.write)
    #     self.c.perform()
    #
    # def exit(self):
    #     self.c.close()


# judge = flash_judge()
# print(judge)
# count = judge.isFlash()
# print(count)
# b = int(random.uniform(1, 50))
# print(b)
app = flash_view()
# count = 5  #刷新次数
articleLists = app.getArticleList('https://www.jianshu.com/u/33e00edf9032') #文章列表页
print(articleLists)
cArticles = 0
for i in articleLists:
    n = 1
    cArticles += 1
    if b != cArticles:
        continue
    app.setReferer('https://www.jianshu.com'+i[0])
    app.firstRequest()  # 请求得到次数和uuid
    while True:
        app.flashView()#刷新次数
        n += 1
        if n > count:
            break
    app.firstRequest(None)  # 检查刷新后次数
    print("")
app.exit()

