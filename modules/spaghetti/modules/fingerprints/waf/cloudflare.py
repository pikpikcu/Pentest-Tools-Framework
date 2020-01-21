#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Cloudflare():    
    @staticmethod
    def Run(headers):
        _ = False
        try:
            for item in headers.items():
                _  = re.search(r'cloudflare[-nginx]',item[1],re.I) is not None
                _ |= re.search(r'__cfduid=',item[1],re.I) is not None
                _ |= re.search(r'cf-ray',item[0],re.I) is not None
                if _: 
                    return "CloudFlare Web Application Firewall (CloudFlare)"
                    break
        except Exception,Error:
            print Error