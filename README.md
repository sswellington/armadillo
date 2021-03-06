# Armadillo

Oferece uma forma de acessar à API do Escador por intermédio de CLI feita em Python 3.9.0 e suas bibliotecas que auxiliam na manipulação do protocolo HTTP, a lista desses estão listados em [requisitos](https://github.com/sswellington/armadillo/blob/main/requirements.txt).
O resultado da consulta é um conjunto de dados semiestruturados em formato json.

Armadillo segue a Política de Dados Abertos do Poder Executivo federal, de maneira a aprimorar a cultura de transparência pública, tendo o objetivo de fomentar o controle social e o desenvolvimento de novas tecnologias destinadas à construção de ambiente de gestão pública participativa e democrática e à melhor oferta de serviços públicos para o cidadão.

Observação, o Armillo não solicita nem um meio de pagamentos.
Entretanto, pode ocorrer cobrança realizada por terceiros, como a API do Escavador, por isto, consulte as informações pelo site da mesma e aproveite para obter a sua credencial.
Além disso, Armillo não realiza a coleta, manipulação dos dados nem proprietário dos mesmos, ou seja, apenas oferece uma interface para acessar os dados do Escavador por intermédio da API do mesmo.

### Como usar
1. Abra a pasta `src`
2. Abra o arquivo `main.py`
3. Faça autentificação:
4. Realizar a pesquisa:   
5. O resultado será exportado em um arquivo para a pasta `database` com o nome `"SEARCH".json`

---

## [API do Escavador](https://api.escavador.com/docs/#api-do-escavador)

O Escavador coleta e compila dados públicos disponíveis em fontes oficiais, desde Diários Oficiais a Tribunais do poder judiciário de todo o Brasil. 
Integre a API do Escavador ao seu sistema e tenha acesso a informações públicas de pessoas, empresas e processos, disponibilizadas de maneira estruturada.

### Autenticação

Utiliza o protocolo [OAuth 2.0](https://tools.ietf.org/html/rfc6749) para autenticação e autorização, permitindo que aplicações enviem solicitações autenticadas em nome de usuários individuais do Escavador.

O access_token recebido deve ser utilizado no cabeçalho das outras requisições, para que a API identifique o usuário. 
O token de acesso tem vida útil limitada (valor retornado no campo expires_in) e caso expire, será necessário obter um novo token repetindo esta requisição.

#### [Bearer](https://tools.ietf.org/html/rfc6750) 

O Bearer identifica recursos protegidos por um OAuth2.0.
No qual o <token> deve ser um string, que representa uma autorização do Server emitida para o client. 
Por sua vez, o client deve possuir mecanismos próprios para identificar e validar o Token.

### Busca

| Parâmetro | Status | Descrição |
|---|---|---|
| q | obrigatório | O termo a ser pesquisado. Você pode pesquisar entre aspas duplas para match perfeito.|
| qo | obrigatório | Tipo da entidade a ser pesquisada. os valores podem ser: <br> **⏺ t:** Para pesquisar todos os tipos de entidades. <br> **⏺ p:** Para pesquisar apenas as pessoas. <br> **⏺ i:** Para pesquisar apenas as instituições. <br> **⏺ pa:** Para pesquisar apenas as patentes. <br> **⏺ d:** Para pesquisar apenas os Diários Oficiais. <br> **⏺ en:** Para pesquisar as pessoas e instituições que são envolvidas em processos. |
| limit | opcional | Número de itens que serão retornados por página. Default: 20 |
| page | opcional | Número da página, respeitando o limite informado. |

---

## [Contribuição](https://github.com/sswellington/armadillo/blob/main/CONTRIBUTING.md)  

Fique à vontade para contribuir com o projeto, toda contribuição é bem vinda.
Sendo possível contribuir de 3 formas: issues, pull requests e revisar pull requests.

## Referência
* [Decreto 8777 de maio de 2016: Política de Dados Abertos do Poder Executivo federal](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/decreto/d8777.htm)
* [Documentação do Python](https://docs.python.org/3/)
* [Documentação da API  do Escavador](https://api.escavador.com/docs/)
* [Segurança - JWT x Cookies x OAuth 2.0 x Bearer por Bruno Brito](https://www.brunobrito.net.br/jwt-cookies-oauth-bearer/)
* [Uso do Flask para consumir api do escavdor por Jonathan Gama](https://github.com/JonathanGamaS/consumo_api_escavador)
* [Modelo de contribução](https://github.com/kelvins/Algoritmos-e-Estruturas-de-Dados/blob/main/CONTRIBUTING.md)
