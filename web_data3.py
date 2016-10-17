
# coding: utf-8

# In[3]:

import os


# In[7]:

os.chdir('C:\\Users\k-chun')


# In[9]:

get_ipython().run_cell_magic(u'writefile', u'ds_web_data_paging.py', u'import scrapy\n\n\nclass QuotesSpider(scrapy.Spider):\n    name = "quotes"\n    start_urls = [\n        \'http://quotes.toscrape.com/page/1/\',\n    ]\n\n    def parse(self, response):\n        for quote in response.css(\'div.quote\'):\n            yield {\n                \'text\': quote.css(\'span.text::text\').extract_first(),\n                \'author\': quote.css(\'span small::text\').extract_first(),\n                \'tags\': quote.css(\'div.tags a.tag::text\').extract(),\n            }\n\n        next_page = response.css(\'li.next a::attr(href)\').extract_first()\n        if next_page is not None:\n            next_page = response.urljoin(next_page)\n            yield scrapy.Request(next_page, callback=self.parse)')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



