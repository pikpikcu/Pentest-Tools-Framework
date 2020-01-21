#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Ruby():
	@staticmethod	
	def Run(content,headers):
		_ = False
		try:
			for item in headers.items():
				_ = re.search(r"mod_rack|phusion|passenger",item[1],re.I) is not None
				_ |= re.search(r'(.rb")',content) is not None
				if _:
					return "Ruby"
					break
		except Exception,ERROR:
			print ERROR