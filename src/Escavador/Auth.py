import logging
import requests
import json


class Auth(object):
    def __init__(self, payload):
        logging.basicConfig(filename=('log/auth.txt'),
            level=logging.DEBUG, 
            format=' %(asctime)s - %(levelname)s - %(message)s')
        
        self.payload = payload
        self.url = 'https://api.escavador.com/api/v1/request-token'
        self.headers = {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/json'}

    
    def __repr__(self):
        response = requests.request('POST', self.url, headers=self.headers, json=self.payload)
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4))
        return (json.dumps(parsed, indent=4))


    @property
    def payload(self):
        return self._payload 
    
    @payload.setter
    def payload(self, payload):
        """        
            | Parâmetro |  Tipo  |	  Status   |          Descrição            |  
            |-----------|--------|-------------|-------------------------------|
            | username	| string | obrigatório | Email do usuário do escavador |
            | password	| string | obrigatório | Senha do usuário do escavador |
        """
        self._payload = payload
        
    @payload.deleter
    def payload(self):
        del self._payload
        
    
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
