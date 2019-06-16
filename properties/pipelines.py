# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  pymysql

class PropertiesPipeline(object):
	def process_item(self, item, spider):
		return item
'''
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
		sql = 'insert into house_tx (address,h_date,price,server,spider,title,url) values (%s,%s,%s,%s,%s,%s,%s)'
		self.cursor.execute(sql,(item['address'],item['h_date'],item['price'],item['server'],item['spider'],item['title'],item['url']))
		self.db.commit()
		return item
	def colse_spider(self,spider):
		self.db.close()
'''
#Manual's Pipeline
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
		print('爬虫开启')
		self.db = pymysql.connect(host=self.host, database=self.database, user=self.user, password=self.password, port=self.port, charset='utf8')
		self.cursor = self.db.cursor()

	def process_item(self,item,spider):
		sql = "insert into house_list_cq (house_name,price,tell_num,address,open_date,check_in_date,property_type,period,Build_category,Open_hair,proper_mana_comp,Thing_industry_fee,product_rate,green_rate,households_num,decoration_situ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		self.cursor.execute(sql,(item['house_name'],item['price'],item['tell_num'],item['address'],item['open_date'],item['check_in_date'],item['property_type'],
								 item['period'],item['Build_category'],item['Open_hair'],item['proper_mana_comp'],item['Thing_industry_fee'],item['product_rate'],
								 item['green_rate'],item['households_num'], item['decoration_situ'])
							)
		self.db.commit()
		return item
	def colse_spider(self,spider):
		self.db.close()
