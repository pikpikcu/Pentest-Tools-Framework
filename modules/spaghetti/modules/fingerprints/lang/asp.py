#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Asp():
	@staticmethod	
	def Run(content,headers):
		_ = False
		try:
			for item in headers.items():
				_ = re.search('ASP.NET|X-AspNet-Version|x-aspnetmvc-version',str(item),re.I) is not None
				_ |= re.search(r'(__VIEWSTATE\W*)',content) is not None
				_ |= re.search(r'(.asp"|.aspx")',content) is not None
				if _:
					return "ASP.NET"
					break
		except Exception,ERROR:
			print ERROR