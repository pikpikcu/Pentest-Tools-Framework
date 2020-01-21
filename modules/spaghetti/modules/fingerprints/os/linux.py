#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Linux():
	@staticmethod	
	def Run(os):
		try:
			for item in os.items():
				_  = re.findall(r'linux|ubuntu|gentoo|debian|dotdeb|centos|redhat|sarge|etch|lenny|squeeze|wheezy|jessie|red hat|scientific linux',str(item),re.I)
				if _:
					if len(_)==2:return _[0]
					else: 
						return _[0]
					break
		except Exception,ERROR:
			print ERROR