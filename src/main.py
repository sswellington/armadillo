from Escavador import Auth

if __name__ == "__main__" :
    payload = {
        'username': 'meuemail@email.com',  
        'password': 'minha_senha'  
    }

    escavador = Auth(payload)
    
    print(escavador.__repr__())
