
# coding: utf-8

# ## 코스피 지수 크롤링 하기

# In[11]:

import urllib


# In[12]:

cospi = urllib.urlopen('https://www.google.com/finance/historical?q=KRX%3AKOSPI200&hl=en&ei=nt77V7nqDsyJ0gSZ6r-QCQ')


# In[13]:

_html = cospi.read()


# In[14]:

type(_html)


# In[15]:

print len(_html)


# In[16]:

from lxml import etree


# In[17]:

_htmlTree = etree.HTML(_html)


# In[18]:

type(_htmlTree)


# In[19]:

result = etree.tostring(_htmlTree, pretty_print=True, method="html")


# In[20]:

print len(result)


# In[21]:

nodes1 = _htmlTree.xpath('//*[@class="lm"]/text()')


# In[22]:

nodes2 = _htmlTree.xpath('//*[@class="rgt"]/text()')


# In[23]:

nodes3 = _htmlTree.xpath('//*[@class="rgt rm"]/text()')


# In[24]:

str1 = _htmlTree.xpath('//*[@class="bb lm lft"]/text()')


# In[25]:


str2 = _htmlTree.xpath('//*[@class="rgt bb"]/text()')


# In[26]:

str3 = _htmlTree.xpath('//*[@class="rgt bb rm"]/text()')


# In[27]:


print len(str1)


# In[28]:

print len(nodes3)


# In[29]:

print len(nodes1)


# In[30]:

print len(nodes2)


# In[36]:

for y in range(1):
    m = 4*y
    print str1[y].strip(), str2[m].strip(), str2[m+1].strip(), str2[m+2].strip(), str2[m+3].strip(), str3[y]
for i in range(20):
    n =4*i
    print nodes1[i].strip(), nodes2[n].strip(), nodes2[n+1].strip(), nodes2[n+2].strip(), nodes2[n+3].strip(), nodes3[i]


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




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



