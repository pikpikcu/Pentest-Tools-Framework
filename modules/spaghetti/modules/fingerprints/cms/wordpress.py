#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Wordpress():
	@staticmethod	
	def Run(content):
		_ = False
		try:
			for x in ('/wp-admin/','/wp-content/','/wp-includes/','<meta name="generator" content="WordPress'):
				_ = re.search(x,content) is not None
				if _:
					return "Wordpress"
					break
		except Exception,ERROR:
			print ERROR