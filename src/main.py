import requests
import json
import logging

from Escavador import Auth


def login():
    l = []    
    f = open('_vault/auth.txt', 'r')
    for line in f:
        l.append(line)
    f.close()
    return l


def query(bearer_token, query_parameters):
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
    access_token = bearer_token["access_token"]
    url = 'https://api.escavador.com/api/v1/busca'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.get(url, headers = headers, params = query_parameters)
    logging.debug(json.loads(response.content))
    print(json.loads(response.content))    


if __name__ == "__main__" :

    logging.basicConfig(filename=('log/main.txt'),
            level=logging.DEBUG, 
            format=' %(asctime)s - %(levelname)s - %(message)s')
    
    EMAIL = ((login())[0]).strip()  # substitua o campo pelo seu email
    PWD = ((login())[1])            # substitua o campo pela sua senha
    
    logging.info("Auth Beging")
    
    escavador = Auth(EMAIL, PWD)    
    try: 
        bearer = escavador.bearer()
    except:
        logging.warning("Error: email ou senha incorreto")
        raise("Error: email ou senha incorreto")
    finally:
        del EMAIL
        del PWD    
    
    print(bearer)
    
    logging.info("Auth End")
    # logging.info("Bearer Beging")
    
    # params = {
    #     'q': 'Otto Teixeira Fraga Netto',  
    #     'qo': 't',  
    #     'limit': '10',  # opcional
    #     'page': '1'  # opcional
    # }

    # query(bearer, params)
    
    # logging.info("Bearer End")
    