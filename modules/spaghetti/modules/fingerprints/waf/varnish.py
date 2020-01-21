#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Varnish():
    @staticmethod
    def Run(headers):
        _ = False
        try:
            for item in headers.items():
                _  = re.search(r'X-Varnish',item[0],re.I) is not None
                _ |= re.search(r'varnish*',item[1],re.I) is not None
                if _:
                    return "Varnish FireWall (OWASP)"
                    break
        except Exception,ERROR:
            print ERROR