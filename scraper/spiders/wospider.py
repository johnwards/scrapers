import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scraper.items import ExternalItem, InternalItem, AssetItem

class WoSpider(CrawlSpider):
  name = "wo"
  allowed_domains = ["www.whiteoctober.co.uk"]
  start_urls = ["http://www.whiteoctober.co.uk"]
  rules = (
    Rule(LinkExtractor(allow=()), callback="parse_item", follow=True),
  )

  def parse_item(self, response):
    internal_item = InternalItem()
    internal_item["url"] = response.url
    yield internal_item

    #Use the inbuilt LinkExtractor to find urls, filtering out internal urls
    extractor_external = LinkExtractor(deny_domains=self.allowed_domains)
    external_links = extractor_external.extract_links(response)
    for link in external_links:
      external_item = ExternalItem()
      external_item["url"] = link.url
      yield external_item

    for src in response.css("img::attr('src')"):
      asset_item = AssetItem()
      asset_item["url"] = response.urljoin(src.extract())
      yield asset_item

    for src in response.css("script::attr('src')"):
      asset_item = AssetItem()
      asset_item["url"] = response.urljoin(src.extract())
      yield asset_item

