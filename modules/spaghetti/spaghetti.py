#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

from lib.utils import banner
from lib.net import utils
from modules.discovery import All
from modules.fingerprints import CheckAll
import sys
import getopt

class Spaghetti(object):
	parse = utils.Parser()
	redirect = True
	proxy = None 
	agent = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
	cookie = None
	def Main(self,argv):
		if len(sys.argv) <= 4:
			banner.Usage(True)
		try:
			opts,args = getopt.getopt(argv,'u:s:',['url=','scan=','agent=','random-agent','cookie=','proxy=','redirect=','help='])
		except getopt.error:
			banner.Usage(True)
		for o,a in opts:
			if o in ('-u','--url'):
				self.target = self.parse.ParserUrl(a)
			if o in ('-s','--scan'):
				self.scan = a 
			if o in ('--agent'):
				self.agent = a 
			if o in ('--random-agent'):
				pass
			if o in ('--cookie'):
				self.cookie = a 
			if o in ('--proxy'):
				self.proxy = a
			if o in ('--redirect'):
				self.redirect = a
			if o in ('--help'):
				banner.Usage(True)
		banner.banner()
		banner.strftime(self.target)
		CheckAll.CheckAll(self.target,self.agent,self.proxy,self.redirect).Run()
		if self.scan == '0':
			All.All(self.target,self.agent,self.proxy,self.redirect)
		elif self.scan == '1':
			All.AdminInterface(self.target,self.agent,self.proxy,self.redirect)
		elif self.scan == '2':
			All.Misconfiguration(self.target,self.agent,self.proxy,self.redirect)
		elif self.scan == '3':
			All.InfoDisclosure(self.target,self.agent,self.proxy,self.redirect)
if __name__ == "__main__":
	try:
		Spaghetti().Main(sys.argv[1:])
	except KeyboardInterrupt:
		sys.exit('[!] Keyboard Interrupt...')
