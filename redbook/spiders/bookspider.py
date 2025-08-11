#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: book_spider.py
Author: cc
Created: 2025-08-11 11:22
Last Modified: 2025-08-11 11:22
Description: Scrapy spider for crawling TongDaXin Red Book documents
"""


import scrapy
from urllib.parse import urljoin


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["www.tdx.com.cn"]
    start_urls = ["https://www.tdx.com.cn/products/user_redbook_style2.html"]

    def parse(self, response):
        # Extract all document rows
        for row in response.xpath('//tr[td[1][.//a]]'):
            # Skip header and empty rows
            if not row.xpath('.//a[contains(@href, "userdoc/")]'):
                continue

            yield {
                'title': row.xpath('.//a/text()').get().strip(),
                'url': urljoin(response.url, row.xpath('.//a/@href').get()),
                'publish_date': row.xpath('.//td[2]//text()').get().strip(),
                'file_type': row.xpath('.//img/@src').get().split('/')[-1].split('_')[0]
            }
