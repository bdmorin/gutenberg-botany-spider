import scrapy
from icecream import ic
ic.configureOutput(includeContext=True)

import logging
logging.basicConfig(level=logging.DEBUG)





class GutenbergBotanySpider(scrapy.Spider):
    name = "gutenberg-botany-spider"
    allowed_domains = ["www.gutenberg.org"]
    start_urls = ["https://www.gutenberg.org/ebooks/search/?query=botany&submit_search=Go%21"]
    
    
    def parse(self, response):
        # Loop over the page to get each book link and yield a Request to the link
        for book in response.css('li.booklink'):
            book_link = response.urljoin(book.css('a.link::attr(href)').get())
            yield scrapy.Request(book_link, callback=self.parse_book)
            
            
     # Pagination
        next_page = response.css('a[title="Go to the next page of results."]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_book1(self, response):
        #ic(response)
        #title = [title.replace('\r', '') for title in response.css('li.booklink a.link span.title::text').getall()]
        data = {}                            
        for tr in response.css("table.bibrec tr"):
            key = tr.css("th::text").get()
            value = ' '.join(tr.css("td ::text").getall()).strip() # Get all text content within the cell
            # Now you can have both 'key' and 'value'. You can choose how to yield them.
            if key is None: continue
            if key in data:
                if not isinstance(data[key], list):
                    data[key] = [data[key]]
                data[key].append(value)
            else:
                data[key] = value

        file_urls = response.urljoin(response.css('table.files td.unpadded.icon_save a[type="text/plain; charset=us-ascii"]::attr(href)').get())
        data['file_urls'] = [file_urls]

        ic(data)
        ic(len(data))
        yield data
        
    def parse_book(self, response):
        # Initialize all fields with None or ''
        data = {
            'Author': None,
            'Category': None,
            'Contents': None,
            'Copyright Status': None,
            'Credits': None,
            'Downloads': None,
            'EBook-No.': None,
            'Illustrator': None,
            'Language': None,
            'LoC Class': None,
            'LoC No.': None,
            'Original Publication': None,
            'Release Date': None,
            'Subject': None,
            'Title': None,
            'file_urls': None,
            'files': None,
        }

        # Update available fields with actual values from page
        for tr in response.css("table.bibrec tr"):
            key = tr.css("th::text").get()
            value = ' '.join(tr.css("td ::text").getall()).strip()
            if key and key in data:
                data[key] = value

        # Update file_urls
        file_urls = response.urljoin(response.css('table.files td.unpadded.icon_save a[type="text/plain; charset=us-ascii"]::attr(href)').get())
        data['file_urls'] = [file_urls]

        yield data

        
        pass