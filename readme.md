## Entendo o Scrapy

Premissa da biblioteca(API) - Pegar informações web.

<mark>OBS:</mark> No vídeo ele está usando python3.6, possa ser que exista uma versão mais atualizada sendo usada.

- link para baixar outras versões de python (para windows):

https://www.python.org/downloads/windows/

- Info:

<mark>Scrapy</mark> não funciona como um modulo comum, que vai chamando metodo ou funções.
Scrapy é que chamamso de **framework**, que é uma estrutura de programas e arquivos e script de aquivos criados, já feitos.
Uma estrutura mais _especifica_ que facilita a fazer certas tarefas e atividades.
Usando essa estrutura, para conseguir um resultado de forma mais simples. Ao ínvesd e programar tudo, já existem coisas pré programas
para que você possa atingir o objetivo, de forma masi simples, na quala finalidade do framework se objetiva.

Frameqork tem finalidade especifica. logo, toda sua criação e codificação tem um finalidade alvo, que tem que q ser a mesma
que você deseja atingir. por isso escolheu o framwork **Scrapy**, ao in´ves de outro. Você deseja, através dele,
obter o resulatdo com a finalidade que ele foi criado.

O que se diferencia de uso de um biblioteca, onde atarvés de várioos funções de uma bibliorteca, você pdoe também montar 
o seu fremeqork, porém, codificando tudo.

Por isso, pelo passar dos anos, várias pessoas já devem ter tido a mesma finalidade que você em projeto
e isso fez que eles, possam ter criado frameworks que fazem o que você deseja fazer.

Por isso, mais simples usar algo que já foi criado, facilitando nosso trabalho.

Você precisa seqguir uma estrutura para atingir os resulatdos, da codificação no framework, por isso, bom ler a sua 
finalidade e seus passos, para que se consiga tirar o melhor proveito do mesmo.

- Inserir liks dos Vídeos:

- Informações de instalação e configurações da biblioteca Scrapy:

!pip install scrapy (caso não enteja instalado)

import scrapy (para uso da biblioteca)

### Usando conda

- To create an environment:

conda create --name myenv

<mark>Note</mark>

<mark>Replace **myenv** with the environment name.</mark>

- When conda asks you to proceed, type y:

proceed ([y]/n)?

This creates the myenv environment in /envs/. No packages will be installed in this environment.

- To create an environment with a specific version of Python:

conda create -n myenv python=3.6

- ativando ambiente virtual:

conda activate <nomedolocalcriado>

- para desativar:

conda deactivate

## Usando Scrapy (Roteiro do projeto, como no vídeo)

<mark>Tudo foi feito via terminal do anaconda prompt</mark>

**Iniciando projeto**

- scrapy startproject <nomearcomoquiser>(no caso foi: imdb250)

**resposta:**

- You can start your first spider with:</br>
    - cd imdb250</br>
    - scrapy genspider example example.com

Escolher uma das opções dada pelo sistema. 

1 - Como proximo passo, digitamos:

- cd imdb250

2 - Depois: (genspider - Gere um spider faz uma função de sugar os dados)

- scrapy genspider _exemple_ _exemple.com_

**exemple** - Podemos alterar, nomeando a gosto </br>
**exemple.com** - link do site. pode ser alterado posteriormente.

exemplo: _screpy genspider imdb imdb.com_

reposta:

_(filmesimdb) C:\Users\shaff\PycharmProjects\projetoimdb\imdb250>scrapy genspider imdb imdb.com
Created spider 'imdb' using template 'basic' in module:
  imdb250.spiders.imdb_

o arquivo criado, que se encontra dentro da pasta **spiders**, mostrada ao lado esquerdo,
dentro das pastas, já vem com algumas condificações do framework

Ele é um arquivo **.py**,o que significa que ele é um arquivo python. Porém, pelas indicações
que fizemos antes, com o _genspider_, criamos esse arquivo, com os parametros passados como _imdb_
e _imdb.com_, e com isso ele já criou dentro da pasta **spiders** o arquivo e função "pré configuradas".

#### Este arquivo tem muita relevância estar dentro desta pasta.

#### É dentro dela que podemos colocar o link do site onde se irá puxar os dados.

POr conta do fremework, este arquivo com essas informações é relevante. Porém, pode ser criado externamente,
sem o uso do _genspider_. Basta criar dentro da basta com os parâemtros necessários. Novamente, o
framework precisa desse arquivo, com essas configurações para trabalhar de forma correta.

Legenda:

**Classe:**

- import scrapy

- class ImdbSpider(scrapy.Spider):

**nome:**
- nome do arquivo: **imdb**

**start_urls**

- endereço do site para puxar informações: ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

**função:**

- def parse (self, response): </br>
  _incluir objetos aqui_ </br>
  pass

**modelo**

import scrapy


class ImdbSpider(scrapy.Spider): </br>
    name = 'imdb' </br>
    #allowed_domains = ['imdb.com'] </br> # pega de todos os dominios que tenha, caso o site seja mundial e etc
    start_urls = ['http://imdb.com/'] </br>

    def parse(self, response):
      
      for filmes in response.css('.titleColumn'): # trazendo informações do site
          yield{
          'titulos': filmes.css('.titleColumn a::text').get(), # mostra apena o titulo dos filmes
          'lancamento' : filmes.css('.secondaryInfo::text').get(), # Lançamento dos filmes (ano de lançamento)
          'nota' : response.css('strong::text').get() # nota do site para os filmes. As valiações pelos usuários)
          }
        pass

- Deixando apena o _nota_ como _response.css('strong::text)_, pois ele está em outra classe de informação, diferente
das informações ue já vem quando buscamos _('.titleColumn):_ por este motivo não usa o _filmes_ e sim _response_
- yield: Similar ao retorno, funcionando melhor dentro desta framework

Organizado a função para um formato de dicionário. Pegando cada dado do _for filmes_ e seu parâmetro de busca _response.css('.titleColumn'):_

- _.text_, pode ser manipulado como uma string

<mark> Premissa desta condificação e pegar dentro da página alvo, decrita acima e pegar as informações
dentro da função, como escrevemos</mark>

## Sheel para testar a códificação

No terminal do Anaconda prompt, digite:

- scrapy shell + enter

Cria um ambinete controlado para se testar automações, conexões, etc.

**Criar conexão com página web e testes:**

- fetch('https://www.imdb.com/chart/top/?ref_=nv_mv_250') + enter

Verificará a conxão entre o shell( ambiente de treianemtno) e o site.
PRecisaremos da resposta **200**. Qualquer outro código, pode ser erro de digitação e outros.

**Buscar informações no site**

Atavés de inspecionar o site, o html do site, e pegar as classes e/ou objetos para cpatar as informações
de uma determianda área.

<mark>Use o SelectorGedget (baixar a extenção se não extiver instalada)</mark>

SelectorGedget - mostra todas as estruturas de um obejto alvo, facilitando a separação e captura.

Exemplo: _.titleColumn a_ (caixa com nome filme). Informações de html da página. Observar, pois podem precisar 
de um observação para que não esteja pegando informações desnecessárias

no caso desta página:
- .tiltleColumn - Pega caisa com no0me e ano do filme
- .tiltleColumn a - nome do filme
- .secondaryInfo - ano do filme
- strong - nota da avaliação

Com essas informações, vamos interagir com o site, através de perguntas e repostas.

- response.css('.titleColumn').get()
    - get - pega a primeiro informação que encontrar com '.titleColumn'
    - getall - pega todas as informações da página com '.titleColumn'
    - css - arquivo com CSS com está marcação '.titleColumn'
    - html - arquivo com HTML com está marcação '.titleColumn'

dependendo do formato do arquivo de busca (css e html), pode trazer mais ou menos resultados.

E isso é retornado como uma lista de resultados. No caso o primeiro da lista. Se usar _.getall()_, trará todos da lista

Aqui já pode-se interagir com a lista, como exemplo:

- filmes = response.css('.titleColumn')
    - lens(todosfilmes)
    - filmes[15] - mostrando os primeiros 15 filmes 
    - e outros...

Usando:

- response.css('titleColumn a::text').getall()

Informará apenas o texto entre as tags. Neste ecaso, o titulo do filme.

Após todos os teste, obteção de dados, podemos escrevre o que foi útil para o PyCharm, e anotar dentro da função
que escrita pelo **Spiders**. Caso não tenha mais uso o Shell, para sair, use:<mark>quit()</mark>

## Rodando o projeto via termina Anaconda prompt

- scrapy crawl _nomedoprojeto_ ou _nomedoprojeto.py_ (no caso do exemplo: imdb)

Se tudo der certo, vai aparecer vários _200_ como repsosta.

como no exemplo: </br></br>


***


(filmesimdb) C:\Users\shaff\PycharmProjects\projetoimdb\imdb250>scrapy crawl imdb
2022-04-25 15:22:19 [scrapy.utils.log] INFO: Scrapy 2.6.1 started (bot: imdb250)
2022-04-25 15:22:19 [scrapy.utils.log] INFO: Versions: lxml 4.8.0.0, libxml2 2.9.12, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 22.4.0, Python 3.6.13 |Anaconda, Inc.| (default, Mar 16 2021, 11:37:27) [MSC v.1916 64 bit (AMD64)], pyOpenSSL 22.0.0 (OpenSSL 1.1.1n  15 Mar 2022), cryptography 36.0.2, Platform Windows-10-10.0.19041-SP0
2022-04-25 15:22:19 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'imdb250',
 'NEWSPIDER_MODULE': 'imdb250.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['imdb250.spiders']}
2022-04-25 15:22:19 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2022-04-25 15:22:19 [scrapy.extensions.telnet] INFO: Telnet Password: 4bb45d56336b6c59
2022-04-25 15:22:20 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2022-04-25 15:22:20 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2022-04-25 15:22:20 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2022-04-25 15:22:20 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2022-04-25 15:22:20 [scrapy.core.engine] INFO: Spider opened
2022-04-25 15:22:20 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2022-04-25 15:22:20 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2022-04-25 15:22:21 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.imdb.com/robots.txt> (referer: None)
2022-04-25 15:22:22 [filelock] DEBUG: Attempting to acquire lock 2418601407488 on C:\Users\shaff\anaconda3\envs\filmesimdb\lib\site-packages\tldextract\.suffix_cache/publicsuffix.org-tlds\de84b5ca2167d4c83e38fb162f2e8738.tldextract.json.lock
2022-04-25 15:22:22 [filelock] DEBUG: Lock 2418601407488 acquired on C:\Users\shaff\anaconda3\envs\filmesimdb\lib\site-packages\tldextract\.suffix_cache/publicsuffix.org-tlds\de84b5ca2167d4c83e38fb162f2e8738.tldextract.json.lock
2022-04-25 15:22:22 [filelock] DEBUG: Attempting to acquire lock 2418601891880 on C:\Users\shaff\anaconda3\envs\filmesimdb\lib\site-packages\tldextract\.suffix_cache/urls\62bf135d1c2f3d4db4228b9ecaf507a2.tldextract.json.lock
2022-04-25 15:22:22 [filelock] DEBUG: Lock 2418601891880 acquired on C:\Users\shaff\anaconda3\envs\filmesimdb\lib\site-packages\tldextract\.suffix_cache/urls\62bf135d1c2f3d4db4228b9ecaf507a2.tldextract.json.lock
2022-04-25 15:22:22 [filelock] DEBUG: Attempting to release lock 2418601891880 on C:\Users\shaff\anaconda3\envs\filmesimdb\lib\site-packages\tldextract\.suffix_cache/urls\62bf135d1c2f3d4db4228b9ecaf507a2.tldextract.json.lock
2022-04-25 15:22:22 [filelock] DEBUG: Lock 2418601891880 released on C:\Users\shaff\anaconda3\envs\filmesimdb\lib\site-packages\tldextract\.suffix_cache/urls\62bf135d1c2f3d4db4228b9ecaf507a2.tldextract.json.lock
2022-04-25 15:22:22 [filelock] DEBUG: Attempting to release lock 2418601407488 on C:\Users\shaff\anaconda3\envs\filmesimdb\lib\site-packages\tldextract\.suffix_cache/publicsuffix.org-tlds\de84b5ca2167d4c83e38fb162f2e8738.tldextract.json.lock
2022-04-25 15:22:22 [filelock] DEBUG: Lock 2418601407488 released on C:\Users\shaff\anaconda3\envs\filmesimdb\lib\site-packages\tldextract\.suffix_cache/publicsuffix.org-tlds\de84b5ca2167d4c83e38fb162f2e8738.tldextract.json.lock
2022-04-25 15:22:22 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.imdb.com/chart/top/?ref_=nv_mv_250> (referer: None)
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Shawshank Redemption', 'lancamento': '(1994)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Godfather', 'lancamento': '(1972)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Dark Knight', 'lancamento': '(2008)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Godfather: Part II', 'lancamento': '(1974)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': '12 Angry Men', 'lancamento': '(1957)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': "Schindler's List", 'lancamento': '(1993)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Lord of the Rings: The Return of the King', 'lancamento': '(2003)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Pulp Fiction', 'lancamento': '(1994)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Lord of the Rings: The Fellowship of the Ring', 'lancamento': '(2001)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Good, the Bad and the Ugly', 'lancamento': '(1966)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Forrest Gump', 'lancamento': '(1994)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Fight Club', 'lancamento': '(1999)', 'nota': '9.2'}
2022-04-25 15:22:22 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Inception', 'lancamento': '(2010)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Lord of the Rings: The Two Towers', 'lancamento': '(2002)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Star Wars: Episode V - The Empire Strikes Back', 'lancamento': '(1980)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Matrix', 'lancamento': '(1999)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Goodfellas', 'lancamento': '(1990)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': "One Flew Over the Cuckoo's Nest", 'lancamento': '(1975)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Se7en', 'lancamento': '(1995)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Seven Samurai', 'lancamento': '(1954)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': "It's a Wonderful Life", 'lancamento': '(1946)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Silence of the Lambs', 'lancamento': '(1991)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'City of God', 'lancamento': '(2002)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Saving Private Ryan', 'lancamento': '(1998)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Life Is Beautiful', 'lancamento': '(1997)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Green Mile', 'lancamento': '(1999)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Star Wars', 'lancamento': '(1977)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Interstellar', 'lancamento': '(2014)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Terminator 2: Judgment Day', 'lancamento': '(1991)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Back to the Future', 'lancamento': '(1985)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Spirited Away', 'lancamento': '(2001)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Psycho', 'lancamento': '(1960)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Pianist', 'lancamento': '(2002)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Léon: The Professional', 'lancamento': '(1994)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Parasite', 'lancamento': '(2019)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Lion King', 'lancamento': '(1994)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'American History X', 'lancamento': '(1998)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Gladiator', 'lancamento': '(2000)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Usual Suspects', 'lancamento': '(1995)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Departed', 'lancamento': '(2006)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Prestige', 'lancamento': '(2006)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Casablanca', 'lancamento': '(1942)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Whiplash', 'lancamento': '(2014)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Intouchables', 'lancamento': '(2011)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Modern Times', 'lancamento': '(1936)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Once Upon a Time in the West', 'lancamento': '(1968)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Hara-Kiri', 'lancamento': '(1962)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Grave of the Fireflies', 'lancamento': '(1988)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Rear Window', 'lancamento': '(1954)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Alien', 'lancamento': '(1979)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'City Lights', 'lancamento': '(1931)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Cinema Paradiso', 'lancamento': '(1988)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Memento', 'lancamento': '(2000)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Apocalypse Now', 'lancamento': '(1979)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Indiana Jones and the Raiders of the Lost Ark', 'lancamento': '(1981)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Django Unchained', 'lancamento': '(2012)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'WALL·E', 'lancamento': '(2008)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Lives of Others', 'lancamento': '(2006)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Sunset Blvd.', 'lancamento': '(1950)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Paths of Glory', 'lancamento': '(1957)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Shining', 'lancamento': '(1980)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Great Dictator', 'lancamento': '(1940)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Witness for the Prosecution', 'lancamento': '(1957)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Avengers: Infinity War', 'lancamento': '(2018)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Aliens', 'lancamento': '(1986)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'American Beauty', 'lancamento': '(1999)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb', 'lancamento': '(1964)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Dark Knight Rises', 'lancamento': '(2012)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Spider-Man: Into the Spider-Verse', 'lancamento': '(2018)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Joker', 'lancamento': '(2019)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Oldboy', 'lancamento': '(2003)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Braveheart', 'lancamento': '(1995)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Amadeus', 'lancamento': '(1984)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Toy Story', 'lancamento': '(1995)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Boat', 'lancamento': '(1981)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Coco', 'lancamento': '(2017)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Inglourious Basterds', 'lancamento': '(2009)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Princess Mononoke', 'lancamento': '(1997)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Once Upon a Time in America', 'lancamento': '(1984)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Avengers: Endgame', 'lancamento': '(2019)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Good Will Hunting', 'lancamento': '(1997)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Requiem for a Dream', 'lancamento': '(2000)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Toy Story 3', 'lancamento': '(2010)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': "Singin' in the Rain", 'lancamento': '(1952)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Your Name.', 'lancamento': '(2016)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Star Wars: Episode VI - Return of the Jedi', 'lancamento': '(1983)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': '3 Idiots', 'lancamento': '(2009)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': '2001: A Space Odyssey', 'lancamento': '(1968)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Reservoir Dogs', 'lancamento': '(1992)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Eternal Sunshine of the Spotless Mind', 'lancamento': '(2004)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'High and Low', 'lancamento': '(1963)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Citizen Kane', 'lancamento': '(1941)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Spider-Man: No Way Home', 'lancamento': '(2021)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Capernaum', 'lancamento': '(2018)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Lawrence of Arabia', 'lancamento': '(1962)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'M', 'lancamento': '(1931)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'North by Northwest', 'lancamento': '(1959)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Hunt', 'lancamento': '(2012)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Vertigo', 'lancamento': '(1958)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Amélie', 'lancamento': '(2001)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'A Clockwork Orange', 'lancamento': '(1971)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Come and See', 'lancamento': '(1985)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Full Metal Jacket', 'lancamento': '(1987)', 'nota': '9.2'}
2022-04-25 15:22:23 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Double Indemnity', 'lancamento': '(1944)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Apartment', 'lancamento': '(1960)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Scarface', 'lancamento': '(1983)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Taxi Driver', 'lancamento': '(1976)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'To Kill a Mockingbird', 'lancamento': '(1962)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Sting', 'lancamento': '(1973)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Ikiru', 'lancamento': '(1952)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Hamilton', 'lancamento': '(2020)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'L.A. Confidential', 'lancamento': '(1997)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Up', 'lancamento': '(2009)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Heat', 'lancamento': '(1995)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Metropolis', 'lancamento': '(1927)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Snatch', 'lancamento': '(2000)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'A Separation', 'lancamento': '(2011)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Die Hard', 'lancamento': '(1988)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Indiana Jones and the Last Crusade', 'lancamento': '(1989)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Incendies', 'lancamento': '(2010)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Bicycle Thieves', 'lancamento': '(1948)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': '1917', 'lancamento': '(2019)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Like Stars on Earth', 'lancamento': '(2007)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Downfall', 'lancamento': '(2004)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'For a Few Dollars More', 'lancamento': '(1965)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Batman Begins', 'lancamento': '(2005)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Dangal', 'lancamento': '(2016)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Kid', 'lancamento': '(1921)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Some Like It Hot', 'lancamento': '(1959)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Father', 'lancamento': '(2020)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'All About Eve', 'lancamento': '(1950)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Green Book', 'lancamento': '(2018)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Wolf of Wall Street', 'lancamento': '(2013)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Judgment at Nuremberg', 'lancamento': '(1961)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Unforgiven', 'lancamento': '(1992)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': "Pan's Labyrinth", 'lancamento': '(2006)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Casino', 'lancamento': '(1995)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Ran', 'lancamento': '(1985)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Monty Python and the Holy Grail', 'lancamento': '(1975)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'There Will Be Blood', 'lancamento': '(2007)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'A Beautiful Mind', 'lancamento': '(2001)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Sixth Sense', 'lancamento': '(1999)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Truman Show', 'lancamento': '(1998)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Yojimbo', 'lancamento': '(1961)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Treasure of the Sierra Madre', 'lancamento': '(1948)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Rashomon', 'lancamento': '(1950)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Great Escape', 'lancamento': '(1963)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Shutter Island', 'lancamento': '(2010)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Kill Bill: Vol. 1', 'lancamento': '(2003)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Jurassic Park', 'lancamento': '(1993)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'No Country for Old Men', 'lancamento': '(2007)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Elephant Man', 'lancamento': '(1980)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Finding Nemo', 'lancamento': '(2003)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Raging Bull', 'lancamento': '(1980)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Chinatown', 'lancamento': '(1974)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Gone with the Wind', 'lancamento': '(1939)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'V for Vendetta', 'lancamento': '(2005)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Inside Out', 'lancamento': '(2015)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Lock, Stock and Two Smoking Barrels', 'lancamento': '(1998)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Thing', 'lancamento': '(1982)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Dial M for Murder', 'lancamento': '(1954)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Secret in Their Eyes', 'lancamento': '(2009)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Bridge on the River Kwai', 'lancamento': '(1957)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': "Howl's Moving Castle", 'lancamento': '(2004)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Trainspotting', 'lancamento': '(1996)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Three Billboards Outside Ebbing, Missouri', 'lancamento': '(2017)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Gran Torino', 'lancamento': '(2008)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Warrior', 'lancamento': '(2011)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Fargo', 'lancamento': '(1996)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'My Neighbor Totoro', 'lancamento': '(1988)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Prisoners', 'lancamento': '(2013)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Million Dollar Baby', 'lancamento': '(2004)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Gold Rush', 'lancamento': '(1925)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Blade Runner', 'lancamento': '(1982)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'On the Waterfront', 'lancamento': '(1954)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Catch Me If You Can', 'lancamento': '(2002)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Third Man', 'lancamento': '(1949)', 'nota': '9.2'}
2022-04-25 15:22:24 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Children of Heaven', 'lancamento': '(1997)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Ben-Hur', 'lancamento': '(1959)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The General', 'lancamento': '(1926)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': '12 Years a Slave', 'lancamento': '(2013)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Wild Strawberries', 'lancamento': '(1957)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Gone Girl', 'lancamento': '(2014)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Deer Hunter', 'lancamento': '(1978)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Before Sunrise', 'lancamento': '(1995)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'In the Name of the Father', 'lancamento': '(1993)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Harry Potter and the Deathly Hallows: Part 2', 'lancamento': '(2011)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Mr. Smith Goes to Washington', 'lancamento': '(1939)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Grand Budapest Hotel', 'lancamento': '(2014)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Wages of Fear', 'lancamento': '(1953)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Sherlock Jr.', 'lancamento': '(1924)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Room', 'lancamento': '(2015)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Barry Lyndon', 'lancamento': '(1975)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Memories of Murder', 'lancamento': '(2003)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Seventh Seal', 'lancamento': '(1957)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Hacksaw Ridge', 'lancamento': '(2016)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Klaus', 'lancamento': '(2019)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Wild Tales', 'lancamento': '(2014)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Big Lebowski', 'lancamento': '(1998)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'How to Train Your Dragon', 'lancamento': '(2010)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Mad Max: Fury Road', 'lancamento': '(2015)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Pather Panchali', 'lancamento': '(1955)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Mary and Max', 'lancamento': '(2009)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Jaws', 'lancamento': '(1975)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Passion of Joan of Arc', 'lancamento': '(1928)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Monsters, Inc.', 'lancamento': '(2001)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Hotel Rwanda', 'lancamento': '(2004)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Tokyo Story', 'lancamento': '(1953)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Dead Poets Society', 'lancamento': '(1989)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Platoon', 'lancamento': '(1986)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Rocky', 'lancamento': '(1976)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Ford v Ferrari', 'lancamento': '(2019)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Stand by Me', 'lancamento': '(1986)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Terminator', 'lancamento': '(1984)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Rush', 'lancamento': '(2013)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Spotlight', 'lancamento': '(2015)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Into the Wild', 'lancamento': '(2007)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Network', 'lancamento': '(1976)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Wizard of Oz', 'lancamento': '(1939)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Logan', 'lancamento': '(2017)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Groundhog Day', 'lancamento': '(1993)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Ratatouille', 'lancamento': '(2007)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Exorcist', 'lancamento': '(1973)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Before Sunset', 'lancamento': '(2004)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Best Years of Our Lives', 'lancamento': '(1946)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Incredibles', 'lancamento': '(2004)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Battle of Algiers', 'lancamento': '(1966)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Rebecca', 'lancamento': '(1940)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'To Be or Not to Be', 'lancamento': '(1942)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Grapes of Wrath', 'lancamento': '(1940)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Cool Hand Luke', 'lancamento': '(1967)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': "Hachi: A Dog's Tale", 'lancamento': '(2009)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Amores perros', 'lancamento': '(2000)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Dersu Uzala', 'lancamento': '(1975)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'My Father and My Son', 'lancamento': '(2005)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The 400 Blows', 'lancamento': '(1959)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Persona', 'lancamento': '(1966)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Life of Brian', 'lancamento': '(1979)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'La Haine', 'lancamento': '(1995)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Pirates of the Caribbean: The Curse of the Black Pearl', 'lancamento': '(2003)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'It Happened One Night', 'lancamento': '(1934)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Sound of Music', 'lancamento': '(1965)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Handmaiden', 'lancamento': '(2016)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Gandhi', 'lancamento': '(1982)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Aladdin', 'lancamento': '(1992)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Help', 'lancamento': '(2011)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Beauty and the Beast', 'lancamento': '(1991)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'The Batman', 'lancamento': '(2022)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Rififi', 'lancamento': '(1955)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.imdb.com/chart/top/?ref_=nv_mv_250>
{'titulos': 'Dances with Wolves', 'lancamento': '(1990)', 'nota': '9.2'}
2022-04-25 15:22:25 [scrapy.core.engine] INFO: Closing spider (finished)
2022-04-25 15:22:25 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 459,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 598247,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 2,
 'elapsed_time_seconds': 5.05084,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2022, 4, 25, 18, 22, 25, 978694),
 'item_scraped_count': 250,
 'log_count/DEBUG': 261,
 'log_count/INFO': 10,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2022, 4, 25, 18, 22, 20, 927854)}
2022-04-25 15:22:25 [scrapy.core.engine] INFO: Spider closed (finished)

***

## Exportando Dados via terminal Anaconda prompt

- scrapy crawl _nomedoarquivo_ _-o ou -O_ _nomedoarquivo_.json (ou outra extenção) </br></br>
**json:** Muito utilizada, por acessar informações de forma simples.</br>
**- o ( -ó menúsculo )** - significa que caso haja informação, ele não apaga e vai adicionando.</br>
**- O ( -Ó maiúsculo )** - significa que caso haja informação, ele apaga e reescreve.

Exemplo: 
- scrapy crawl imdb -O imdb.json
- scrapy crawl imdb -O imdb.csv

Arquivo é criado na pasta principal do projeto.