#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import random
import urlparse
 
class RandomAgent():
	def Randomagent(self):
		agent_list = (
			"Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.5.22 Version/10.50",
			"Mozilla/6.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:2.0.0.0) Gecko/20061028 Firefox/3.0",
			"Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/13.0.1",
			"Lynx/2.8.8dev.3 libwww-FM/2.14 SSL-MM/1.4.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
			"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US",
			"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US",
			"Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120724 Debian Iceweasel/15.0")
		return (agent_list[random.randint(0,len(agent_list)-1)])

class Checker():
	@staticmethod
	def Payload(url,payload):
		if url.endswith('/')and(payload.startswith('/')):
			return(url[:-1]+"?"+payload[1:])
		elif not url.endswith('/') and payload.startswith('/'):
			return(url+"?"+payload[1:])
		elif url.endswith('/') and not payload.startswith('/'):
			return(url[:-1]+"?"+payload)
		else:
			return(url+"?"+payload)

	@staticmethod
	def Path(url,path):
		if url.endswith('/')and(path.startswith('/')):
			return(url+path[1:])
		elif not url.endswith('/')and not path.startswith('/'):
			return(url+"/"+path)
		else:
			return(url+path)		

class Parser():
	def ParserUrl(self,url):
		scheme = urlparse.urlsplit(url).scheme
		netloc = urlparse.urlsplit(url).netloc
		path = urlparse.urlsplit(url).path
		query = urlparse.urlsplit(url).query
		if scheme not in ['http','https','']:
			pass
		if netloc == "":
			return("http"+"://"+path)
		else:
			return(scheme+"://"+netloc+path)