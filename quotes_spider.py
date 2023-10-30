import os
import scrapy
os.chdir("C://Users//acer/Desktop/PY/Scrapping mio/scrapy")

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"]
    
    def parse(self,response):
        with open('rwesultados.html','w', encoding ='utf-8') as f:
            f.write(response.text)