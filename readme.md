1、创建项目和爬虫

scrapy startproject redbook
cd redbook/ && scrapy genspider bookspider https://www.tdx.com.cn/products/user_redbook_style2.html

2、修改默认配置
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"


3、修改爬虫中的parse解析页面和启动爬虫


```python
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


```

4、结果展示

![image-20250811112539767](C:\Users\025-1000\AppData\Roaming\Typora\typora-user-images\image-20250811112539767.png)