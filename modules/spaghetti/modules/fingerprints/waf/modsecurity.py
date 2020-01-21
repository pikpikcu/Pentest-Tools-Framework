#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Modsecurity():
    @staticmethod
    def Run(headers):
        _ = False
        try:
            for item in headers.items():
                _ = re.search(r'Mod_Security|NOYB',item[1],re.I) is not None
                if _:
                    return "ModSecurity Web Application Firewall (Trustwave)"
                    break
        except Exception,ERROR:
            print ERROR