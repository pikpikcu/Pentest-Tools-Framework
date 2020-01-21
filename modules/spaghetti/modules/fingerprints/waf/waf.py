#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import aws
import baidu
import barracuda
import bigip
import binarysec
import cloudflare
import cloudfront
import dotdefender
import edgecast
import incapsula
import modsecurity
import profense
import radware
import paloalto
import sucuri
import urlscan
import varnish
import webknight

def Waf(headers):
	return (
		aws.Aws().Run(headers),
		baidu.Baidu().Run(headers),
		barracuda.Barracuda().Run(headers),
		bigip.Bigip().Run(headers),
		binarysec.Binarysec().Run(headers),
		cloudflare.Cloudflare().Run(headers),
		cloudfront.Cloudfront().Run(headers),
		dotdefender.Dotdefender().Run(headers),
		edgecast.Edgecast().Run(headers),
		paloalto.Paloalto().Run(headers),
		incapsula.Incapsula().Run(headers),
		modsecurity.Modsecurity().Run(headers),
		profense.Profense().Run(headers),
		radware.Radware().Run(headers),
		sucuri.Sucuri().Run(headers),
		urlscan.Urlscan().Run(headers),
		varnish.Varnish().Run(headers),
		webknight.Webknight().Run(headers)
		)