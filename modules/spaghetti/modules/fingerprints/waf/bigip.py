#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Bigip():
    @staticmethod
    def Run(headers):
        _ = False
        try:
            for item in headers.items():
                _  = re.search(r'BigIP|BIGipServer',item[1],re.I) is not None
                _ |= re.search(r'TS\w{4,}=',item[1],re.I) is not None
                if _: 
                    return "BIG-IP Application Security Manager (F5 Networks)"
                    break
        except Exception,ERROR:
            print ERROR