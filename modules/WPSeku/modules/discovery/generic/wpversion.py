#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

import re
import json
import requests

from lib import wphttp
from lib import wpprint

class wpversion:
	
	chk = wphttp.UCheck() 
	out = wpprint.wpprint()
	
	def __init__(self,agent,proxy,redir,time,url,cookie):
		self.url = url
		self.agent = agent
		self.cookie = cookie
		self.req = wphttp.wphttp(
			agent=agent,proxy=proxy,
			redir=redir,time=time
			)
	def run(self):
		try:
			url = wpversion.chk.path(self.url,'/wp-links-opml.php')
			resp = self.req.send(url,c=self.cookie)
			if resp.status_code == 200 and resp._content != None:
				vers = re.findall(r'\S+WordPress/(\d+.\d+[.\d+]*)',resp._content)
				if vers:
					wpversion.out.plus('Running WordPress version: {}'.format(vers[0]))
					self.dbwpscan(vers[0])
		except Exception,e:
			try:
				url = wpversion.chk.path(self.url,'/feed')
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp._content != None:
					vers = re.findall(r'\S+?v=(\d+.\d+[.\d+]*)',resp._content)
					if vers:
						wpversion.out.plus('Running WordPress version: {}'.format(vers[0]))
						self.dbwpscan(vers[0])
			except Exception,e:
				try:
					url = wpversion.chk.path(self.url,'/feed/atom')
					resp = self.req.send(url,c=self.cookie)
					if resp.status_code == 200 and resp._content != None:
						vers = re.findall(r'<generator uri="http://wordpress.org/" version="(\d+\.\d+[\.\d+]*)"',resp._content)
						if vers:
							wpversion.out.plus('Running WordPress version: {}'.format(vers[0]))
							self.dbwpscan(vers[0])
				except Exception,e:
					try:
						url = wpversion.chk.path(self.url,'readme.html')
						resp = self.req.send(url,c=self.cookie)
						if resp.status_code == 200 and resp._content != None:
							vers = re.findall(r'.*wordpress-logo.png" /></a>\n.*<br />.* (\d+\.\d+[\.\d+]*)\n</h1>',resp._content)
							if vers:
								wpversion.out.plus('Running WordPress version: {}'.format(vers[0]))
								self.dbwpscan(vers[0])
					except Exception,e:
						try:
							url = wpversion.chk.path(self.url,'')
							resp = self.req.send(url,c=self.cookie)
							if resp.status_code == 200 and resp._content != None:
								vers = re.findall(r'<meta name="generator" content="WordPress (\d+\.\d+[\.\d+]*)"',resp._content)
								if vers:
									wpversion.out.plus('Running WordPress version: {}'.format(vers[0]))
									self.dbwpscan(vers[0])
						except Exception,e:
							pass

	def dbwpscan(self,version):
		try:
			url = "https://www.wpvulndb.com/api/v2/wordpresses/{}".format(self.Version(version))
			resp = requests.packages.urllib3.disable_warnings()
			resp = requests.get(url,headers={'user-agent':self.agent},verify=False)
			js = json.loads(resp._content,'UTF-8')
			if js[version]:
				if js[version]['release_date']:
					wpversion.out.more('Release date: {}'.format(js[version]['release_date']))
				if js[version]['vulnerabilities']:
					for x in xrange(len(js[version]['vulnerabilities'])):
						wpversion.out.more('Title: {}'.format(js[version]['vulnerabilities'][x]['title']))
						if js[version]['vulnerabilities'][x]['references']['url']:
							for y in range(len(js[version]['vulnerabilities'][x]['references']['url'])):
								wpversion.out.more('Reference: {}'.format(js[version]['vulnerabilities'][x]['references']['url'][y]))
						wpversion.out.more('Fixed in: {}'.format(js[version]['vulnerabilities'][x]['fixed_in']))
				elif not js[version]['vulnerabilities']:
					wpversion.out.more('Not found vulnerabilities')
			elif not js[version]:
				wpversion.out.more('Not found vulnerabilities')
		except Exception,e:
			pass

	def Version(self,vers):
		try:
			v = ""
			for vv in xrange(len(vers.split('.'))):
				v += vers.split('.')[vv]
			return v
		except Exception,e:
			pass