
# coding: utf-8

# In[7]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[8]:

import os

keyPath=os.path.join(os.getcwd(), 'src', 'twitter4j.properties')
key=getKey(keyPath)


# In[9]:

import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client


# In[10]:

import oauth2 as oauth
import json
consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])


# In[11]:

client = oauth.Client(consumer, token)


# In[16]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"


# In[25]:

myparam={'q':'messi','count':50,'since_id':'795410088517214208'} #메시에 대해서 검색


# In[26]:

mybody=urllib.urlencode(myparam)


# In[27]:

response,content=client.request(url+"?"+mybody,method="GET")


# In[28]:

json.loads(content)


# In[30]:

tsearch_json = json.loads(content)


# In[31]:

for tweet in tsearch_json['statuses']:
    print tweet['id']


# In[32]:

f=open('messi_twitter_1.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    print i, tweet['id'], tweet['text']
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
f.close()


# In[33]:

import urllib
url = "https://api.twitter.com/1.1/followers/list.json"
response, content = client.request(url, method="GET")
tfollower_json = json.loads(content)


# In[34]:

for k,v in tfollower_json.iteritems():
    print k


# In[36]:

for i in tfollower_json['users']:
    print i['id'],i['screen_name']


# In[37]:

for k,v in tfollower_json['users'][0].iteritems():
        print k


# In[40]:

timeline = _client.statuses.home_timeline()


# In[41]:

print type(timeline[0])
for key in timeline[0].keys():
    print key,timeline[0][key]


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



