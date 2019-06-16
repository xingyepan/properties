# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from properties.items import PropertiesItem1
from scrapy.http import Request
from urllib import parse

class ManualSpider(scrapy.Spider):
	name = "manual"
	allowed_domains = ["db"]
	start_urls = ['https://db.house.qq.com/index.php?mod=search&city=cq#LXNob3d0eXBlXzEtcGFnZV80']

	def parse(self, response):
		#Get the next index URLs and yield Requests
		li_list = response.xpath('//*[@id="search_result_list"]//li[@class="address"]/a/@href').extract()
		for li in li_list:
			Request(li)
		#用处理器进行处理  更强大
		dl = ItemLoader(item = PropertiesItem1(),response = response)
		dl.add_xpath('h_name','//*[@id="baseinfo_top_layout"]/div[1]/div[1]/div[1]/h2/text()')
		dl.add_xpath('price','//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/div[1]/h2/span/text()')
		dl.add_xpath('tell_num', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/div[2]/i/text()')
		dl.add_xpath('address', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[1]/text()')
		dl.add_xpath('open_date', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[2]/text()')
		dl.add_xpath('check_in_date', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[3]/text()')
		dl.add_xpath('property_type', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[4]/text()')
		dl.add_xpath('period', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[5]/text()')
		dl.add_xpath('Build_category', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[7]/text()')
		dl.add_xpath('Open_hair', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[9]/text()')
		dl.add_xpath('proper_mana_comp', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[12]/text()')
		dl.add_xpath('Thing_industry_fee', '//*[@id="xxIntr"]/ul[1]/li[12]/p/text()')
		dl.add_xpath('product_rate', '//*[@id="xxIntr"]/ul[1]/li[14]/p/text()')
		dl.add_xpath('green_rate', '//*[@id="xxIntr"]/ul[1]/li[13]/p/text()')
		dl.add_xpath('households_num', '//*[@id="xxIntr"]/ul[1]/li[10]/p/text()')
		dl.add_xpath('decoration_situ', '//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[6]/text()')
		# 用 css 选择器 进行提取数据
		# 用ID属性进行定位
		#dl.add_css('price','#baseinfo_top_layout strong::text')

		#用 xpath 选择器  进行提取数据
		#dl.add_xpath('price','//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/div[1]/h2/span/strong/text()')

		#add_value()  方法 获取python 计算获取的单个值  而不是xpath or css 表达式
		#dl.add_value('url',response.url)
		yield dl.load_item()
