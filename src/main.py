import json
import logging
import requests

from Armadillo import Armadillo


def login():
    """ forma de realizar login, sem expor os dados de autentificação """
    l = []    
    f = open('_vault/auth.txt', 'r')
    for line in f:
        l.append(line)
    f.close()
    return l


if __name__ == "__main__" : 
    
    tatu = Armadillo(
        (((login())[0]).strip()),
        ((login())[1])
    )
    search = "Mariza Ferro"
    
    response = tatu.query(search)
    with open('database/'+search+'.json', 'a', encoding='utf-8') as f:
        json.dump(json.loads(response.content), f, ensure_ascii=False, indent=4)
        f.write('\n')
        f.write('\n')      
    del response
    