#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

import re
from lib import wpprint

class wpserver:
	def run(self,headers):
		server = ""
		try:
			for item in headers.items():
				if re.search(r'server',item[0],re.I): server = item[1]
			if server != "":
				wpprint.wpprint().plus('Server: {}'.format(server))
		except Exception,e:
			pass