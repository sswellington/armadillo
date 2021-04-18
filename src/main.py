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
    
    logging.info("Auth End")
    logging.info("Bearer Beging")
    
    access_token = bearer["access_token"]
    url = 'https://api.escavador.com/api/v1/busca'

    params = {
        'q': 'João Silva',  
        'qo': 't',  
        'page': '1'
    }

    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.get(url, headers=headers, params=params)
    print(json.loads(response.content))
    

    logging.info("Bearer End")