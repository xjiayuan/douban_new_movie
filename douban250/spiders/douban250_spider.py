from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from douban250.items import Douban250Item

class DoubanSpider(CrawlSpider):
    name = "douban250_spider"
    allowed_domains = []
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    
    rules = (Rule(LinkExtractor(allow=r'https://movie\.douban\.com/top250\?start=\d+&filter='), callback='parse_item', follow=True),)
    
    def parse_item(self, response):
        for movie in response.xpath('//em'):
            item = Douban250Item()
            item['movie_name'] = movie.xpath('../../..//span[@class="title"][1]/text()').extract()
            item['star'] = movie.xpath('../../..//span[@class="rating_num"]/text()').extract()
            item['quote'] = movie.xpath('../../..//span[@class="inq"]/text()').extract() or ' '
            yield item
            
        """
        item = Douban250Item()
        movie_name = response.xpath('//span[@class="title"][1]/text()').extract()
        star = response.xpath('//span[@class="rating_num"]/text()').extract()
        quote = response.xpath('//span[@class="inq"]/text()').extract()
    
        item['movie_name'] = [n.encode('utf-8') for n in movie_name]
        item['star'] = [n.encode('utf-8') for n in star]
        item['quote'] = [n.encode('utf-8') for n in quote]
        
        yield item
        """
