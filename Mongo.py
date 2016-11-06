
# coding: utf-8

# In[1]:

import pymongo


# In[2]:

from pymongo import MongoClient


# In[3]:

client=MongoClient('localhost:27017')


# In[4]:

db=client.Employees


# In[6]:

db.mytable.find()


# In[7]:

empCol=db.mytable.find()


# In[11]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[12]:

import os

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=getKey(keyPath)


# In[27]:

import os
import requests

KEY=str(key['dataseoul'])
TYPE='json'
SERVICE='CardSubwayStatisticsService'
START_INDEX=1
END_INDEX=5
USE_MON='201306'
url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=str(START_INDEX)
url+='/'
url+=str(END_INDEX)
url+='/'
url+=USE_MON


# In[28]:

response = requests.get(url).text
print response


# In[29]:

import json
jd = json.loads(response)


# In[30]:

print jd['CardSubwayStatisticsService']['row'][0]


# In[ ]:



