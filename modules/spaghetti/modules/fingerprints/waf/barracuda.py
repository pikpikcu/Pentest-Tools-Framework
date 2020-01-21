#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Barracuda():
	@staticmethod
	def Run(headers):
		_ = False
		try:
			for item in headers.items():
				_  = re.search(r'barracuda*',item[1],re.I) is not None
				_ |= re.search(r'barra_counter_session=',item[1],re.I) is not None
				_ |= re.search(r'barracuda_',item[1],re.I) is not None
				if _: 
					return "Barracuda Web Application Firewall (Barracuda Networks)"
					break
		except Exception,ERROR:
			print ERROR