#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Rack():
	@staticmethod	
	def Run(headers):
		_ = False
		try:
			for item in headers.items():
				_ = re.search(r'mod_rack*|rack.session=*|x-rack|X-Rack-Cache',str(item),re.I) is not None 
				if _:
					return "Rack"
					break
		except Exception,ERROR:
			pass
