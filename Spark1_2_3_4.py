
# coding: utf-8

# In[1]:

import findspark


# In[2]:

import os
os.getcwd()


# In[3]:

import os
spark_home='C:/Users/k-chun/Documents/spark/spark-2.0.2-bin-hadoop2.6'


# In[4]:

print spark_home


# In[5]:

findspark.init(spark_home)


# In[6]:

import pyspark


# In[7]:

conf=pyspark.SparkConf()


# In[8]:

conf=pyspark.SparkConf().setAppName("myApp")


# In[9]:

sc=pyspark.SparkContext()


# In[14]:

def c2f() :
    c=list([39.2, 36.5,37.0,])
    f=list()
    for x in c:
        _c=9/5*x+32;
        f.append(_c)
        
    return f


# In[16]:

print c2f()


# In[18]:

sc._conf.get("spark.jars.packages")


# In[19]:

sc._conf.getAll()


# In[21]:

get_ipython().run_cell_magic(u'writefile', u'spark(txt)/ronaldo_wiki.txt', u"\ud06c\ub9ac\uc2a4\ud2f0\uc544\ub204 \ud638\ub0a0\ub450 wiki\uac80\uc0c9 \uacb0\uacfc.\nCristiano Ronaldo dos Santos Aveiro, ComM, \nGOIH (Portuguese pronunciation: born 5 February 1985) is a Portuguese professional footballer who plays for Spanish club Real Madrid and the Portugal national team. He is a forward and serves as captain for Portugal. In 2008, he won his first Ballon d'Or and FIFA World Player of the Year awards.\nHe then won the FIFA Ballon d'Or in 2013 and 2014. In 2015, Ronaldo scored his 500th senior career goal for club and country.\nOften ranked the best player in the world and widely regarded as one of the greatest of all time, Ronaldo was named the best Portuguese player of all time by the Portuguese Football Federation,\nduring its 100th anniversary celebrations in 2015. He is the only player to win four European Golden Shoe awards. One of the most marketable athletes in sport, in 2016 Forbes named Ronaldo the world's best paid athlete. In June 2016, ESPN ranked him the world's most famous athlete.")


# In[26]:

textFile=sc.textFile("spark(txt)/ronaldo_wiki.txt")


# In[27]:

type(textFile)


# In[28]:

textFile.take(3)


# In[29]:

textFile.map(lambda x:x.split(' '))


# In[30]:

words=textFile.map(lambda x:x.split(' '))


# In[31]:

words.collect()


# In[32]:

_player=textFile.filter(lambda line:"player" in line)


# In[33]:

_player.count()


# In[34]:

_player2=textFile.filter(lambda line:u"호날두" in line)


# In[35]:

_player2.count()


# In[38]:

print _player2.first()


# In[39]:

a=[1,2,3]


# In[40]:

type(a)


# In[41]:

sc.parallelize(a)


# In[42]:

myrdd=sc.parallelize(a)


# In[44]:

myrdd.take(2)


# In[50]:

def mySplit(x):
    return x.split(" ")

words=textFile.map(mySplit)


# In[51]:

for i in words.collect():
    print i


# In[52]:

words=textFile.map(lambda x:x.split(' '))


# In[56]:

lines = sc.textFile("spark(data)/ronaldo_wiki.txt")
word_count_bo = lines    .flatMap(lambda x: x.split(' '))


# In[63]:

a=["I am Cristiano Ronaldo","I am best player"]
myrdd=sc.parallelize(a)


# In[64]:

myrdd.map(lambda x : x.split(' '))


# In[65]:

words=myrdd.map(lambda x:x.split(' '))


# In[66]:

words.collect()


# In[67]:

myrdd    .map(lambda x:x.split(' '))    .collect()


# In[70]:

myrdd.map(lambda x:x.replace("a","'")).collect()

