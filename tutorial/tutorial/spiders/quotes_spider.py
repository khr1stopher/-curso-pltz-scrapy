import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'Quotes'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response, **kwargs):
        with open('resultados.html', 'w', encoding='utf-8') as f:
            f.write(response.text)