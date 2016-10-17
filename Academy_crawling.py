
# coding: utf-8

# In[2]:

import lxml.html
from lxml.cssselect import CSSSelector
import requests


# In[3]:

d = requests.get('https://www.ieee.org/conferences_events/index.html')


# In[4]:

html = lxml.html.fromstring(d.text)


# In[5]:

print lxml.html.tostring(html)


# In[6]:

sel=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div:nth-child(2)')
nodes = sel(html)
for node in nodes:
    print lxml.html.tostring(node)


# In[7]:

sel=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div a')
nodes = sel(html)
print nodes


# In[8]:

for node in nodes:
  
    print node.text


# In[9]:

sel=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div p > br')

nodes = sel(html)
print nodes

for node in nodes:
    print lxml.html.tostring(node)
  


# In[10]:

sel=CSSSelector('div.box-c-indent p > a')
nodes = sel(html)
print len(nodes)
print nodes


# In[12]:

for node in nodes:
    if node is not None:
        print node.text_content()


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



