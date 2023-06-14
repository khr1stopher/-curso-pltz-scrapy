import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # TITLE = '//h1/a/text()'
    # CITAS = '//span[@class="text" and @itemprop="text"]/text()'
    # TOP_TEN_TAGS = '//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()'
    # NEXT_PAGE_BTN = '//ul[@class="pager"]/li[@class="next"]/a/@href'

    start_urls = [
        'http://quotes.toscrape.com'
    ]

    custom_settings = {
            'FEEDS': {
                'quotes.json': {
                    'format': 'json',
                    'encoding': 'utf8',
                    'store_empty': False,
                    'fields': None,
                    'indent': 4,
                    'item_export_kwargs': {
                        'export_empty_fields': True,
                    },
                },
            },
            'CONCURRENT_REQUETS': 24,
            'MEMUSAGE_LIMIT_MB': 2048,
            'MEMUSAGE_NOTIFY_MAIL': [
                'kkromans009@gmail.com'
            ],
            'ROBOTSTXT_OBEY': True,
            'USER_AGENT': 'Khristopher',
            'FEED_EXPORT_ENCODING': 'utf-8'
        }
    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())

        
        next_btn = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_btn:
            yield response.follow(next_btn, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
        else:
            yield {
                'quotes': quotes
            }

    def parse(self, response, **kwargs):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()

        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            top_tags = top_tags[:top]

        yield {
            "Title": title,
            "top_tags": top_tags
        }

        next_btn = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_btn:
            yield response.follow(next_btn, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})