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
    "import urllib"
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
    "response = urllib.urlopen('http://python.org/')"
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
     "data": {
      "text/plain": [
       "<addinfourl at 54878472L whose fp = <socket._fileobject object at 0x00000000034461B0>>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response"
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
    "_html=response.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "p=re.compile('href=\"(http://.*?)\"')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "res=p.findall(_html)"
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
      "http://www.ie6countdown.com/\n",
      "http://browsehappy.com/\n",
      "http://www.google.com/chromeframe/?redirect=true\n",
      "http://plus.google.com/+Python\n",
      "http://www.facebook.com/pythonlang?fref=ts\n",
      "http://twitter.com/ThePSF\n",
      "http://brochure.getpython.info/\n",
      "http://wiki.python.org/moin/Languages\n",
      "http://python.org/dev/peps/\n",
      "http://planetpython.org/\n",
      "http://pyfound.blogspot.com/\n",
      "http://pycon.blogspot.com/\n",
      "http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator\n",
      "http://blog.python.org\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/fAqupGsm4LQ/python-360b2-is-now-available.html\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/ZLTGxjKhYp0/python-core-development-sprint-2016-36.html\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/6vXS6z9YHg0/python-360-beta-1-is-now-available.html\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/ukG8L0FEq2Q/python-360-alpha-4-preview-release-is.html\n",
      "http://feedproxy.google.com/~r/PythonInsider/~3/6i6vUY_x_SE/python-360-alpha-3-preview-release-is.html\n",
      "http://www.djangoproject.com/\n",
      "http://www.pylonsproject.org/\n",
      "http://bottlepy.org\n",
      "http://tornadoweb.org\n",
      "http://flask.pocoo.org/\n",
      "http://www.web2py.com/\n",
      "http://www.wxpython.org/\n",
      "http://wiki.python.org/moin/TkInter\n",
      "http://www.pygtk.org\n",
      "http://www.riverbankcomputing.co.uk/software/pyqt/intro\n",
      "http://www.scipy.org\n",
      "http://pandas.pydata.org/\n",
      "http://ipython.org\n",
      "http://buildbot.net/\n",
      "http://trac.edgewall.org/\n",
      "http://roundup.sourceforge.net/\n",
      "http://www.ansible.com\n",
      "http://www.saltstack.com\n",
      "http://brochure.getpython.info/\n",
      "http://wiki.python.org/moin/Languages\n",
      "http://python.org/dev/peps/\n",
      "http://planetpython.org/\n",
      "http://pyfound.blogspot.com/\n",
      "http://pycon.blogspot.com/\n",
      "http://docs.python.org/devguide/\n",
      "http://bugs.python.org/\n",
      "http://pythonmentors.com/\n"
     ]
    }
   ],
   "source": [
    "for item in res:\n",
    "    print item"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
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
   "execution_count": 10,
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
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Element html at 0x362a348>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "_htmlTree"
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
    "nodes = _htmlTree.xpath('//a[@href]')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'href': '#content', 'title': 'Skip to content'}\n",
      "{'href': '#python-network', 'aria-hidden': 'true', 'id': 'close-python-network', 'class': 'jump-link'}\n",
      "{'href': '/', 'class': 'current_item selectedcurrent_branch selected', 'title': 'The Python Programming Language'}\n",
      "{'href': '/psf-landing/', 'title': 'The Python Software Foundation'}\n",
      "{'href': 'https://docs.python.org', 'title': 'Python Documentation'}\n",
      "{'href': 'https://pypi.python.org/', 'title': 'Python Package Index'}\n",
      "{'href': '/jobs/', 'title': 'Python Job Board'}\n",
      "{'href': '/community/', 'title': 'Python Community'}\n",
      "{'href': '#top', 'aria-hidden': 'true', 'id': 'python-network', 'class': 'jump-link'}\n",
      "{'href': '/'}\n",
      "{'href': '#site-map', 'id': 'site-map-link', 'class': 'jump-to-menu'}\n",
      "{'href': '#', 'class': 'action-trigger'}\n",
      "{'href': 'javascript:;', 'class': 'text-shrink', 'title': 'Make Text Smaller'}\n",
      "{'href': 'javascript:;', 'class': 'text-grow', 'title': 'Make Text Larger'}\n",
      "{'href': 'javascript:;', 'class': 'text-reset', 'title': 'Reset any font size changes I have made'}\n",
      "{'href': '#', 'class': 'action-trigger'}\n",
      "{'href': 'http://plus.google.com/+Python'}\n",
      "{'href': 'http://www.facebook.com/pythonlang?fref=ts'}\n",
      "{'href': 'http://twitter.com/ThePSF'}\n",
      "{'href': '/community/irc/'}\n",
      "{'href': '/accounts/login/', 'title': 'Sign Up or Sign In to Python.org'}\n",
      "{'href': '/accounts/signup/'}\n",
      "{'href': '/accounts/login/'}\n",
      "{'href': '/about/', 'class': '', 'title': ''}\n",
      "{'href': '/about/apps/', 'title': ''}\n",
      "{'href': '/about/quotes/', 'title': ''}\n",
      "{'href': '/about/gettingstarted/', 'title': ''}\n",
      "{'href': '/about/help/', 'title': ''}\n",
      "{'href': 'http://brochure.getpython.info/', 'title': ''}\n",
      "{'href': '/downloads/', 'class': '', 'title': ''}\n",
      "{'href': '/downloads/', 'title': ''}\n",
      "{'href': '/downloads/source/', 'title': ''}\n",
      "{'href': '/downloads/windows/', 'title': ''}\n",
      "{'href': '/downloads/mac-osx/', 'title': ''}\n",
      "{'href': '/download/other/', 'title': ''}\n",
      "{'href': 'https://docs.python.org/3/license.html', 'title': ''}\n",
      "{'href': '/download/alternatives', 'title': ''}\n",
      "{'href': '/doc/', 'class': '', 'title': ''}\n",
      "{'href': '/doc/', 'title': ''}\n",
      "{'href': '/doc/av', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/BeginnersGuide', 'title': ''}\n",
      "{'href': 'https://docs.python.org/devguide/', 'title': ''}\n",
      "{'href': 'https://docs.python.org/faq/', 'title': ''}\n",
      "{'href': 'http://wiki.python.org/moin/Languages', 'title': ''}\n",
      "{'href': 'http://python.org/dev/peps/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/PythonBooks', 'title': ''}\n",
      "{'href': '/community/', 'class': '', 'title': ''}\n",
      "{'href': '/community/diversity/', 'title': ''}\n",
      "{'href': '/community/irc/', 'title': ''}\n",
      "{'href': '/community/lists/', 'title': ''}\n",
      "{'href': '/community/workshops/', 'title': ''}\n",
      "{'href': '/community/sigs/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/', 'title': ''}\n",
      "{'href': '/community/logos/', 'title': ''}\n",
      "{'href': '/community/merchandise/', 'title': ''}\n",
      "{'href': '/community/awards', 'title': ''}\n",
      "{'href': '/about/success/', 'class': '', 'title': 'success-stories'}\n",
      "{'href': '/about/success/#arts', 'title': ''}\n",
      "{'href': '/about/success/#business', 'title': ''}\n",
      "{'href': '/about/success/#education', 'title': ''}\n",
      "{'href': '/about/success/#engineering', 'title': ''}\n",
      "{'href': '/about/success/#government', 'title': ''}\n",
      "{'href': '/about/success/#scientific', 'title': ''}\n",
      "{'href': '/about/success/#software-development', 'title': ''}\n",
      "{'href': '/blogs/', 'class': '', 'title': 'News from around the Python world'}\n",
      "{'href': '/blogs/', 'title': 'Python Insider Blog Posts'}\n",
      "{'href': 'http://planetpython.org/', 'title': 'Planet Python'}\n",
      "{'href': 'http://pyfound.blogspot.com/', 'title': 'PSF Blog'}\n",
      "{'href': 'http://pycon.blogspot.com/', 'title': 'PyCon Blog'}\n",
      "{'href': '/events/', 'class': '', 'title': ''}\n",
      "{'href': '/events/python-events', 'title': ''}\n",
      "{'href': '/events/python-user-group/', 'title': ''}\n",
      "{'href': '/events/python-events/past/', 'title': ''}\n",
      "{'href': '/events/python-user-group/past/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', 'title': ''}\n",
      "{'href': '/shell/', 'data-shell-container': '#dive-into-python', 'class': 'button prompt', 'id': 'start-shell'}\n",
      "{'href': '//docs.python.org/3/tutorial/controlflow.html#defining-functions'}\n",
      "{'href': '//docs.python.org/3/tutorial/introduction.html#lists'}\n",
      "{'href': 'http://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator'}\n",
      "{'href': '//docs.python.org/3/tutorial/'}\n",
      "{'href': '//docs.python.org/3/tutorial/controlflow.html'}\n",
      "{'href': '/doc/', 'class': 'readmore'}\n",
      "{'href': '/about/gettingstarted/'}\n",
      "{'href': 'https://wiki.python.org/moin/Python2orPython3'}\n",
      "{'href': '/downloads/release/python-352/'}\n",
      "{'href': '/downloads/release/python-2712/'}\n",
      "{'href': 'https://docs.python.org'}\n",
      "{'href': '//jobs.python.org'}\n",
      "{'href': 'http://blog.python.org', 'title': 'More News'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/fAqupGsm4LQ/python-360b2-is-now-available.html'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/ZLTGxjKhYp0/python-core-development-sprint-2016-36.html'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/6vXS6z9YHg0/python-360-beta-1-is-now-available.html'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/ukG8L0FEq2Q/python-360-alpha-4-preview-release-is.html'}\n",
      "{'href': 'http://feedproxy.google.com/~r/PythonInsider/~3/6i6vUY_x_SE/python-360-alpha-3-preview-release-is.html'}\n",
      "{'href': '/events/calendars/', 'title': 'More Events'}\n",
      "{'href': '/events/python-events/455/'}\n",
      "{'href': '/events/python-events/374/'}\n",
      "{'href': '/events/python-user-group/469/'}\n",
      "{'href': '/events/python-user-group/464/'}\n",
      "{'href': '/events/python-events/416/'}\n",
      "{'href': '/success-stories/', 'title': 'More Success Stories'}\n",
      "{'href': '/success-stories/industrial-light-magic-runs-python/'}\n",
      "{'href': '/success-stories/industrial-light-magic-runs-python/'}\n",
      "{'href': '/about/apps', 'title': 'More Applications'}\n",
      "{'href': 'http://www.djangoproject.com/', 'class': 'tag'}\n",
      "{'href': 'http://www.pylonsproject.org/', 'class': 'tag'}\n",
      "{'href': 'http://bottlepy.org', 'class': 'tag'}\n",
      "{'href': 'http://tornadoweb.org', 'class': 'tag'}\n",
      "{'href': 'http://flask.pocoo.org/', 'class': 'tag'}\n",
      "{'href': 'http://www.web2py.com/', 'class': 'tag'}\n",
      "{'href': 'http://www.wxpython.org/', 'class': 'tag'}\n",
      "{'href': 'http://wiki.python.org/moin/TkInter', 'class': 'tag'}\n",
      "{'href': 'http://www.pygtk.org', 'class': 'tag'}\n",
      "{'href': 'https://wiki.gnome.org/Projects/PyGObject', 'class': 'tag'}\n",
      "{'href': 'http://www.riverbankcomputing.co.uk/software/pyqt/intro', 'class': 'tag'}\n",
      "{'href': 'http://www.scipy.org', 'class': 'tag'}\n",
      "{'href': 'http://pandas.pydata.org/', 'class': 'tag'}\n",
      "{'href': 'http://ipython.org', 'class': 'tag'}\n",
      "{'href': 'http://buildbot.net/', 'class': 'tag'}\n",
      "{'href': 'http://trac.edgewall.org/', 'class': 'tag'}\n",
      "{'href': 'http://roundup.sourceforge.net/', 'class': 'tag'}\n",
      "{'href': 'http://www.ansible.com', 'class': 'tag'}\n",
      "{'href': 'http://www.saltstack.com', 'class': 'tag'}\n",
      "{'href': 'https://www.openstack.org', 'class': 'tag'}\n",
      "{'href': '/dev/peps/'}\n",
      "{'href': '/dev/peps/peps.rss', 'class': 'rss-link', 'aria-hidden': 'true'}\n",
      "{'href': '/psf/'}\n",
      "{'href': '/psf/', 'class': 'readmore'}\n",
      "{'href': '/users/membership/', 'class': 'button'}\n",
      "{'href': '/psf/donations/', 'class': 'button'}\n",
      "{'href': '#python-network', 'id': 'back-to-top-1', 'class': 'jump-link'}\n",
      "{'href': '/about/'}\n",
      "{'href': '/about/apps/', 'title': ''}\n",
      "{'href': '/about/quotes/', 'title': ''}\n",
      "{'href': '/about/gettingstarted/', 'title': ''}\n",
      "{'href': '/about/help/', 'title': ''}\n",
      "{'href': 'http://brochure.getpython.info/', 'title': ''}\n",
      "{'href': '/downloads/'}\n",
      "{'href': '/downloads/', 'title': ''}\n",
      "{'href': '/downloads/source/', 'title': ''}\n",
      "{'href': '/downloads/windows/', 'title': ''}\n",
      "{'href': '/downloads/mac-osx/', 'title': ''}\n",
      "{'href': '/download/other/', 'title': ''}\n",
      "{'href': 'https://docs.python.org/3/license.html', 'title': ''}\n",
      "{'href': '/download/alternatives', 'title': ''}\n",
      "{'href': '/doc/'}\n",
      "{'href': '/doc/', 'title': ''}\n",
      "{'href': '/doc/av', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/BeginnersGuide', 'title': ''}\n",
      "{'href': 'https://docs.python.org/devguide/', 'title': ''}\n",
      "{'href': 'https://docs.python.org/faq/', 'title': ''}\n",
      "{'href': 'http://wiki.python.org/moin/Languages', 'title': ''}\n",
      "{'href': 'http://python.org/dev/peps/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/PythonBooks', 'title': ''}\n",
      "{'href': '/community/'}\n",
      "{'href': '/community/diversity/', 'title': ''}\n",
      "{'href': '/community/irc/', 'title': ''}\n",
      "{'href': '/community/lists/', 'title': ''}\n",
      "{'href': '/community/workshops/', 'title': ''}\n",
      "{'href': '/community/sigs/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/', 'title': ''}\n",
      "{'href': '/community/logos/', 'title': ''}\n",
      "{'href': '/community/merchandise/', 'title': ''}\n",
      "{'href': '/community/awards', 'title': ''}\n",
      "{'href': '/about/success/', 'title': 'success-stories'}\n",
      "{'href': '/about/success/#arts', 'title': ''}\n",
      "{'href': '/about/success/#business', 'title': ''}\n",
      "{'href': '/about/success/#education', 'title': ''}\n",
      "{'href': '/about/success/#engineering', 'title': ''}\n",
      "{'href': '/about/success/#government', 'title': ''}\n",
      "{'href': '/about/success/#scientific', 'title': ''}\n",
      "{'href': '/about/success/#software-development', 'title': ''}\n",
      "{'href': '/blogs/', 'title': 'News from around the Python world'}\n",
      "{'href': '/blogs/', 'title': 'Python Insider Blog Posts'}\n",
      "{'href': 'http://planetpython.org/', 'title': 'Planet Python'}\n",
      "{'href': 'http://pyfound.blogspot.com/', 'title': 'PSF Blog'}\n",
      "{'href': 'http://pycon.blogspot.com/', 'title': 'PyCon Blog'}\n",
      "{'href': '/events/'}\n",
      "{'href': '/events/python-events', 'title': ''}\n",
      "{'href': '/events/python-user-group/', 'title': ''}\n",
      "{'href': '/events/python-events/past/', 'title': ''}\n",
      "{'href': '/events/python-user-group/past/', 'title': ''}\n",
      "{'href': 'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event', 'title': ''}\n",
      "{'href': '/dev/'}\n",
      "{'href': 'http://docs.python.org/devguide/', 'title': ''}\n",
      "{'href': 'http://bugs.python.org/', 'title': ''}\n",
      "{'href': 'https://mail.python.org/mailman/listinfo/python-dev', 'title': ''}\n",
      "{'href': 'http://pythonmentors.com/', 'title': ''}\n",
      "{'href': '#python-network', 'id': 'back-to-top-2', 'class': 'jump-link'}\n",
      "{'href': '/about/help/'}\n",
      "{'href': '/community/diversity/'}\n",
      "{'href': 'https://github.com/python/pythondotorg/issues'}\n",
      "{'href': 'https://status.python.org/'}\n",
      "{'href': '/psf-landing/'}\n",
      "{'href': '/about/legal/'}\n",
      "{'href': '/privacy/'}\n"
     ]
    }
   ],
   "source": [
    "for node in nodes:\n",
    "    print node.attrib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from lxml.cssselect import CSSSelector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel=CSSSelector('p[href]')"
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
    "import lxml.html"
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
    "html= lxml.html.fromstring(_html)"
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
    "results=sel(html)"
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
    "for item in results:\n",
    "    print item.get('href'), item.text"
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
    "sel=CSSSelector('body a')"
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
    "resu=sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "196\n"
     ]
    }
   ],
   "source": [
    "print len(resu)"
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
      "Skip to content\n",
      "\n",
      "                    \n",
      "Python\n",
      "PSF\n",
      "Docs\n",
      "PyPI\n",
      "Jobs\n",
      "Community\n",
      "\n",
      "                    \n",
      "None\n",
      "None\n",
      "None\n",
      "Smaller\n",
      "Larger\n",
      "Reset\n",
      "Socialize\n",
      "None\n",
      "None\n",
      "None\n",
      "None\n",
      "Sign In\n",
      "Sign Up / Register\n",
      "Sign In\n",
      "About\n",
      "Applications\n",
      "Quotes\n",
      "Getting Started\n",
      "Help\n",
      "Python Brochure\n",
      "Downloads\n",
      "All releases\n",
      "Source code\n",
      "Windows\n",
      "Mac OS X\n",
      "Other Platforms\n",
      "License\n",
      "Alternative Implementations\n",
      "Documentation\n",
      "Docs\n",
      "Audio/Visual Talks\n",
      "Beginner's Guide\n",
      "Developer's Guide\n",
      "FAQ\n",
      "Non-English Docs\n",
      "PEP Index\n",
      "Python Books\n",
      "Community\n",
      "Diversity\n",
      "IRC\n",
      "Mailing Lists\n",
      "Python Conferences\n",
      "Special Interest Groups\n",
      "Python Wiki\n",
      "Python Logo\n",
      "Merchandise\n",
      "Community Awards\n",
      "Success Stories\n",
      "Arts\n",
      "Business\n",
      "Education\n",
      "Engineering\n",
      "Government\n",
      "Scientific\n",
      "Software Development\n",
      "News\n",
      "Python News\n",
      "Community News\n",
      "PSF News\n",
      "PyCon News\n",
      "Events\n",
      "Python Events\n",
      "User Group Events\n",
      "Python Events Archive\n",
      "User Group Events Archive\n",
      "Submit an Event\n",
      ">_\n",
      "                        \n",
      "More about defining functions in Python 3\n",
      "More about lists in Python 3\n",
      "More about simple math functions in Python 3\n",
      "Whet your appetite\n",
      "More control flow tools in Python 3\n",
      "Learn More\n",
      "Start with our Beginner’s Guide\n",
      "Check here\n",
      "Python 3.5.2\n",
      "Python 2.7.12\n",
      "docs.python.org\n",
      "jobs.python.org\n",
      "More\n",
      "Python 3.6.0b2 is the second of four planned beta releases of ...\n",
      "From September 5th to the 9th a group of Python ...\n",
      "Python 3.6.0b1 is the first of four planned beta releases of ...\n",
      "Python 3.6.0a4 has been released.  3.6.0a4 is the last of four planned alpha ...\n",
      "Python 3.6.0a3 has been released.  3.6.0a3 is the third of four planned alpha ...\n",
      "More\n",
      "Plone Conference 2016\n",
      "OSCON Europe 2016\n",
      "Chennaipy\n",
      "PyKla monthly meetup\n",
      "PyCon CZ 2016\n",
      "More\n",
      "ILM runs a batch processing environment capable of modeling, rendering and compositing tens of thousands of motion picture frames per day. Thousands of machines running Linux, IRIX, Compaq Tru64, OS X, Solaris, and Windows join together to provide a production pipeline used by ~800 users daily. Speed of development is key, and Python was a faster way to code (and re-code) the programs that control this production pipeline.\n",
      "Industrial Light & Magic Runs on Python\n",
      "More\n",
      "Django\n",
      "Pyramid\n",
      "Bottle\n",
      "Tornado\n",
      "Flask\n",
      "web2py\n",
      "wxPython\n",
      "tkInter\n",
      "PyGtk\n",
      "PyGObject\n",
      "PyQt\n",
      "SciPy\n",
      "Pandas\n",
      "IPython\n",
      "Buildbot\n",
      "Trac\n",
      "Roundup\n",
      "Ansible\n",
      "Salt\n",
      "OpenStack\n",
      "Python Enhancement Proposals\n",
      "None\n",
      "Python Software Foundation\n",
      "Learn more\n",
      "Become a Member\n",
      "Donate to the PSF\n",
      "None\n",
      "About\n",
      "Applications\n",
      "Quotes\n",
      "Getting Started\n",
      "Help\n",
      "Python Brochure\n",
      "Downloads\n",
      "All releases\n",
      "Source code\n",
      "Windows\n",
      "Mac OS X\n",
      "Other Platforms\n",
      "License\n",
      "Alternative Implementations\n",
      "Documentation\n",
      "Docs\n",
      "Audio/Visual Talks\n",
      "Beginner's Guide\n",
      "Developer's Guide\n",
      "FAQ\n",
      "Non-English Docs\n",
      "PEP Index\n",
      "Python Books\n",
      "Community\n",
      "Diversity\n",
      "IRC\n",
      "Mailing Lists\n",
      "Python Conferences\n",
      "Special Interest Groups\n",
      "Python Wiki\n",
      "Python Logo\n",
      "Merchandise\n",
      "Community Awards\n",
      "Success Stories\n",
      "Arts\n",
      "Business\n",
      "Education\n",
      "Engineering\n",
      "Government\n",
      "Scientific\n",
      "Software Development\n",
      "News\n",
      "Python News\n",
      "Community News\n",
      "PSF News\n",
      "PyCon News\n",
      "Events\n",
      "Python Events\n",
      "User Group Events\n",
      "Python Events Archive\n",
      "User Group Events Archive\n",
      "Submit an Event\n",
      "Contributing\n",
      "Developer's Guide\n",
      "Issue Tracker\n",
      "python-dev list\n",
      "Core Mentorship\n",
      "None\n",
      "Help & \n",
      "Diversity \n",
      "Submit Website Bug\n",
      "Status \n",
      "Python Software Foundation\n",
      "Legal Statements\n",
      "Privacy Policy\n"
     ]
    }
   ],
   "source": [
    "for item in resu:\n",
    "    print item.text"
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
  }
 ],
 "metadata": {
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
