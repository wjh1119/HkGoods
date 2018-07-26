import scrapy
from hk.items import HkItem


class HkSpider(scrapy.Spider):
    name = "hk"
    allowed_domains = ["http://baojia.3hk.cn/301"]
    start_urls = [
        "http://baojia.3hk.cn/301",
    ]

    def parse(self, response):

        for sel in response.xpath('//table[@class="table1"]'):

            item = HkItem()
            item['a1title'] = sel.xpath(
                'tr[1]/td[@class="textleft"]/div/text()').extract()[0] if len(
                    sel.xpath('tr[1]/td[@class="textleft"]/div/text()')
                    .extract()) > 0 else ""
            item['a2link'] = sel.xpath(
                'tr[2]/td[@class="textleft"]/div/span[@class="red"]/text()'
            ).extract()[0] if len(
                sel.xpath(
                    'tr[2]/td[@class="textleft"]/div/span[@class="red"]/text()'
                ).extract()) > 0 else ""

            desc = sel.xpath('tr[3]/td[@class="textleft"]/div/text()').extract()
            if type(desc) == list:

                if len(desc) == 0:
                    desc = ""
                else:
                    desc = desc[0]
            item['a3desc'] = desc
            
            yield item

        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)