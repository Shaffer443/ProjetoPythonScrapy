import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'                                                               # Nome do arquivo, dado por mim
    #allowed_domains = ['imdb.com']                                             # pega de todos os dominios que tenha, caso o site seja mundial e etc
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']             # link da página dos dados

    def parse(self, response):

        for filmes in response.css('.titleColumn'):                             # trazendo informações do site
            yield {

                    'titulos': filmes.css('.titleColumn a::text').get(),             # mostra apena o titulo dos filmes
                    'lancamento': filmes.css('.secondaryInfo::text').get()[1:-1],     # Lançamento dos filmes (ano de lançamento)
                    'nota': response.css('strong::text').get()                        # nota do site para os filmes. As valiações pelos usuários)
            }

        #pass

                                                                                # .text, pode ser manipulado como uma string