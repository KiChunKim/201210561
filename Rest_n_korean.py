{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import os \n",
    "KEY=\"697a486559636e3037304356486844\" \n",
    "TYPE='json'\n",
    "SERVICE = 'StationAdresTelno' \n",
    "START_INDEX='1'\n",
    "END_INDEX='20'\n",
    "LINE_NUM='2'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "url='http://openapi.seoul.go.kr:8088/'\n",
    "url+=KEY\n",
    "url+='/'\n",
    "url+=TYPE\n",
    "url+='/'\n",
    "url+=SERVICE\n",
    "url+='/'\n",
    "url+=START_INDEX\n",
    "url+='/'\n",
    "url+=END_INDEX\n",
    "url+='/'\n",
    "url+=LINE_NUM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://openapi.seoul.go.kr:8088/697a486559636e3037304356486844/json/StationAdresTelno/1/20/2\n"
     ]
    }
   ],
   "source": [
    "print url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import requests\n",
    "data=requests.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<Response [200]>\n"
     ]
    }
   ],
   "source": [
    "print data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\"StationAdresTelno\":{\"list_total_count\":51,\"RESULT\":{\"CODE\":\"INFO-000\",\"MESSAGE\":\"정상 처리되었습니다\"},\"row\":[{\"LINE\":\"2호선\",\"STATN_NM\":\"시청\",\"ADRES\":\"서울 중구 서소문동 27\",\"RDNMADR\":\"서울특별시 중구 서소문로 지하 127 (서소문동) (2호선 시청역)\",\"TELNO\":\"6110-2011\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"을지로입구\",\"ADRES\":\"서울 중구 을지로1가 89-1\",\"RDNMADR\":\"서울특별시 중구 을지로 지하 42 (을지입구역)\",\"TELNO\":\"6110-2021\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"을지로3가\",\"ADRES\":\"서울 중구 을지로3가 70-1\",\"RDNMADR\":\"서울특별시 중구 을지로 지하 106 (2호선 을지로3가역)\",\"TELNO\":\"6110-2031\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"을지로4가\",\"ADRES\":\"서울 중구 을지로4가 261-1\",\"RDNMADR\":\"서울특별시 중구 을지로 지하 178 (2호선 을지로4가역)\",\"TELNO\":\"6110-2041\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"동대문역사문화공원\",\"ADRES\":\"서울 중구 을지로7가 1\",\"RDNMADR\":\"서울특별시 중구 을지로 지하 279 (2호선 동대문역역사문화공원역)\",\"TELNO\":\"6110-2051\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"신당\",\"ADRES\":\"서울 중구 신당5동 106-1\",\"RDNMADR\":\"서울특별시 중구 퇴계로 지하 431-1 (2호선 신당역)\",\"TELNO\":\"6110-2061\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"상왕십리\",\"ADRES\":\"서울 성동구 하왕십리2동 946-14\",\"RDNMADR\":\"서울특별시 성동구 왕십리로 지하 374 (상왕십리역)\",\"TELNO\":\"6110-2071\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"왕십리\",\"ADRES\":\"서울 성동구 행당1동 246\",\"RDNMADR\":\"서울특별시 성동구 왕십리로 지하300 (2호선 왕십리역)\",\"TELNO\":\"6110-2081\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"한양대\",\"ADRES\":\"서울 성동구 행당동 산 17\",\"RDNMADR\":\"서울특별시 성동구 왕십리로 206 (한양대역)\",\"TELNO\":\"6110-2091\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"뚝섬\",\"ADRES\":\"서울 성동구 성수1가2동 656-745\",\"RDNMADR\":\"서울특별시 성동구 아차산로18 (뚝섬역)\",\"TELNO\":\"6110-2101\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"성수\",\"ADRES\":\"서울 성동구 성수2가 3동 300-1\",\"RDNMADR\":\"서울특별시 성동구 아차산로 100 (성수역)\",\"TELNO\":\"6110-2111\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"건대입구\",\"ADRES\":\"서울 광진구 구의로 231\",\"RDNMADR\":\"서울특별시 광진구 아차산로 243 (2호선 건대입구역)\",\"TELNO\":\"6110-2121\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"구의\",\"ADRES\":\"서울 광진구 구의동 245-24\",\"RDNMADR\":\"서울특별시 광진구 아차산로 384-1 (구의역)\",\"TELNO\":\"6110-2131\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"강변\",\"ADRES\":\"서울 광진구 구의3동 546-6\",\"RDNMADR\":\"서울특별시 광진구 강변역로 53 (강변역)\",\"TELNO\":\"6110-2141\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"잠실나루\",\"ADRES\":\"서울 송파구 신천동 1번지\",\"RDNMADR\":\"서울특별시 송파구 오금로 20 (잠실나루역)\",\"TELNO\":\"6110-2151\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"잠실\",\"ADRES\":\"서울 송파구 잠실동 27\",\"RDNMADR\":\"서울특별시 송파구 올림픽로 지하 265 (2호선 잠실역)\",\"TELNO\":\"6110-2161\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"신천\",\"ADRES\":\"서울 송파구 잠실본동 5\",\"RDNMADR\":\"서울특별시 송파구 올림픽로 지하 140 (신천역)\",\"TELNO\":\"6110-2171\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"종합운동장\",\"ADRES\":\"서울 송파구 잠실동 1-236\",\"RDNMADR\":\"서울특별시 송파구 올림픽로 지하 23 (종합운동장역)\",\"TELNO\":\"6110-2181\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"삼성\",\"ADRES\":\"서울 강남구 삼성동 172-82\",\"RDNMADR\":\"서울특별시 강남구 테헤란로 지하 538 (삼성역)\",\"TELNO\":\"6110-2191\"},{\"LINE\":\"2호선\",\"STATN_NM\":\"선릉\",\"ADRES\":\"서울 강남구 삼성2동 143-42\",\"RDNMADR\":\"서울특별시 강남구 테헤란로 지하 340 (2호선 선릉역)\",\"TELNO\":\"6110-2201\"}]}}\n"
     ]
    }
   ],
   "source": [
    "print data.text"
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
    "r=requests.get(\"http://httpbin.org/get\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r.status_code"
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
    "r=requests.get('http://httpbin.org/status/404')"
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
       "404"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r.status_code"
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
     "data": {
      "text/plain": [
       "{'Content-Length': '0', 'Server': 'nginx', 'Connection': 'keep-alive', 'Access-Control-Allow-Credentials': 'true', 'Date': 'Sun, 16 Oct 2016 15:57:51 GMT', 'Access-Control-Allow-Origin': '*', 'Content-Type': 'text/html; charset=utf-8'}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r.headers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "  \"args\": {}, \n",
      "  \"headers\": {\n",
      "    \"Accept\": \"*/*\", \n",
      "    \"Host\": \"httpbin.org\", \n",
      "    \"User-Agent\": \"curl/7.49.0\"\n",
      "  }, \n",
      "  \"origin\": \"114.204.54.19\", \n",
      "  \"url\": \"http://httpbin.org/get\"\n",
      "}\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n",
      "                                 Dload  Upload   Total   Spent    Left  Speed\n",
      "\n",
      "  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0\n",
      "  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0\n",
      "100   186  100   186    0     0    361      0 --:--:-- --:--:-- --:--:--   361\n"
     ]
    }
   ],
   "source": [
    "!curl http://httpbin.org/get"
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
    "r1=requests.get('http://httpbin.org/encoding/utf8')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "test1=r1.text[:500]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\\u203e\n"
     ]
    }
   ],
   "source": [
    "print '\\u203e'"
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
     "data": {
      "text/plain": [
       "('ko_KR', 'cp949')"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import locale\n",
    "locale.getdefaultlocale()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<h1>Unicode Demo</h1>\n",
      "\n",
      "<p>Taken from <a\n",
      "href=\"http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt\">http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt</a></p>\n",
      "\n",
      "<pre>\n",
      "\n",
      "UTF-8 encoded sample plain-text file\n",
      "‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n",
      "\n",
      "Markus Kuhn [ˈmaʳkʊs kuːn] <http://www.cl.cam.ac.uk/~mgk25/> — 2002-07-25\n",
      "\n",
      "\n",
      "The ASCII compatible UTF-8 encoding used in this plain-text file\n",
      "is defined in Unicode, ISO 10646-1, and RFC 2279.\n",
      "\n",
      "\n",
      "Using Unicode/UTF-8, you can write in emails and so\n"
     ]
    }
   ],
   "source": [
    "print test1"
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
