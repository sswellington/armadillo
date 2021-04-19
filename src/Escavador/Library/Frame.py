import requests


class Frame(object):
    def __init__(self):
        self.verb = ''
        self.url = ''
        self.headers= ''


    @property
    def verb(self):
        return self._verb 
    
    @verb.setter
    def verb(self, verb):
        self._verb = verb.upper()
        
    @verb.deleter
    def verb(self):
        del self._verb
        
    
    @property
    def url(self):
        return self._url 
    
    @url.setter
    def url(self, url):
        self._url = url
        
    @url.deleter
    def url(self):
        del self._url
    
    
    @property
    def headers(self):
        return self._headers 
    
    @headers.setter
    def headers(self, headers):
        self._headers = headers
        
    @headers.deleter
    def headers(self):
        del self._headers
