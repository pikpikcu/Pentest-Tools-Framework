#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Rails():
	@staticmethod	
	def Run(headers):
		_ = False
		try:
			for item in headers.items():
				_ =  re.search(r'rails*|_rails_admin_session=*|x-rails',str(item),re.I) is not None
				if _:
					return "Rails"
					break
		except Exception,ERROR:
			pass
