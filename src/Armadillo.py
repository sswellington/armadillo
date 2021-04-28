import logging
import requests

from Escavador import Auth, Query


class Armadillo(object):
    
    def __init__(self, email, password): 
        logging.basicConfig(filename=('log/armadillo.txt'),
                level=logging.DEBUG, 
                format=' %(asctime)s - %(levelname)s - %(message)s')
        
        self.entity = 'p'
        self.limit = '1'
        self.page = '1'
        self.bearer = self.get_bearer(email, password)    
    
    
    def get_bearer(self, email, password):
        logging.info("Auth Beging")
    
        oauth = Auth(email, password)    
        try: 
            return oauth.bearer()
        except:
            logging.warning("Error: email or password incorrect")
            raise("Error: email ou senha incorreto")
            return False
        finally:
            del oauth
        
        
    def query(self, search):
        ''' q : O termo a ser pesquisado.
            Você pode pesquisar entre aspas duplas para match perfeito
        '''
        logging.info("Bearer Beging")
        logging.debug(self.bearer)

        try: 
            tatu = Query(self.bearer)    
        except: 
            logging.warning("Error: bearer token incorrect")
            raise("Error: token bearer incorreto")
        
        logging.info("Bearer End")
        logging.info("Query Begin")
        
        parms = {
            'q': search,   
            'qo': self.entity,
            'limit': self.limit, 
            'page': self.page
        }
                
        response = tatu.search_all_data(parms)
        logging.info(response.content)
        del tatu
            
        logging.info("Query End")
        return response
    
    
    @property
    def entity(self):
        return self._entity 
    
    @entity.setter
    def entity(self, entity):
        ''' qo: Tipo da entidade a ser pesquisada    
            t : Para pesquisar todos os tipos de entidades.
            p : Para pesquisar apenas as pessoas.
            i : Para pesquisar apenas as instituições.
            pa: Para pesquisar apenas as patentes.
            d : Para pesquisar apenas os Diários Oficiais.
        '''
        self._entity = entity
        
    @entity.deleter
    def entity(self):
        del self._entity
        
    
    @property
    def limit(self):
        return self._limit 
    
    @limit.setter
    def limit(self, limit):
        '''Número de itens que serão retornados por página'''
        self._limit = limit
        
    @limit.deleter
    def limit(self):
        del self._limit
        
    
    @property
    def page(self):
        return self._page 
    
    @page.setter
    def page(self, page):
        '''Número da página, respeitando o limite informado'''
        self._page = page
        
    @page.deleter
    def page(self):
        del self._page
        
    
    @property
    def bearer(self):
        return self._bearer 
    
    @bearer.setter
    def bearer(self, bearer):
        '''
            O Bearer identifica recursos protegidos por um OAuth2.0.
            O qual o <token> deve ser um string, que representa uma autorização do Server emitida para o cliente. 
            ---
            @parms = self.get_bearer()
        '''
        self._bearer = bearer
        
    @bearer.deleter
    def bearer(self):
        del self._bearer
        