import requests
import json
import logging

from Escavador import Auth, Query


def login():
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
    
    EMAIL = ((login())[0]).strip()  # substitua o campo pelo seu email
    PWD = ((login())[1])            # substitua o campo pela sua senha
    
    logging.info("Auth Beging")
    
    oauth = Auth(EMAIL, PWD)    
    try: 
        bearer = oauth.bearer()
    except:
        logging.warning("Error: email ou senha incorreto")
        raise("Error: email ou senha incorreto")
    finally:
        del oauth    
        del EMAIL
        del PWD
    
    logging.debug(bearer)
    logging.info("Auth End")
    logging.info("Bearer Beging")

    tatu = Query(bearer)
    
    params = {
        'q': "Mariza Ferro",  # O termo a ser pesquisado. 
        'qo': 'p',  # Tipo da entidade a ser pesquisada
        # 'limit': '10',  # Número de itens que serão retornados por página, opcional 
        # 'page': '1'  # Número da página, respeitando o limite informado, opcional
    }
    
    result = tatu.search_all_data(params)
    del tatu
    del params
    
    logging.info(result)
    
    with open('database/sampling.json', 'a', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
        f.write('\n')
        f.write('\n')      
    
    logging.info("Bearer End")
    