
# coding: utf-8

# In[13]:

import urllib


# In[14]:

url='http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data'


# In[15]:

res=urllib2.urlopen(url)


# In[16]:

html=res.read()


# In[17]:

html


# In[18]:

lines=html.splitlines()


# In[19]:

lines


# In[20]:

data=[]


# In[21]:

for line in lines:
    data.append(line.split())


# In[22]:

for line in data:
    print line


# ## 한국 포털사이트 접속하여 노래 검색하기

# In[24]:

import urllib


# In[25]:

keyword='비오는'


# In[39]:

s = urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")


# In[40]:

data= s.read()


# In[42]:

data


# In[43]:

import re
p=re.compile('title=".*비.?오는.*"')
res=p.findall(data)
for item in res:
    print item


# In[30]:

import lxml.html
from lxml.cssselect import CSSSelector


# In[31]:

html = lxml.html.fromstring(mydata)


# In[33]:

sel = CSSSelector('#content > div:nth-child(4) > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack > table > tbody > tr:nth-child(2) > td.name > a._title.title')
##직접 못찾고 교재 나와 있는 링크로 복사해서 붙여넣기 했습니다


# In[34]:

results = sel(html)


# In[36]:

for item in results:
    print item.text_content()


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



