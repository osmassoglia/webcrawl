# -*- coding: utf-8 -*-
from std_http import std_http
from std_web import std_web
from crawlnode import crawlnode
from urlparse import urlparse

class websitecrawl:
    
    def __init__(self):
        self.website = '';
        self.tlinks = 0; # Total links
        self.ilinks = 0; # Internal links
        self.elinks = 0; # External links
        self.clinks = 0; # Checked links
        
        self.domain = '';
        self.protocol = '';
        
        self.urls = {}
        self.tocrawl = {}
        self.db = '';
        #Default values
        self.restrict = "";
        self.maxpages = 1000;
        
    def set_parameter(self, name, value):
        setattr(self, name, value)
        

    def set_enviroment(self, url):
        schemabase = urlparse(url);
        self.protocol = schemabase[0]
        self.domain = schemabase[1]
        print "Enviroment setted ..."
        
    
    def start_crawl(self, url):
        node = crawlnode(self);
        self.set_enviroment(url)        
        print "Starting Crawl ...", url
        node.start_node(url)
        print "First Crawl Finish"
        print self.tocrawl
        while len(self.tocrawl):
            print "Left(s) ",len(self.tocrawl)            
            nurl , value = self.tocrawl.popitem()
            node.start_node(nurl)
        