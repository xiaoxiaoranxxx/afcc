import scrapy
import re
import json
from scrapy import Request

def strip(s):
    if s:
        return s.strip()
    return ''


class DiscoverySpider(scrapy.Spider):
    name = 'discover'
    allowed_domains = ['xinpianchang.com', 'https://openapi-vtom.vmovier.com']
    start_urls = [
        'https://www.xinpianchang.com/channel/index/id-1/sort-like?from=tabArticle']

    def parse(self, response):
        pid_list = response.xpath(
            '//ul[@class="video-list"]/li/@data-articleid').extract()
        url = 'https://www.xinpianchang.com/a%s?from=ArticleList'
        for pid in pid_list:
            #print(url % pid)
            yield response.follow(url % pid, self.parse_post)
        pages = response.xpath('//div[@class="page"]/a/@href').extract()
        for page in pages:
            yield response.follow(page,self.parse)

    def parse_post(self, response):
        post = {}
        post['title'] = response.xpath(
            '//div[@class="title-wrap"]/h3/text()').get()
        post['video'] = response.xpath('//*[@id="xpcplayer"]/div/div[2]/video/@src').get()
        cates = response.xpath('//span[contains(@class,"cate v-center")]/a/text()').extract()
        post['category'] = ''.join([cate.strip() for cate in cates])
        post['created_at'] = response.xpath('//span[contains(@class,"update-time v-center")]/i/text()').get()
        post['play-counts'] = response.xpath('//i[contains(@class,"play-counts")]/@data-curplaycounts').get()
        post['like_counts'] = response.xpath('//span[contains(@class,"like-counts")]/text()').get()
        post['desc'] = response.xpath('//p[contains(@class,"desc")]/text()').get().strip()

        # vid = re.findall('vid:' , response.text)
        # video_url = 'https://openapi-vtom.vmovier.com/v3/video/%s?expand=resource'
        # request = Request(video_url % vid, callback=self.parse_video)
        # request.meta['post'] = post
    #     yield request

    # def parse_video(self, response):
    #     post = response.meta['post']
    #     result = json.loads(response.text)
    #     post['video'] = result['data']['resource']['default']['url']
        yield post



