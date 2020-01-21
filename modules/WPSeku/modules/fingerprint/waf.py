#/usr/bin/env python
# -*- Coding: UTF-8 -*-
#
# WPSeku: Wordpress Security Scanner
#
# @url: https://github.com/m4ll0k/WPSeku
# @author: Momo Outaadi (M4ll0k)

import re
from lib import wpprint

class wpwaf:
	def run(self,content):
		waf = ""
		try:
			if re.search('/wp-content/plugins/wordfence/',content):
				waf += "Wordfence Security"
			elif re.search('/wp-content/plugins/bulletproof-security/',content):
				waf += "BulletProof Security"
			elif re.search('/wp-content/plugins/sucuri-scanner/',content):
				waf += "Sucuri Security"
			elif re.search('/wp-content/plugins/better-wp-security/',content):
				waf += "Better WP Security"
			elif re.search('/wp-content/plugins/wp-security-scan/',content):
				waf += "Acunetix WP SecurityScan"
			elif re.search('/wp-content/plugins/all-in-one-wp-security-and-firewall/',content):
				waf += "All In One WP Security & Firewall"
			elif re.search('/wp-content/plugins/6scan-protection/',content):
				waf += "6Scan Security"
			if waf != "":
				wpprint.wpprint().plus('Detect firewall: {}'.format(waf))
		except Exception,e:
			pass