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

class wptheme:
	
	chk = wphttp.UCheck() 
	out = wpprint.wpprint()
	
	def __init__(self,agent,proxy,redir,time,url,cookie):
		self.url = url
		self.cookie = cookie
		self.agent = agent
		self.req = wphttp.wphttp(
			agent=agent,proxy=proxy,
			redir=redir,time=time
			)
	def run(self):
		wptheme.out.test('Passive enumerate themes..')
		try:
			url = wptheme.chk.path(self.url,'')
			resp = self.req.send(url,c=self.cookie)
			theme = re.findall(r'/wp-content/themes/(.+?)/',resp.content)
			themes = []
			for th in theme:
				if th not in themes:
					themes.append(th)
			if themes != []:
				if len(themes) == 1:
					wptheme.out.plus('Name: {}'.format(themes[0]))
					self.info(themes[0])
					self.style(themes[0])
					self.changelog(themes[0])
					self.fullpathdisc(themes[0])
					self.license(themes[0])
					self.listing(themes[0])
					self.readme(themes[0])
					self.dbwpscan(themes[0])

				elif len(themes) > 1:
					for theme in themes:
						wptheme.out.plus('Name: {}'.format(theme))
						self.info(theme)
						self.style(theme)
						self.changelog(theme)
						self.fullpathdisc(theme)
						self.license(theme)
						self.listing(theme)
						self.readme(theme)
						self.dbwpscan(theme)

			elif themes == None:
				wptheme.out.warning('Not found themes..')
		except Exception,e:
			print e

	def info(self,theme):
		try:
			path = '/wp-content/themes/{}/{}'.format(theme,'style.css')
			url = wptheme.chk.path(self.url,path)
			resp = self.req.send(url,c=self.cookie)
			if resp.status_code == 200 and resp.content != None:
				wptheme.out.more('Theme Name: {}'.format(re.findall("Theme Name: (\w+)",resp.content)[0]))
				wptheme.out.more('Theme URL: {}'.format(re.findall('Theme URI: (\S+)',resp,content)[0]))
				wptheme.out.more('Author: {}'.format(re.findall('Author: (\S+)',resp.content)[0]))
				wptheme.out.more('Author URL: {}'.format(re.findall('Author URL: (\S+)',resp.content)[0]))
				wptheme.out.more('Version: {}'.format(re.findall('Version: (\d+.\d+[.\d+]*)',resp.content)[0]))
		except Exception,e:
			pass

	def style(self,theme):
		try:
			path = '/wp-content/themes/{}/{}'.format(theme,'style.css')
			url = wptheme.chk.path(self.url,path)
			resp = self.req.send(url,c=self.cookie)
			if resp.status_code == 200 and resp.content != None:
				if resp.url == url:
					wptheme.out.more('Style: {}'.format(resp.url))
		except Exception,e:
			pass

	def changelog(self,theme):
		try:
			ch = ['changelog.txt','changelog.md','CHANGELOG.txt','CHANGELOG.md']
			for pt in ch:
				path = '/wp-content/themes/{}/{}'.format(theme,pt)
				url = wptheme.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						wptheme.out.more('Changelog: {}'.format(resp.url))
						exit()
		except Exception,e:
			pass

	def fullpathdisc(self,theme):
		try:
			ch = ["/404.php","/archive.php","/author.php","/comments.php","/footer.php",
			      "/functions.php","/header.php","/image.php","/page.php","/search.php",
			      "/single.php","/archive.php"
			      ]
			for pt in ch:
				path = '/wp-content/themes/{}/{}'.format(theme,pt)
				url = wptheme.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						if re.search('Fatal error',resp.content):
							wptheme.out.more('Full Path Disclosure: {}'.format(resp.url))
							exit()
		except Exception,e:
			pass

	def license(self,theme):
		try:
			ch = ['license.txt','license.md','LICENSE.md','LICENSE.txt']
			for pt in ch:
				path = '/wp-content/themes/{}/{}'.format(theme,pt)
				url = wptheme.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						wptheme.out.more('License: {}'.format(resp.url))
						exit()
		except Exception,e:
			pass

	def listing(self,theme):
		try:
			ch = ["/js","/css","/images","/inc","/admin","/src","/widgets","/lib","/assets",
			"/includes","/logs","/vendor","/core"
			]
			for pt in ch:
				path = '/wp-content/themes/{}/{}'.format(theme,pt)
				url = wptheme.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						if re.search('Index of',resp.content):
							wptheme.out.more('Listing: {}'.format(resp.url))
		except Exception,e:
			pass

	def readme(self,theme):
		try:
			ch = ['readme.txt','readme.md','README.md','README.txt']
			for pt in ch:
				path = '/wp-content/themes/{}/{}'.format(theme,pt)
				url = wptheme.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						wptheme.out.more('Readme: {}'.format(resp.url))
						exit()
		except Exception,e:
			pass

	def dbwpscan(self,theme):
		try:
			url = "https://www.wpvulndb.com/api/v2/themes/{}".format(theme)
			resp = requests.packages.urllib3.disable_warnings()
			resp = requests.get(url,headers={'user-agent':self.agent},verify=False)
			js = json.loads(resp._content,'UTF-8')
			print js
			if js[theme]:
				if js[theme]['vulnerabilities']:
					for x in xrange(len(js[theme]['vulnerabilities'])):
						wptheme.out.more('Title: {}'.format(js[theme]['vulnerabilities'][x]['title']))
						if js[theme]['vulnerabilities'][x]['references']['url']:
							for y in range(len(js[theme]['vulnerabilities'][x]['references']['url'])):
								wptheme.out.more('Reference: {}'.format(js[theme]['vulnerabilities'][x]['references']['url'][y]))
						wptheme.out.more('Fixed in: {}'.format(js[theme]['vulnerabilities'][x]['fixed_in']))
				elif not js[theme]['vulnerabilities']:
					wptheme.out.more('Not found vulnerabilities')
			elif not js[theme]:
				wptheme.out.more('Not found vulnerabilities')
		except Exception,e:
			pass
