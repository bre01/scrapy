import scrapy
from re import findall
from urllib.request import urlopen
from ..items import WeatherItem
#from .. import itmes

#WeatherItem=items.WeatherItem;
class EverycitySpider(scrapy.Spider):
    name = "everyCity"
    allowed_domains = ["weather.com.cn"]
    #start_urls = ["http://weather.com.cn/"]
    start_urls = [];
    url=r"http://www.weather.com.cn/yunnan/index.shtml"
    with urlopen(url) as fp:
        contents=fp.read().decode()
        
    pattern='<a title=".*?" href="(.+?)" target="_blank">(.+?)</a>'
    for url in findall(pattern,contents):
        start_urls.append(url[0])
        

    def parse(self, response):
        item = WeatherItem()
        #print(response.xpath('//div[@class="crumbs fl"]//a[3]//text()').extract())
        city = response.xpath('//div[@class="crumbs fl"]//a[3]//text()').extract()[0]
        item['city'] = city
        selector = response.xpath('//ul[@class="t clearfix"]')[0]
        weather = ''
        for li in selector.xpath('./li'):
            date = li.xpath('./h1//text()').extract()[0]
            cloud = li.xpath('./p[@title]//text()').extract()[0]
            if len(li.xpath('./p[@class="tem"]//span//text()').extract())!=0 :
                high = li.xpath('./p[@class="tem"]//span//text()').extract()[0]
                low = li.xpath('./p[@class="tem"]//i//text()').extract()[0]
                wind = li.xpath('./p[@class="win"]//em//span[1]/@title').extract()[0] 
                wind = wind + li.xpath('./p[@class="win"]//i//text()').extract()[0]
                weather = weather + date+':'+cloud+','+high+r'/'+low+','+wind+'\n'
            else: 
            #high = li.xpath('./p[@class="tem"]//span//text()').extract()[0]
                temp = li.xpath('./p[@class="tem"]//i//text()').extract()[0]
                wind = li.xpath('./p[@class="win"]//em//span[1]/@title').extract()[0] 
                wind = wind + li.xpath('./p[@class="win"]//i//text()').extract()[0]
                weather = weather + date+':'+cloud+','+"now:"+temp+','+wind+'\n'
        item['weather'] = weather
        return [item]   
