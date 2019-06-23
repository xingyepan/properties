# -*- coding: utf-8 -*-
import scrapy
import datetime
import socket
from scrapy.loader import ItemLoader
from properties.items import PropertiesItem

class HouseSpider(scrapy.Spider):
	name = 'house'
	allowed_domains = ["db"]
	start_urls = ['https://db.house.qq.com/cq_185751/']

	def parse(self, response):
		# 直接在日志中输出结果 方式：
    	#self.log("address:%s" %response.xpath('//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[1]/text()').extract())
		'''
    	#实例化 item 可以输出到指定的文件类型 中保存结果
		# item = PropertiesItem()
    	item['title']=response.xpath('//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/div[1]/h1/text()').extract()
		item['price']=response.xpath('//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/div[1]/h2/span/strong/text()').re('[.0-9]+')
		item['address']=response.xpath('//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[1]/text()').extract()
		return item
		'''
		#用处理器进行处理  更强大
		dl = ItemLoader(item = PropertiesItem(),response = response)
		# 用 css 选择器 进行提取数据
    	# 用ID属性进行定位
    	#dl.add_css('price','#baseinfo_top_layout strong::text')
    	#用 class 属性定位  等同于上面用ID定位
		dl.add_css('price','.price strong::text')

		#用 xpath 选择器  进行提取数据
		dl.add_xpath('title','//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/div[1]/h1/text()')
		#dl.add_xpath('price','//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/div[1]/h2/span/strong/text()')
		dl.add_xpath('address','//*[@id="baseinfo_top_layout"]/div[3]/div[2]/div/ul[2]/li[1]/text()')
		#add_value()  方法 获取python 计算获取的单个值  而不是xpath or css 表达式
		dl.add_value('url',response.url)
		dl.add_value('spider', self.name)
		dl.add_value('server', socket.gethostname())
		dl.add_value('h_date', datetime.datetime.now())
		#item =  dl.load_item()
		print(dl.load_item())
		yield dl.load_item()


