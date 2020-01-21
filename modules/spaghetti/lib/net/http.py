#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import requests
import utils
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class Http(object):
	''' connection class '''
	# default user-agent
	_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
	# random user-agent
	_random = utils.RandomAgent()
	# checker payload
	_check = utils.Checker()
	# __init__
	def __init__(self,**kwargs):
		self.agent = Http._agent if("agent") not in kwargs else kwargs["agent"]
		self.proxy = None if("proxy") not in kwargs else kwargs["proxy"]
		self.redirect = True if("redirect") not in kwargs else kwargs["redirect"]

	def Send(self,url,method="GET",payload=None,timeout=None,headers=None,cookie=None):
		if payload is None: payload = {}
		if headers is None: headers = {}
		# headers add user-agent
		if '--random-agent' in sys.argv:
			headers['User-Agent'] = Http._random.Randomagent()
		else:
			headers['User-Agent'] = self.agent
		# requests session
		request = requests.Session()
		#req = requests.packages.urllib3.disable_warnings()
		req = requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
		# get method
		if method.upper() == "GET":
			if payload: url = "{}".format(Http._check.Payload(url,payload))
			req = request.request(method.upper(),url,headers=headers,cookies=cookie,allow_redirects=self.redirect,
				timeout=timeout,proxies={'http':self.proxy,'https':self.proxy},verify=False)
		# post method
		elif method.upper() == "POST":
			req = request.request(method.upper(),url,headers=headers,data=payload,cookies=cookie,
				allow_redirects=self.redirect,timeout=timeout,proxies={'http':self.proxy,'https':self.proxy},verify=False)
		# other methods
		elif method.upper():
			req = request.request(method.upper(),url,headers=headers,cookies=cookie,allow_redirects=self.redirect,
				timeout=timeout,proxies={'http':self.proxy,'https':self.proxy},verify=False)
		# return req.__attrs__
		return req