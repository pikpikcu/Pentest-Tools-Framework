#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Php():
	@staticmethod	
	def Run(content,headers):
		_ = False
		try:
			for item in headers.items():
				_  = re.search(r'X-PHP-PID|PHP\S*|PHPSESSID',str(item)) is not None
				_ |= re.search(r'(.php")',content) is not None
				if _:
					return "PHP"
					break
		except Exception,ERROR:
			print ERROR