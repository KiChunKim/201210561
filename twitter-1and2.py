
# coding: utf-8

# In[31]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[32]:

import os
os.path.expanduser("~")


# In[38]:

import os

keyPath=os.path.join(os.getcwd(), 'src', 'twitter4j.properties')
key=getKey(keyPath)


# In[39]:

import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client


# In[42]:

_client.statuses.update(status="Hello Twitter 1 160777")


# In[47]:

import oauth2 as oauth
import json
consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])


# In[49]:

client = oauth.Client(consumer, token)


# In[50]:

help(client.request)


# In[51]:

import urllib
url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'Hello 21 160777'})
response,content=client.request(url,method='POST',body=mybody)


# In[52]:

import io
with io.open('src/ds_twitter_1.json', 'w', encoding='utf8') as json_file:
    data=json.dumps(content, json_file, ensure_ascii=False, encoding='utf8')
    json_file.write(data)


# In[53]:

timeline = _client.statuses.home_timeline()


# In[54]:

print type(timeline)
print len(timeline)


# In[55]:

print type(timeline[0])
for key in timeline[0].keys():
    print key,timeline[0][key]


# In[58]:

for tweet in timeline:
     print tweet['id'],tweet['text']


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



