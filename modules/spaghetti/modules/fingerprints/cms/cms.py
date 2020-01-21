#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import drupal
import joomla
import wordpress

def Cms(content):
	return (
		drupal.Drupal().Run(content),
		joomla.Joomla().Run(content),
		wordpress.Wordpress().Run(content)
		)
	