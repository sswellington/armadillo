import requests
import json
import logging

from Escavador.Library import Frame


class Query(Frame):
    def __init__(self, bearer_token):
        logging.basicConfig(filename=('log/query.txt'),
            level=logging.DEBUG, 
            format=' %(asctime)s - %(levelname)s - %(message)s')
        
        super().__init__()
        
        """ Busca em toda base do escador """
        self.url = 'https://api.escavador.com/api/v1/busca'
        
        self.verb = 'GET'
        self.headers = {
            'Authorization': f'Bearer {bearer_token["access_token"]}',
            'X-Requested-With': 'XMLHttpRequest'
        }
         

    def search_all_data(self, query_parameters):
        """ Busca apenas pessoas físicas """
        self.url = 'https://api.escavador.com/api/v1/busca'
        return self._search_engine(query_parameters)
        
            
    # def search_per_peoples(self, id):
    #     """ Busca apenas pessoas físicas """
    #     self.url = 'https://api.escavador.com/api/v1/pessoas/' + str(id)
    #     params = {'q': "otto", 'qo': 'p'}
    #     return self._search_engine(params)
        
        
    def _search_engine(self, params):
        """ Query Parameters
            Parâmetro |	Status      | Descrição
            q	      | obrigatório	| O termo a ser pesquisado. Você pode pesquisar entre aspas duplas para match perfeito.
            qo	      | obrigatório	| Tipo da entidade a ser pesquisada. os valores podem ser:
                t : Para pesquisar todos os tipos de entidades.
                p : Para pesquisar apenas as pessoas.
                i : Para pesquisar apenas as instituições.
                pa: Para pesquisar apenas as patentes.
                d : Para pesquisar apenas os Diários Oficiais.
                en: Para pesquisar as pessoas e instituições que são envolvidas em processos.
            limit     | opcional	| Número de itens que serão retornados por página. Default: 20
            page	  | opcional	| Número da página, respeitando o limite informado.
        """
        response = requests.get(self.url, headers = self.headers, params = params)
        logging.debug(json.loads(response.content))
        return (json.loads(response.content))    
