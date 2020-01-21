#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

from lib import wpprint

class wpheaders:
	def run(self,headers):
		fields = ('Accept',
				  'Accept-Charset',
				  'Accept-Encoding',
				  'Accept-Language',
				  'Accept-Datetime',
				  'Authorization',
				  'Connection',
				  'Cookie',
				  'Content-Length',
				  'Content-MD5',
				  'Content-Type',
				  'Expect',
				  'From',
				  'Host',
				  'If-Match',
				  'If-Modified-Since',
				  'If-None-Match',
				  'If-Range',
				  'If-Unmodified-Since',
				  'Max-Forwards',
				  'Origin',
				  'Pragma',
				  'Proxy-Authorization',
				  'Range',
				  'Referer',
				  'User-Agent',
				  'Upgrade',
				  'Via',
				  'Warning',
				  'X-Requested-With',
				  'X-Forwarded-For',
				  'X-Forwarded-Host',
				  'X-Forwarded-Proto',
				  'Front-End-Https',
				  'X-Http-Method-Override',
				  'X-ATT-DeviceId',
				  'X-Wap-Profile',
				  'Proxy-Connection',
				  'Accept-Ranges',
				  'Age',
				  'Allow',
				  'Cache-Control',
				  'Content-Encoding',
				  'Content-Language',
				  'Content-Length',
				  'Content-Location',
				  'Content-MD5',
				  'Content-Disposition',
				  'Content-Range',
				  'Content-Type',
				  'Date',
				  'ETag',
				  'Expires',
				  'Last-Modified',
				  'Link',
				  'Location',
				  'Proxy-Authenticate',
				  'Refresh',
				  'Retry-After',
				  'Server',
				  'Set-Cookie',
				  'Status',
				  'Strict-Transport-Security',
				  'Trailer',
				  'Transfer-Encoding',
				  'Vary',
				  'WWW-Authenticate',
				  'X-Frame-Options',
				  'Public-Key-Pins',
				  'X-XSS-Protection',
				  'Content-Security-Policy',
				  'X-Content-Security-Policy',
				  'X-WebKit-CSP',
				  'X-Content-Type-Options',
				  'X-Powered-By',
				  'Keep-Alive',
				  'Content-language',
				  'X-UA-Compatible'
				  )
		try:
			for key in headers.keys():
				if key not in fields:
					wpprint.wpprint().plus('Uncommon header "%s" found, with contents: %s'%(key,headers[key]))
		except Exception,e:
			pass