# -*- coding: utf-8 -*-
from std_http import *
from std_web import std_web
from std_db import *


url = "http://www.duoc.cl"

http = std_http()
web = std_web()
db = std_db();
db_args = {'host':'127.0.0.1', 'user':'root', 'passwd':'websites'}
self.db.setParams(db_args)
self.db.connect();
self.db.selectDb('crawl')

if http.check_url(url):
    response = http.get_page(url)
    links = web.get_all_links(url,response[1])
    #print links
    for link in links:
        print link
        print "\t",links[link]
        
    #web.get_all_links(response[1])   
    
else:
    print "error"

