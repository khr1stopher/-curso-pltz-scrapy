import scrapy

# links = '//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href'

class SpiderCIA(scrapy.Spider):
    name = 'cia'
    start_urls = [
        'https://www.cia.gov/readingroom/historical-collections'
    ]
    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    def parse(self, response, **kwargs):
        links_desclassified = response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()
        content = ''.join(response.xpath('//div[@class="field-item even"]/p[not(@class) and not(child::strong and child::i)]/text()').getall())

        for link in links_desclassified:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        content = ''.join(response.xpath('//div[@class="field-item even"]/p[not(@class) and not(child::strong and child::i)]/text()').getall())

        yield {
            'url': link,
            'title': title,
            'body': content
        }