# -*- coding: utf-8 -*-
from std_http import std_http
from std_web import std_web
import hashlib
import re 

class crawlnode:
    
    def __init__(self, main):
        self.parent = main
        self.hash = "";



    def addurl(self, url, checked, wid,type=0):
        if not self.parent.urls.has_key(url):
            self.parent.urls.update({url:{'checked':checked,'wid':wid}})                    
            if type==1:
                if self.parent.restrict:
                    pattern = """%s""" % self.parent.restrict
                   # print pattern
                    if re.search(pattern, url):
                        self.addtocrawl(url)
                else:
                    self.addtocrawl(url)
        
            

    def updateurl(self, url, checked):
        if self.parent.urls.has_key(url):
            self.parent.urls[url]['checked'] = checked;
        
    def addtocrawl(self, url):
        if not self.parent.tocrawl.has_key(url):
            self.parent.tocrawl.update({url:1})
    
    def get_wid(self, url):
        if self.parent.urls.has_key(url):
            return self.parent.urls[url]['wid']
    
    def update_link(self, url, status):
        wid= self.get_wid(url)
        if wid:        
            self.parent.db.execute("""update links set status=%s where wid=%s""",(status, wid))
            self.parent.db.commit();        
    
    def add_link(self, url, data, status=0):
        wid= self.get_wid(url)
        if not wid:      
            self.hash = hashlib.md5()
            self.hash.update(url)                
            self.parent.db.execute("""insert links (hash, protocol, domain, path, type, status) values (%s,%s,%s,%s,%s,%s)""",(self.hash.hexdigest(),data['ptr'], data['dom'], data['path'], data['type'], status))
            self.parent.db.commit();
            return self.parent.db.last_insert_id();
        else:
            if(status):
                self.update_link(url, status)
            return wid;   
        
    
    def add_achors(self, wid, data):
        for anchor in links[link]['tags']:                   
            self.parent.db.execute(u"""insert anchor (wid, anchor) values (%s,%s)""",(last_id, anchor[0]))
            self.parent.db.commit();        
    
    def start_node(self, url):
        print "Crawling ", url
        http = std_http()
        web = std_web(self.parent)
        if http.check_url(url):
            response = http.get_page(url)
            status = response[0]['status']
            print status
            data = web.process_url(url);
            wid = self.add_link(url, data,status)
            self.addurl(url, 1, wid, 1)            
            links = web.get_all_links(url, response[1])
            
            for link in links:
               
                lwid = self.add_link(link, links[link]['info'])                
                self.addurl(link, 0, lwid, links[link]['info']['type'])
                
                # print link
                # print links[link]['info']
                

                for anchor in links[link]['tags']:                                      
                    self.parent.db.execute(u"""insert anchor (wid, anchor, pwid) values (%s,%s,%s)""",(lwid, anchor, wid))
                    self.parent.db.commit();
                                                
                # print "\t",links[link]
                # for anchor in links[link]:
                #    print anchor
            # web.get_all_links(response[1])   
            
        else:
            print "error"     