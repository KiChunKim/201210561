
# coding: utf-8

# In[1]:

import os 
KEY="697a486559636e3037304356486844" 
TYPE='json'
SERVICE = 'StationAdresTelno' 
START_INDEX='1'
END_INDEX='20'
LINE_NUM='2'


# In[2]:

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=LINE_NUM


# In[3]:

print url


# In[4]:

import requests
data=requests.get(url)


# In[8]:

print data


# In[10]:

print data.text


# In[11]:

r=requests.get("http://httpbin.org/get")


# In[12]:

r.status_code


# In[13]:

r=requests.get('http://httpbin.org/status/404')


# In[14]:

r.status_code


# In[15]:

r.headers


# In[16]:

get_ipython().system(u'curl http://httpbin.org/get')


# In[17]:

r1=requests.get('http://httpbin.org/encoding/utf8')


# In[18]:

test1=r1.text[:500]


# In[19]:

print '\u203e'


# In[20]:

import locale
locale.getdefaultlocale()


# In[21]:

print test1


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



