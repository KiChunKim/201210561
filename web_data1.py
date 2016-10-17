
# coding: utf-8

# In[1]:

import urllib


# In[2]:

response = urllib.urlopen('http://python.org/')


# In[3]:

response


# In[4]:

_html=response.read()


# In[5]:

import re


# In[6]:

p=re.compile('href="(http://.*?)"')


# In[7]:

res=p.findall(_html)


# In[8]:

for item in res:
    print item


# In[9]:

from lxml import etree


# In[10]:

_htmlTree = etree.HTML(_html)


# In[11]:

_htmlTree


# In[12]:

nodes = _htmlTree.xpath('//a[@href]')


# In[13]:

for node in nodes:
    print node.attrib


# In[14]:

from lxml.cssselect import CSSSelector


# In[15]:

sel=CSSSelector('p[href]')


# In[16]:

import lxml.html


# In[17]:

html= lxml.html.fromstring(_html)


# In[18]:

results=sel(html)


# In[19]:

for item in results:
    print item.get('href'), item.text


# In[24]:

sel=CSSSelector('body a')


# In[25]:

resu=sel(html)


# In[26]:

print len(resu)


# In[28]:

for item in resu:
    print item.text


# In[ ]:



