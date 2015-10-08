# -*- coding: utf-8 -*-
import json

from scraper.items import ExternalItem, InternalItem, AssetItem

class SitemapPipline(object):

  def __init__(self):
    self.assets = list()
    self.internal = list()
    self.external = list()

  def process_item(self, item, spider):
    if type(item) is ExternalItem:
      self.external.append(item["url"])
    elif type(item) is InternalItem:
      self.internal.append(item["url"])
    elif type(item) is AssetItem:
      self.assets.append(item["url"])
    return item

  def close_spider(self, spider):
    with open('external.json', 'w+') as external_file:
      external_file.write(json.dumps(self.external))
    with open('internal.json', 'w+') as internal_file:
      internal_file.write(json.dumps(self.internal))
    with open('assets.json', 'w+') as assets_file:
      assets_file.write(json.dumps(self.assets))
    