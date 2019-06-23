# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
from scrapy.item import Item,Field

class PropertiesItem(Item):
	# define the fields for your item here like:
	# name = scrapy.Field()

	#Primary fileds
	address = Field()
	price = Field()
	title = Field()
	description = Field()
	image_urls = Field()

	#Calculated fields
	images = Field()
	location = Field()

	#Housekeeping fields
	url = Field()
	project = Field()
	spider =Field()
	server = Field()
	h_date = Field()


class PropertiesItem1(Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	house_name = Field()
	price = Field()
	tell_num = Field()
	address = Field()
	open_date = Field()
	check_in_date = Field()
	property_type = Field()
	period = Field()
	Build_category = Field()
	Open_hair = Field()
	proper_mana_comp = Field()
	Thing_industry_fee = Field()
	product_rate = Field()
	green_rate = Field()
	households_num = Field()
	decoration_situ = Field()
	url = Field()




