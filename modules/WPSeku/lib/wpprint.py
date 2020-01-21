#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

import wpcolor

class wpprint:

	r = wpcolor.wpcolor().red(0)
	g = wpcolor.wpcolor().green(0)
	y = wpcolor.wpcolor().yellow(0)
	b = wpcolor.wpcolor().blue(0)
	w = wpcolor.wpcolor().white(0)
	e = wpcolor.wpcolor().reset()

	def plus(self,string):
		print ("{}[+]{} {}{}{}".format(
			self.g,self.e,self.w,string,self.e)
		)

	def test(self,string):
		print ("{}[*]{} {}{}{}".format(
			self.b,self.e,self.w,string,self.e)
		)

	def warning(self,string):
		print ("{}[!]{} {}{}{}".format(
			self.r,self.e,self.w,string,self.e)
		)

	def info(self,string):
		print ("{}[i]{} {}{}{}".format(
			self.y,self.e,self.w,string,self.e)
		)

	def more(self,string):
		print (" {}|{}  {}{}{}".format(
			self.w,self.e,self.w,string,self.e)
		)
	def passs(self):
		print ("")