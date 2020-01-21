#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Mac():
	@staticmethod	
	def Run(os):
		_ = False
		try:
			for item in os.items():
				_  = re.search(r'Mac|MacOS|MacOS\S*',str(item)) is not None
				if _:
					return "MacOS"
					break
		except Exception,ERROR:
			print ERROR