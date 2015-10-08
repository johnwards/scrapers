# -*- coding: utf-8 -*-

import scrapy

class AssetItem(scrapy.Item):
    url = scrapy.Field()
 
class InternalItem(scrapy.Item):
	url = scrapy.Field()

class ExternalItem(scrapy.Item):
	url = scrapy.Field()

