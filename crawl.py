# -*- coding: utf-8 -*-
from websitecrawl import websitecrawl
from std_db import std_db
from std_http import std_http
from std_web import std_web


url = "http://drupalqa.duoc.cl/"

#http = std_http()
#web = std_web()
db = std_db();
db_args = {'host':'127.0.0.1', 'user':'root', 'passwd':'websites'}
db.setParams(db_args)
db.connect();
db.selectDb('crawl')
db.execute("""TRUNCATE TABLE links""");
db.execute("""TRUNCATE TABLE anchor""");        

website = websitecrawl();
website.set_parameter('db', db);
#website.set_parameter('restrict','/englishprogram/')
website.start_crawl(url);



