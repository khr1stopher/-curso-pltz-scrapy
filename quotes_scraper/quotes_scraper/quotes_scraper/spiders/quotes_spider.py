import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # TITLE = '//h1/a/text()'
    # CITAS = '//span[@class="text" and @itemprop="text"]/text()'
    # TOP_TEN_TAGS = '//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()'

    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response, **kwargs):
        print('*' * 10)
        print('\n')

        title = response.xpath('//h1/a/text()').get()
        print(f'Titulo: {title}')

        print('*' * 10)
        print('\n')

        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        print('Citas: ')
        for quote in quotes:
            print(f' - {quote}')

        print('*' * 10)
        print('\n')

        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        print('Top Ten tags: ')

        for tags in top_ten_tags:
            print(f' - {tags}')

        print('*' * 10)