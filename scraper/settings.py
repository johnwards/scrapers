# -*- coding: utf-8 -*-

BOT_NAME = 'wo'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

LOG_LEVEL = 'INFO'


ITEM_PIPELINES = {
    'scraper.pipelines.SitemapPipline': 100,
}
