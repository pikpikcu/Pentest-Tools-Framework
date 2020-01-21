#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

class wpcolor:

	def red(self,num):
		return ("\x1b[{};31m").format(str(num))

	def green(self,num):
		return ("\x1b[{};32m").format(str(num))

	def yellow(self,num):
		return ("\x1b[{};33m").format(str(num))

	def blue(self,num):
		return ("\x1b[{};34m").format(str(num))

	def white(self,num):
		return ("\x1b[{};38m").format(str(num))

	def reset(self):
		return ("\x1b[0m")