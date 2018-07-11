# -*- coding: utf-8 -*-
from scrapy import Selector
from scrapy import Spider
from wikiSpider.items import WikispiderItem

class ArticleSpider(Spider):
	name = "article"
	allowed_domains = ["zh.wikipedia.org"]
	start_urls = ["https://zh.wikipedia.org/wiki/%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4%E9%9B%86%E5%9B%A2",
	"https://zh.wikipedia.org/wiki/%E8%94%A1%E5%B4%87%E4%BF%A1"]

	def parse(self,response):
		item = WikispiderItem()
		title = response.xpath('//h1/text()')[0].extract()
		print("Title is: "+title)
		item['title'] = title
		# item.title = title
		return item
		