# Armadillo

## [API do Escavador](https://api.escavador.com/docs/#api-do-escavador)

O Escavador coleta e compila dados públicos disponíveis em fontes oficiais, desde Diários Oficiais a Tribunais do poder judiciário de todo o Brasil. 
Integre a API do Escavador ao seu sistema e tenha acesso a informações públicas de pessoas, empresas e processos, disponibilizadas de maneira estruturada.

### Autenticação

Utiliza o protocolo OAuth 2.0 para autenticação e autorização, permitindo que aplicações enviem solicitações autenticadas em nome de usuários individuais do Escavador.

O access_token recebido deve ser utilizado no cabeçalho das outras requisições, para que a API identifique o usuário. 
O token de acesso tem vida útil limitada (valor retornado no campo expires_in) e caso expire, será necessário obter um novo token repetindo esta requisição.