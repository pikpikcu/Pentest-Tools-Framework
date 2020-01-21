#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import aspx_mvc
import cakephp
import cherry
import django
import nette
import rack
import rails
import symfony

def Framework(headers):
	return (
		aspx_mvc.Aspxmvc().Run(headers),
		cakephp.Cakephp().Run(headers),
		cherry.Cherry().Run(headers),
		django.Django().Run(headers),
		nette.Nette().Run(headers),
		rack.Rack().Run(headers),
		rails.Rails().Run(headers),
		symfony.Symfony().Run(headers)
		)