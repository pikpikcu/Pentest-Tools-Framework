#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Joomla():
	@staticmethod	
	def Run(content):
		_ = False
		try:
			_ = re.search(r'/index.php?option=(\S*)|<meta name="generator" content="Joomla*|Powered by <a href="http://www.joomla.org">Joomla!</a>*',content) is not None
			if _:
				if re.search('/templates/*',content,re.I):
					return "Joomla"
		except Exception,ERROR:
			print ERROR