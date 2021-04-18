import requests
import json
import logging


class Auth(object):
    def __init__(self, email, password):
        logging.basicConfig(filename=('log/auth_status_codes.txt'),
            level=logging.DEBUG, 
            format=' %(asctime)s - %(levelname)s - %(message)s')
        
        self.verb = 'POST'
        self.url = 'https://api.escavador.com/api/v1/request-token'
        self.headers = {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/json'}
        self.payload = {'username': email, 'password': password}


    def bearer(self):
        response = requests.request(
            self.verb, 
            self.url, 
            headers =self.headers, 
            json =self.payload
        )
        
        """ DEBUG - HTTP response status codes : BEGIN """
        parsed = json.loads(response.text)
        logging.debug(json.dumps(parsed, indent=4))
        """ DEBUG - HTTP response status codes : END """
        
        response_dict = json.loads(response.content)
        return {
            "access_token": response_dict["access_token"], 
            "refresh_token": response_dict["refresh_token"]
        }


    @property
    def payload(self):
        return self._payload 
    
    @payload.setter
    def payload(self, payload):
        self._payload = payload
        
    @payload.deleter
    def payload(self):
        del self._payload


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
