# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class weatherPipeline:
    def process_item(self, item, spider):
        with open('weather.txt', 'a', encoding='utf8') as fp:
            fp.write(item['city']+'\n')
            print(item["city"])
            fp.write(item['weather']+'\n\n')        
            print(item["weather"])
        return item
        
        
