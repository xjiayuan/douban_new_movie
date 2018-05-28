# -*- coding:utf-8 -*-

from scrapy.spiders import Spider
from douban_new_movie.items import DoubanNewMovieItem

class DoubanNewMovieSpider(Spider):
    name = "douban_new_movie_spider"
    start_urls = ['http://movie.douban.com/chart']
    allowed_domains = ["www.movie.douban.com"]
    
    def parse(self, response):
        
        movie_name = response.xpath("//div[@class='pl2']/a/text()").extract()
        movie_url = response.xpath("//div[@class='pl2']/a/@href").extract()
        movie_star = response.xpath("//div[@class='pl2']/div/span[@class='rating_nums']/text()").extract()
        
        item = DoubanNewMovieItem()
        
        item['movie_name'] = [n.encode('utf-8') for n in movie_name]
        item['movie_star'] = [n for n in movie_star]
        item['movie_url'] = [n for n in movie_url]
        
        yield item
        
        print movie_name, movie_star, movie_url
