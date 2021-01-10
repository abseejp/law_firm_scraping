# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AttorneyItem(scrapy.Item):
    # define the fields for your item here like:
    attorney_name = scrapy.Field()
    
