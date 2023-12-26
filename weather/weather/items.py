# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name=scrapy.Field();
    city=scrapy.Field();
    city=scrapy.Field(); 
    weather=scrapy.Field();
    pass
class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    weather=scrapy.Field(); 
    name=scrapy.Field();
    city=scrapy.Field();
    city=scrapy.Field(); 
    pass
