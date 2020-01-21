#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

class colors():
	# red
	def red(self,number):
		return('\033[{};31m'.format(number))
	# green
	def green(self,number):
		return('\033[{};32m'.format(number))
	# yellow
	def yellow(self,number):
		return('\033[{};33m'.format(number))
	# blue
	def blue(self,number):
		return('\033[{};34m'.format(number))
	# white
	def white(self,number):
		return('\033[{};38m'.format(number))
	# end
	def end(self):
		return('\033[0m')