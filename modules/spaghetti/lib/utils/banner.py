#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import color
import os
import sys
import time
import printer
import socket

r = color.colors().red(1)
e = color.colors().end()
b = color.colors().blue(1)
g = color.colors().green(1)
y = color.colors().yellow(1)
ny = color.colors().yellow(0)
w = color.colors().white(3)
name = os.path.join(os.path.basename(sys.argv[0]))

def strftime(target):
	printer.Printer().plus("Target: %s"%target)
	if 'http://' in target:
		t = "%s"%target.split('http://')[1]
	else:
		t = "%s"%target.split('https://')[1]
	try:
		printer.Printer().plus('IP: %s'%socket.gethostbyaddr('%s'%t)[2][0])
	except socket.error:
		printer.Printer().plus('IP: Host name lookup failure')
	printer.Printer().plus("Starting: %s\n"%time.strftime('%d/%m/%Y %H:%M:%S'))

def banner():
	print(r+" _____             _       _   _   _ "+e)
	print(r+"|   __|___ ___ ___| |_ ___| |_| |_|_|"+e)
	print(r+"|__   | . | .'| . |   | -_|  _|  _| |"+e)
	print(r+"|_____|  _|__,|_  |_|_|___|_| |_| |_|"+e)
	print(r+"      |_|     |___|           "+y+"v0.1.0\n"+e)
	print(w+"|| Spaghetti - Web Application Security Scanner"+e)
	print(w+"|| Codename - "+y+"\"Pasta\""+e)
	print(w+"|| Momo Outaadi (M4ll0k)"+e)
	print(w+"|| "+ny+"https://github.com/m4ll0k/Spaghetti\n"+e)

def Usage(exit=False):
	banner()
	print("Usage: %s -u/--url examples.com -s/--scan [0-3]\n"%name)
	print(" -u --url\tTarget URL (eg: http://examples.com)")
	print(" -s --scan\tScan Option:\n")
	print("\t 0:\tFull Scan")
	print("\t 1:\tAdministrative Console")
	print("\t 2:\tMisconfiguration / Default File")
	print("\t 3:\tInformation Disclosure\n")
	print(" --agent\tSet user-agent")
	print(" --random-agent\tRandom user-agent")
	print(" --cookie\tSet cookies, default=None")
	print(" --redirect\tRedirect target URL, default=True")
	print(" --proxy\tSet proxy, (host:port)")
	print(" --help\t\tShow this help and exit\n")
	print("Examples:")
	print("\t%s --url http://site.com --scan [0-3]\n" % name)
	if exit:
		sys.exit(0)
