#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Binarysec():
    @staticmethod
    def Run(headers):
        _ = False
        try:
            for item in headers.items():
                _  = re.search(r'BinarySec',item[1],re.I) is not None
                _ |= re.search(r'x-binarysec-[via|nocahe]',item[0],re.I) is not None
                if _: 
                    return "BinarySEC Web Application Firewall (BinarySEC)"
                    break
        except Exception,ERROR:
            print ERROR