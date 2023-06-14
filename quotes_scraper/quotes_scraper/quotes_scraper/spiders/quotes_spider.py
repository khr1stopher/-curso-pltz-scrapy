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
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json'
    }

    def parse(self, response, **kwargs):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        yield {
            "Title": title,
            "quotes": quotes,
            "top_ten_tags": top_ten_tags
        }

        next_btn = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_btn:
            yield response.follow(next_btn, callback=self.parse)