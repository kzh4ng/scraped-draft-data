import scrapy

from draft.items import DraftItem
from scrapy.utils.response import open_in_browser

class DraftSpider(scrapy.Spider):
    name = "draft"
    allowed_domains = ["www.thebaseballcube.com"]
    year = "2013"
    start_urls = [
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=1&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=2&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=3&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=4&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=5&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=6&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=7&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=8&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=9&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",
    "http://www.thebaseballcube.com/draft/research.asp?Y1="+ year +"&Y2="+ year +"&R=10&RS==&Ov=&Ovs=%3C=&T=&Player=&School=&Pos=&HL=&Region=&P=June-Reg&CT=&Bonus=0&Signed=&Active=&Source=&Bats=&Throws=&Sort=",

    ]
    


    def parse(self, response):
        for href in response.xpath('//table/tr/td[6]/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        batting = 0
        pitching = 0
        item = DraftItem()
        item['experience'] = 0
        item['name'] = response.xpath('//h1/text()').extract()
        for tr in response.xpath('//table/tr[@class="ncaaRow"][@id[starts-with(.,"non")]]'):
            batting = batting + 1

        for tr in response.xpath('//table/tr[@class="ncaaRow"][@id[starts-with(.,"ncaa")]]'):
            pitching = pitching + 1

        if batting > pitching:
            item['experience'] = batting
        else:
            item['experience'] = pitching
        yield item
