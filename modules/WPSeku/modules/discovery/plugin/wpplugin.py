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

class wpplugin:
	
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
		wpplugin.out.test('Passive enumerate plugins..')
		try:
			url = wpplugin.chk.path(self.url,'')
			resp = self.req.send(url,c=self.cookie)
			plugins = re.findall(r'/wp-content/plugins/(.+?)/',resp.content)
			plugin = []
			for pl in plugins:
				if pl not in plugin:
					plugin.append(pl)
			if plugin != []:
				if len(plugin) == 1:
					wpplugin.out.plus('Name: {}'.format(plugin[0]))
					self.changelog(plugin[0])
					self.fullpathdisc(plugin[0])
					self.license(plugin[0])
					self.listing(plugin[0])
					self.readme(plugin[0])
					self.dbwpscan(plugin[0])

				elif len(plugin) > 1:
					for pl in plugin:
						wpplugin.out.plus('Name: {}'.format(pl))
						self.changelog(pl)
						self.fullpathdisc(pl)
						self.license(pl)
						self.listing(pl)
						self.readme(pl)
						self.dbwpscan(pl)

			elif themes == None:
				wpplugin.out.warning('Not found themes..')
		except Exception,e:
			pass

	def changelog(self,plugin):
		try:
			ch = ['changelog.txt','changelog.md','CHANGELOG.txt','CHANGELOG.md']
			for pt in ch:
				path = '/wp-content/plugins/{}/{}'.format(plugin,pt)
				url = wpplugin.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						wpplugin.out.more('Changelog: {}'.format(resp.url))
						exit()
		except Exception,e:
			pass

	def fullpathdisc(self,plugin):
		try:
			ch = ["/404.php","/archive.php","/author.php","/comments.php","/footer.php",
			      "/functions.php","/header.php","/image.php","/page.php","/search.php",
			      "/single.php","/archive.php"
			      ]
			for pt in ch:
				path = '/wp-content/plugins/{}/{}'.format(plugin,pt)
				url = wpplugin.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						if re.search('Fatal error',resp.content):
							wpplugin.out.more('Full Path Disclosure: {}'.format(resp.url))
							exit()
		except Exception,e:
			pass

	def license(self,plugin):
		try:
			ch = ['license.txt','license.md','LICENSE.md','LICENSE.txt']
			for pt in ch:
				path = '/wp-content/plugins/{}/{}'.format(plugin,pt)
				url = wpplugin.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						wpplugin.out.more('License: {}'.format(resp.url))
						exit()
		except Exception,e:
			pass

	def listing(self,plugin):
		try:
			ch = ["/js","/css","/images","/inc","/admin","/src","/widgets","/lib","/assets",
			"/includes","/logs","/vendor","/core"
			]
			for pt in ch:
				path = '/wp-content/plugins/{}/{}'.format(plugin,pt)
				url = wpplugin.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						if re.search('Index of',resp.content):
							wpplugin.out.more('Listing: {}'.format(resp.url))
		except Exception,e:
			pass

	def readme(self,plugin):
		try:
			ch = ['readme.txt','readme.md','README.md','README.txt']
			for pt in ch:
				path = '/wp-content/plugins/{}/{}'.format(plugin,pt)
				url = wpplugin.chk.path(self.url,path)
				resp = self.req.send(url,c=self.cookie)
				if resp.status_code == 200 and resp.content != None:
					if resp.url == url:
						wpplugin.out.more('Readme: {}'.format(resp.url))
						exit()
		except Exception,e:
			pass

	def dbwpscan(self,plugin):
		try:
			url = "https://www.wpvulndb.com/api/v2/plugins/{}".format(plugin)
			resp = requests.packages.urllib3.disable_warnings()
			resp = requests.get(url,headers={'user-agent':self.agent},verify=False)
			js = json.loads(resp._content,'UTF-8')
			if js[plugin]:
				if js[plugin]['vulnerabilities']:
					for x in xrange(len(js[plugin]['vulnerabilities'])):
						wpplugin.out.more('Title: {}'.format(js[plugin]['vulnerabilities'][x]['title']))
						if js[plugin]['vulnerabilities'][x]['references']['url']:
							for y in range(len(js[plugin]['vulnerabilities'][x]['references']['url'])):
								wpplugin.out.more('Reference: {}'.format(js[plugin]['vulnerabilities'][x]['references']['url'][y]))
						wpplugin.out.more('Fixed in: {}'.format(js[plugin]['vulnerabilities'][x]['fixed_in']))
				elif not js[plugin]['vulnerabilities']:
					wpplugin.out.more('Not found vulnerabilities')
			elif not js[plugin]:
				wpplugin.out.more('Not found vulnerabilities')
		except Exception,e:
			pass
