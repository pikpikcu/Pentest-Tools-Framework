#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

import sys
import random
import urllib3
import requests

class UCheck:
	def payload(self,url,payload):
		
		if url.endswith('/') & payload.startswith('/'):
			return str(url[:-1]+"?"+payload[1:])

		elif not url.endswith('/') & payload.startswith('/'):
			return str(url+"?"+payload[1:])

		elif url.endswith('/') and not payload.startswith('/'):
			return str(url[:-1]+"?"+payload)

		else:
			return str(url+"?"+payload)

	def path(self,url,path):
		
		if url.endswith('/') & path.startswith('/'):
			if not path.endswith('/'):
				return str(url[:-1]+path)
			else:
				return str(url+path[:-1])
		
		elif not url.endswith('/') and not path.startswith('/'):
			if not path.endswith('/'):
				return str(url+"/"+path)
			else:
				return str(url+"/"+path[:-1])
		
		else:
			if not path.endswith('/'):
				return str(url+path)
			else:
				return str(url+path[:-1])

class wphttp(object):
	ucheck = UCheck()
	def __init__(self,**k):
		self.agent = None if "agent" not in k else k["agent"]
		self.proxy = None if "proxy" not in k else k["proxy"]
		self.redir = True if "redir" not in k else k["redir"]
		self.time  = None if "time"  not in k else k["time" ]

	def ragent(self):
		ag = (
			'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
			'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
			'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US',
			'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)',
			'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0',
			'Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1',
			'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko/20100101 Firefox/11.0',
			'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705)',
			'Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1',
			'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
			'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01',
			'Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1',
			'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
			)
		return str(ag[random.randint(0,len(ag)-1)])

	def send(self,u,m="GET",p=None,h=None,c=None):
		if p is None : p = {}
		if h is None : h = {}
		if c is not None : c = {c:''}
		if '-r' in sys.argv or '--ragent' in sys.argv:
			h['user-agent'] = self.ragent()
		else:
			h['user-agent'] = self.agent
		# request
		request = requests.Session()
		req = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		# get
		if m.lower()=='get':
			if p: u='{}'.format(Request.ucheck.payload(u,p))
			req = request.request(
				method=m.upper(),url=u,headers=h,cookies=c,timeout=self.time,
				allow_redirects=self.redir,proxies={'http':self.proxy,'https':self.proxy},verify=False)
		# post
		elif m.lower()=='post':
			req = request.request(
				method=m.upper(),url=u,headers=h,cookies=c,timeout=self.time,
				allow_redirects=self.redir,proxies={'http':self.proxy,'https':self.proxy},verify=False)
		# req
		return req