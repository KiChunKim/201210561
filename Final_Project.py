
# coding: utf-8

# In[1]:

def getKey(keyPath): #34 Lines
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[2]:

import os

keyPath=os.path.join(os.getcwd(), 'src', 'twitter4j.properties')
key=getKey(keyPath)


# In[3]:

import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client


# In[4]:

import oauth2 as oauth
import json
consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])


# In[5]:

client = oauth.Client(consumer, token)


# In[6]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"


# In[7]:

myparam={'q':'FIFA favorite player','count':300,'since_id':' 770722840979132417'}  #2016년 발롱도르 검색 검색


# In[8]:

mybody=urllib.urlencode(myparam)


# In[9]:

response,content=client.request(url+"?"+mybody,method="GET")


# In[10]:

json.loads(content)


# In[11]:

tsearch_json = json.loads(content)


# In[12]:

f=open('FIFA_twitterff.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    print i, tweet['id'], tweet['text']
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
f.close()


# In[12]:

import urllib
url = "https://api.twitter.com/1.1/followers/list.json"
response, content = client.request(url, method="GET")
tfollower_json = json.loads(content)


# In[12]:

for k,v in tfollower_json.iteritems():
    print k


# In[13]:

timeline = _client.statuses.home_timeline()


# In[14]:

print type(timeline[0])
for key in timeline[0].keys():
    print key,timeline[0][key]

