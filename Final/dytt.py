# -*- coding: utf-8 -*-
import re
from copy import deepcopy

import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from www_dytt8_net.items import WwwDytt8NetItem


class DyttSpider(scrapy.Spider):
    name = 'dytt'
    allowed_domains = ['www.dytt8.net', 'www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/dyzz/index.html']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r'.*/\d+/\d+\.html', deny=r".*game.*"), callback='parse', follow=True),
    #     Rule(LinkExtractor(restrict_xpaths=u'//a[text()="下一页"]'))
    # )
    def parse(self, response):

        lis = response.xpath('//*[@id="header"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/ul//table')
        for li in lis:
            href = li.xpath('./tr[2]/td[2]/b/a/@href').extract_first()
            href = 'https://www.ygdy8.net' + href
            yield scrapy.Request(url=deepcopy(href), callback=self.parse_item, dont_filter=True)


        next_href = response.xpath('//*[@class="co_content8"]/div[@class="x"]//a')[-2]

        if next_href:
            next_href = 'https://www.ygdy8.net/html/gndy/dyzz/' + next_href.xpath('./@href').extract_first()
            print(next_href)
            yield scrapy.Request(url=next_href, callback=self.parse)

    def parse_item(self, response):
        item = WwwDytt8NetItem()
        item['title'] = response.xpath('//div[@class="title_all"]/h1/font/text()').extract_first()
        item['publish_time'] = response.xpath('//div[@class="co_content8"]/ul/text()').extract_first().strip().replace(
            '发布时间：', '')
        imgs_xpath = response.xpath('//div[@id="Zoom"]//img')

        item['images'] = [i.xpath('./@src').extract_first() for i in imgs_xpath if i.xpath('./@src')]

        item['download_links'] = re.compile('<a href="(ftp://.*?)">').findall(response.text)

        item['contents'] = [i.strip().replace('\n', '').replace('\r', '') for i in
                            response.xpath('string(//div[@id="Zoom"])').extract()]
        #
        yield item
