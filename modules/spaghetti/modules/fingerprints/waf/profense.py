#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Application Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import re

class Profense():
    @staticmethod
    def Run(headers):
        _ = False
        try:
            for item in headers.items():
                _ = re.search(r'PLBSID=',item[1],re.I) is not None
                _ = re.search(r'Profense',item[1],re.I) is not None
                if _:
                    return "Profense Web Application Firewall (Armorlogic)"
                    break 
        except Exception,ERROR:
            print ERROR