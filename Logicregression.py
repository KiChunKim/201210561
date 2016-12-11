
# coding: utf-8

# In[1]:

import findspark


# In[2]:

import os
spark_home='C:/Users/k-chun/Documents/spark/spark-2.0.2-bin-hadoop2.6'


# In[3]:

findspark.init(spark_home)


# In[4]:

import pyspark
conf=pyspark.SparkConf()
conf=pyspark.SparkConf().setAppName("myApp")
sc=pyspark.SparkContext()


# In[5]:

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)


# In[10]:

from pyspark.ml.feature import HashingTF, IDF, Tokenizer, RegexTokenizer
from pyspark.sql import SQLContext

sqlCtx = SQLContext(sc)
df = sqlCtx.createDataFrame(
    [
        [0,'my dog has flea problems. help please.'],
        [1,'maybe not take him to dog park stupid'],
        [0,'my dalmation is so cute. I love him'],
        [1,'stop posting stupid worthless garbage'],
        [0,'mr licks ate my steak how to stop him'],
        [1,'quit buying worthless dog food stupid'],
        [0,u'우리 강아지 벌레 있어요 도와주세요'],
        [0,u'우리 강아지 귀여워 너 사랑해'],
        [1,u'강아지 공원 가지마 바보같이'],
        [1,u'강아지 음식 구매 마세요 바보같이']
    ],
    ['cls','sent']
)


# In[13]:

tokenizer = Tokenizer(inputCol="sent", outputCol="words")
tokDf = tokenizer.transform(df)
tokDf.printSchema()


# In[14]:

for r in tokDf.select("cls", "sent").take(3):
    print(r)


# In[15]:

tokDf.show()


# In[16]:

re = RegexTokenizer(inputCol="sent", outputCol="wordsReg", pattern="\\s+")
regDf=re.transform(df)
regDf.show()


# In[17]:

from sklearn.feature_extraction.text import TfidfVectorizer

vocabulary = "a list of words I want to look for in the documents".split()
vect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', 
                 stop_words='english')
vect.fit(vocabulary)
tfidf=vect.transform(vocabulary)


# In[18]:

hashTF = HashingTF(inputCol="words", outputCol="hash", numFeatures=50)
hashDf = hashTF.transform(tokDf)


# In[20]:

idf = IDF(inputCol="hash", outputCol="idf")
idfModel = idf.fit(hashDf)
idfDf = idfModel.transform(hashDf)
for e in idfDf.select("cls","hash").take(12):
    print(e)


# In[22]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_spark_hello.py', u'print "---------BEGIN-----------"\nimport pyspark\nconf = pyspark.SparkConf().setAppName("myAppName1")\nsc   = pyspark.SparkContext(conf=conf)\nsc.setLogLevel("ERROR")\nprint "---------RESULT-----------"\nprint sc\nrdd = sc.parallelize(range(1000), 10)\nprint "mean=",rdd.mean()\nnums = sc.parallelize([1, 2, 3, 4])\nsquared = nums.map(lambda x: x * x).collect()\nfor num in squared:\n    print "%i " % (num)')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



