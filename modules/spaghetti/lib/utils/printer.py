#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import color

class Printer():
	R = color.colors().red(1) #red
	NR = color.colors().red(0) # normal red
	G = color.colors().green(1) # green
	Y = color.colors().yellow(1) # yellow
	B = color.colors().blue(1) # blue
	W = color.colors().white(0) # white
	E = color.colors().end() # reset

	def plus(self,string,flag="+"):
		print("{}[{}]{} {}{}{}".format(Printer.G,flag,Printer.E,Printer.W,string,Printer.E))
	
	def less(self,string,flag="-"):
		print("{}[{}]{} {}{}{}".format(Printer.R,flag,Printer.E,Printer.W,string,Printer.E))
	
	def error(self,string,flag="!"):
		print("{}[{}]{} {}{}".format(Printer.R,flag,Printer.E,Printer.NR,string,Printer.E))
	
	def test(self,string,flag="*"):
		print("{}[{}]{} {}{}{}".format(Printer.B,flag,Printer.E,Printer.W,string,Printer.E))
	
	def info(self,string,color='G',flag="|"):
		if color=='G':
			print(" {}{}{} {}{}{}".format(Printer.G,flag,Printer.E,Printer.W,string,Printer.E))
		else:
			print(" {}{}{} {}{}{}".format(Printer.R,flag,Printer.E,Printer.W,string,Printer.E))