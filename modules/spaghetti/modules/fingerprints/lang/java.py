#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Java():
	@staticmethod	
	def Run(content,headers):
		_ = False
		try:
			for item in headers.items():
				_ = re.search(r'Java|Servlet|JSP|JBoss|Glassfish|Oracle|JRE|JDK|JSESSIONID',str(item)) is not None
				if _:
					return "Java"
					break
		except Exception,ERROR:
			print ERROR