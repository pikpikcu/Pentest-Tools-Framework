#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Solaris():
	@staticmethod	
	def Run(os):
		_ = False
		try:
			for item in os.items():
				_ = re.search(r'solaris|sunos|opensolaris|sparc64|sparc',str(item),re.I) is not None
				if _:
					return "Solaris"
					break
		except Exception,ERROR:
			print ERROR