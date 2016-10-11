{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 코스피 지수 크롤링 하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import urllib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "cospi = urllib.urlopen('https://www.google.com/finance/historical?q=KRX%3AKOSPI200&hl=en&ei=nt77V7nqDsyJ0gSZ6r-QCQ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_html = cospi.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23694\n"
     ]
    }
   ],
   "source": [
    "print len(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from lxml import etree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_htmlTree = etree.HTML(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "lxml.etree._Element"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(_htmlTree)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "result = etree.tostring(_htmlTree, pretty_print=True, method=\"html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25406\n"
     ]
    }
   ],
   "source": [
    "print len(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "nodes1 = _htmlTree.xpath('//*[@class=\"lm\"]/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "nodes2 = _htmlTree.xpath('//*[@class=\"rgt\"]/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "nodes3 = _htmlTree.xpath('//*[@class=\"rgt rm\"]/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "str1 = _htmlTree.xpath('//*[@class=\"bb lm lft\"]/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "\n",
    "str2 = _htmlTree.xpath('//*[@class=\"rgt bb\"]/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "str3 = _htmlTree.xpath('//*[@class=\"rgt bb rm\"]/text()')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print len(str1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "print len(nodes3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "print len(nodes1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "print len(nodes2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date Open High Low Close Volume\n",
      "\n",
      "Oct 10, 2016 258.85 260.71 257.68 260.31 74,083,000\n",
      "\n",
      "Oct 7, 2016 261.17 261.53 259.73 260.06 62,369,000\n",
      "\n",
      "Oct 6, 2016 261.60 261.68 259.65 261.13 64,936,000\n",
      "\n",
      "Oct 5, 2016 257.51 259.49 256.67 258.99 58,014,000\n",
      "\n",
      "Oct 4, 2016 259.51 259.74 258.55 259.18 62,561,000\n",
      "\n",
      "Sep 30, 2016 258.30 258.91 257.29 257.49 74,918,000\n",
      "\n",
      "Sep 29, 2016 259.60 260.95 259.60 260.35 65,365,000\n",
      "\n",
      "Sep 28, 2016 259.32 259.46 257.96 258.21 59,186,000\n",
      "\n",
      "Sep 27, 2016 256.16 259.87 255.16 259.57 58,684,000\n",
      "\n",
      "Sep 26, 2016 258.07 259.32 256.90 257.48 43,876,000\n",
      "\n",
      "Sep 23, 2016 258.44 259.14 257.71 258.37 58,392,000\n",
      "\n",
      "Sep 22, 2016 258.46 259.99 258.13 258.34 59,904,000\n",
      "\n",
      "Sep 21, 2016 254.65 256.55 254.56 256.52 51,982,000\n",
      "\n",
      "Sep 20, 2016 253.86 255.23 253.33 255.09 54,626,000\n",
      "\n",
      "Sep 19, 2016 251.51 254.54 251.38 253.93 59,750,000\n",
      "\n",
      "Sep 13, 2016 253.39 253.55 251.66 251.77 74,548,000\n",
      "\n",
      "Sep 12, 2016 252.37 253.43 250.53 250.53 66,332,000\n",
      "\n",
      "Sep 9, 2016 258.68 258.94 256.21 257.31 70,053,000\n",
      "\n",
      "Sep 8, 2016 260.72 261.48 259.41 260.86 79,382,000\n",
      "\n",
      "Sep 7, 2016 261.15 262.10 260.31 260.31 68,749,000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for y in range(1):\n",
    "    m = 4*y\n",
    "    print str1[y].strip(), str2[m].strip(), str2[m+1].strip(), str2[m+2].strip(), str2[m+3].strip(), str3[y]\n",
    "for i in range(20):\n",
    "    n =4*i\n",
    "    print nodes1[i].strip(), nodes2[n].strip(), nodes2[n+1].strip(), nodes2[n+2].strip(), nodes2[n+3].strip(), nodes3[i]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
