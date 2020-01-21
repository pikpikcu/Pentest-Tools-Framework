#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import asp
import java
import php	
import python
import ruby

def Lang(content,headers):
	return (
		asp.Asp().Run(content,headers),
		java.Java().Run(content,headers),
		php.Php().Run(content,headers),
		python.Python().Run(content,headers),
		ruby.Ruby().Run(content,headers)
		)