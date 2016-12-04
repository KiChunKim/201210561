
# coding: utf-8

# In[15]:

import findspark


# In[16]:

import os
spark_home='C:/Users/k-chun/Documents/spark/spark-2.0.2-bin-hadoop2.6'


# In[17]:

findspark.init(spark_home)


# In[20]:

import pyspark
conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc=pyspark.SparkContext()


# In[21]:

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)


# In[22]:

from pyspark.mllib.regression import LabeledPoint
p = [LabeledPoint(1,[1.0,2.0,3.0]),
     LabeledPoint(1,[1.1,2.1,3.1]),
     LabeledPoint(0,[1.2,2.2,3.3])]
trainDf=sqlCtx.createDataFrame(p)
trainDf.collect()


# In[83]:

svmfn="C:\Users\k-chun\Documents\spark\spark-2.0.2-bin-hadoop2.6\data\mllib.txt"


# In[84]:

print svmfn


# In[85]:

svmDf=sqlCtx.read.format("libsvm").load(svmfn) #실행 오류 나왔습니다...


# In[38]:

lines = sc.textFile("spark(txt)/ronaldo_wiki.txt")


# In[39]:

lines.flatMap(lambda x:x.split())


# In[40]:

wc=lines.flatMap(lambda x:x.split())


# In[41]:

wc.collect()


# In[42]:

from operator import add
wc = sc.textFile("spark(txt)/ronaldo_wiki.txt")    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())    .map(lambda x:x.split())    .map(lambda x:[(i,1) for i in x])


# In[43]:

for e in wc.collect():
    print e 


# # json 파일읽기 

# In[58]:

sqlCtx.read.json("C:/Users/k-chun/Documents/spark/spark-2.0.2-bin-hadoop2.6/examples/src/main/resources/people.json")


# In[67]:

pdf=sqlCtx.read.json("C:/Users/k-chun/Documents/spark/spark-2.0.2-bin-hadoop2.6/examples/src/main/resources/people.json")


# In[68]:

p = [{'name': 'kim', 'height': 170}]
sqlCtx.createDataFrame(p).collect()

type(p)

from pyspark.sql import *
pRow=list(Row(name="kim", height=1961))

df=sqlCtx.createDataFrame([pRow])
df.show()


# In[69]:

type(pdf)


# In[71]:

pdf.filter(pdf['age']>21).show()


# In[73]:

pdf.registerTempTable("people") 
sqlCtx.sql("select age from people").show()


# # url을 읽어오기

# In[74]:

import requests
r=requests.get("https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json")


# In[75]:

wc=r.json()


# In[76]:

print wc[0]


# In[77]:

sqlCtx.createDataFrame(wc)


# In[78]:

wcDf=sqlCtx.createDataFrame(wc)


# In[79]:

wcDf.printSchema()


# In[81]:

wcDf.registerTempTable("wc")


# In[82]:

sqlCtx.sql("select Club, Team, Year from wc").show()

