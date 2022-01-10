import scrapy

# scrapy
# sudo apt install python3-scrapy
# scrapy startproject name
# scrapy genspider newname www.name.com
# scrapy crawl newname

class QuotoSpider(scrapy.Spider):
    name = 'quote'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self,response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                '文章----------->' : quote.css('span.text::text').extract_first(), 
                '\n作者/n' : quote.xpath('./span/small/text()').extract_first(), 
            }
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield response.follow(next_page,self.parse)


#scrapy runspider ./xiaoxiaoran5/4-scrapy.py
#scrapy runspider ./xiaoxiaoran5/4-scrapy.py -o quotes.json


