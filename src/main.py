import json
import logging
# import pandas as pd
import requests

from Escavador import Auth, Query


def login():
    """ forma de realizar login, sem expor os dados de autentificação """
    l = []    
    f = open('_vault/auth.txt', 'r')
    for line in f:
        l.append(line)
    f.close()
    return l


if __name__ == "__main__" :

    logging.basicConfig(filename=('log/main.txt'),
            level=logging.DEBUG, 
            format=' %(asctime)s - %(levelname)s - %(message)s')
    
    ''' LOGIN : INICIO '''
    EMAIL = ((login())[0]).strip()  # substitua o campo pelo seu email
    PWD = ((login())[1])            # substitua o campo pela sua senha
    ''' LOGIN : FIM '''
    
    ''' PESQUISA : INICIO
        q : O termo a ser pesquisado.
            Você pode pesquisar entre aspas duplas para match perfeito
        qo: Tipo da entidade a ser pesquisada    
            t : Para pesquisar todos os tipos de entidades.
            p : Para pesquisar apenas as pessoas.
            i : Para pesquisar apenas as instituições.
            pa: Para pesquisar apenas as patentes.
            d : Para pesquisar apenas os Diários Oficiais. 
    '''
    PESQUISA = {
        'q': "Mariza Ferro",   
        'qo': 'p',
        # 'limit': '10',  # Número de itens que serão retornados por página, opcional 
        # 'page': '1'  # Número da página, respeitando o limite informado, opcional
    }
    ''' PESQUISA : FIM '''
    
    ''' NÃO É NECESSÁRIO ALTERAR AS INFORMAÇÕES ABAIXO '''
    logging.info("Auth Beging")
    
    oauth = Auth(EMAIL, PWD)    
    try: 
        bearer = oauth.bearer()
    except:
        logging.warning("Error: email or password incorrect")
        raise("Error: email ou senha incorreto")
    finally:
        del oauth    
        del EMAIL
        del PWD
    
    logging.debug(bearer)
    logging.info("Auth End")
    logging.info("Bearer Beging")

    try: 
        tatu = Query(bearer)    
    except: 
        logging.warning("Error: bearer token incorrect")
        raise("Error: token bearer incorreto")
    
    logging.info("Bearer End")
    logging.info("Query Begin")
        
    response = tatu.search_all_data(PESQUISA)
    logging.info(response.content)
    del tatu
    del PESQUISA
    
    with open('database/sampling.json', 'a', encoding='utf-8') as f:
        json.dump(json.loads(response.content), f, ensure_ascii=False, indent=4)
        f.write('\n')
        f.write('\n')      
    del response
    
    
    """ Error: json file - arrays must all be same length 
        https://pandas.pydata.org/docs/reference/api/pandas.read_json.html
        https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
    """
    # # data = response.text
    # # df = pd.json_normalize(data['links'])
    # df = pd.read_json('database/sampling.csv')
    # df.to_csv('database/sampling.csv')
    
    logging.info("Query End")
    