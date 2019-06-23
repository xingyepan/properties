# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  pymysql
from properties.items import PropertiesItem
from properties.items import PropertiesItem1

class PropertiesPipeline(object):
	def process_item(self, item, spider):
		return item

class HousePipeline(object):
	def __init__(self, host, database, user, password, port):
		self.host = host
		self.database = database
		self.user = user
		self.password = password
		self.port = port
		self.db = None
		self.cursor = None


	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			host = crawler.settings.get('MYSQL_HOST'),
			database = crawler.settings.get('MYSQL_DATABASE'),
			user =  crawler.settings.get('MYSQL_USER'),
			password = crawler.settings.get('MYSQL_PASS'),
			port = crawler.settings.get('MYSQL_PORT')
		)
	def open_spider(self,spider):
		print('爬虫开启')
		self.db = pymysql.connect(host=self.host, database=self.database, user=self.user, password=self.password, port=self.port, charset='utf8')
		self.cursor = self.db.cursor()

	def process_item(self,item,spider):
		#if spider.name == 'house':
		if isinstance(item,PropertiesItem):
			print('show the house data')
			sql = 'insert into house_tx (address,h_date,price,server,spider,title,url) values (%s,%s,%s,%s,%s,%s,%s)'
			self.cursor.execute(sql,(item['address'],item['h_date'],item['price'],item['server'],item['spider'],item['title'],item['url']))
			self.db.commit()
			return item
	def colse_spider(self,spider):
		self.db.close()



class ManualPipeline(object):
	def __init__(self, host, database, user, password, port):
		self.host = host
		self.database = database
		self.user = user
		self.password = password
		self.port = port
		self.db = None
		self.cursor = None


	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			host = crawler.settings.get('MYSQL_HOST'),
			database = crawler.settings.get('MYSQL_DATABASE'),
			user =  crawler.settings.get('MYSQL_USER'),
			password = crawler.settings.get('MYSQL_PASS'),
			port = crawler.settings.get('MYSQL_PORT')
		)
	def open_spider(self,spider):
		print('爬虫开启_B')
		self.db = pymysql.connect(host=self.host, database=self.database, user=self.user, password=self.password, port=self.port, charset='utf8')
		self.cursor = self.db.cursor()

	def process_item(self,item,spider):
		#if spider.name == 'manual':
		if isinstance(item, PropertiesItem1):
			print('the item is  like this{}'.format(item))
			sql = 'insert into house_list_cq(url) values (%s)'
			self.cursor.execute(sql,(item['url']))
			print('test if i got here ')
			self.db.commit()
			return item

	def colse_spider(self,spider):
		self.db.close()
