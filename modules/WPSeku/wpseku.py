#/usr/bin/env python
# -*- Coding: UTF-8 -*-

import os
import sys
import time
import getopt

from lib import wphttp
from lib import wpcolor
from lib import wpprint

from urlparse import urlsplit
from modules.fingerprint import fingerprint
from modules.discovery import discovery 
from modules.bruteforce import wpxmlrpc

RED = wpcolor.wpcolor().red(1)
WHITE = wpcolor.wpcolor().white(0)
YELLOW = wpcolor.wpcolor().yellow(4)
RESET = wpcolor.wpcolor().reset()

class WPSeku(object):
	out = wpprint.wpprint()
	def banner(self):
		print
	def usage(self,ext=False):
		path = os.path.basename(sys.argv[0])
		self.banner()
		print "Usage: {} [options]\n".format(path)
		print "\t-t --target\tTarget URL (eg: http://site.com)"
		print "\t-b --brute\tBruteforce login via xmlrpc"
		print "\t-u --user\tSet username, (df=admin)"
		print "\t-p --proxy\tSet proxy, (host:port)"
		print "\t-c --cookie\tSet cookie, (--cookie=\"COOKIE\")"
		print "\t-a --agent\tSet user-agent, (--agent=\"AGENT\")"
		print "\t-r --ragent\tSet random user-agent"
		print "\t-f --redirect\tRedirect target url, (df=true)"
		print "\t-m --timeout\tSet timeout, (df=None)"
		print "\t-w --wordlist\tSet wordlist, (df=db/wordlist.txt)"
		print "\t-h --help\tShow this help and exit\n"
		print "Examples:"
		print "\t{} -t http://site.com".format(path)
		print "\t{} -t http://site.com -b -w wlist.txt".format(path)
		print "\t{} -t http://site.com/wordpress/ --redirect".format(path)
		print "\t{} -t http://site.com -b -u test -w wlist.txt\n".format(path)
		if ext:
			exit()

	brute = False
	user = "admin"
	cookie = None
	agent = "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"
	redirect = True
	wordlist = "db/wordlist.txt"
	proxy = None
	timeout = None

	def main(self,kw):
		if len(sys.argv) <= 2:
			self.usage(True)
		try:
			opts,args = getopt.getopt(kw,"t:u:p:c:a:m:w:frbh:",["target=","brute",
				"user=","proxy=","cookie=","timeout=","agent=","ragent","redirect","wordlist=","help"]
				)
		except getopt.error,e:
			self.usage(True)
		for opt,arg in opts:
			if opt in ('-t','--target'):
				self.target = self.check(arg)
			if opt in ('-b','--brute'):
				self.brute = True
			if opt in ('-u','--user'):
				self.user = arg
			if opt in ('-p','--proxy'):
				self.proxy = arg
			if opt in ('-c','--cookie'):
				self.cookie = arg
			if opt in ('-a','--agent'):
				self.agent = arg
			if opt in ('-r','--ragent'):
				pass
			if opt in ('-m','--timeout'):
				self.timeout = arg
			if opt in ('-f','--redirect'):
				self.redirect = False
			if opt in ('-w','--wordlist'):
				self.wordlist = arg
			if opt in ('-h','--help'):
				self.usage(True)
		# starting 
		self.init()
		if self.brute == True:
			wpxmlrpc.wpxmlrpc(agent=self.agent,proxy=self.proxy,
				redir=self.redirect,time=self.timeout,url=self.target,
				cookie=self.cookie,wlist=self.wordlist,user=self.user).run()
			exit()
		# fingerprint 
		fingerprint.fingerprint(agent=self.agent,proxy=self.proxy,
			redir=self.redirect,time=self.timeout,url=self.target,
			cookie=self.cookie).run()
		# discovery
		discovery.discovery().run(agent=self.agent,proxy=self.proxy,
			redir=self.redirect,time=self.timeout,url=self.target,
			cookie=self.cookie)

	def check(self,url):
		o = urlsplit(url)
		u = ''
		if o.netloc == '':
			u = 'http://{}'.format(o.path)
		else:
			u = '{}://{}{}'.format(o.scheme,o.netloc,o.path)
		if urlsplit(u).scheme not in ['http','https']:
			self.banner()
			exit(WPSeku.out.warning('Scheme \"{}\" not support\n'.format(urlsplit(u).scheme)))
		return str(u)

	def init(self):
		self.banner()
		WPSeku.out.plus('Target: {}'.format(self.target))
		WPSeku.out.plus('Starting: {}\n'.format(time.strftime('%d/%m/%Y %H:%M:%S')))

if __name__ == "__main__":
	try:
		WPSeku().main(sys.argv[1:])
	except KeyboardInterrupt:
		exit(wpprint.wpprint().warning('Keyboard interrupt by user'))
