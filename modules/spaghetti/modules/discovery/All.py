#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Spaghetti: Web Server Security Scanner
#
# @url: https://github.com/m4ll0k/Spaghetti
# @author: Momo Outaadi (M4ll0k)
# @license: See the file 'doc/LICENSE'

import AdminInterfaces
import AllowMethod
import ApacheUsers
import ApacheXss
import Backdoor
import Backup 
import Captcha
import ClientAccessPolicy
import CommonDirectory
import CommonFile
import Cookie
import HtmlObject 
import LDAPInjection
import ModStatus
import Email 
import MultiIndex
import PrivateIP 
import Robots

def All(url,agent,proxy,redirect):
	Cookie.Cookie(url,agent,proxy,redirect).Run()
	AllowMethod.AllowMethod(url,agent,proxy,redirect).Run()
	Robots.Robots(url,agent,proxy,redirect).Run()
	ClientAccessPolicy.ClientAccessPolicy(url,agent,proxy,redirect).Run()
	PrivateIP.PrivateIP(url,agent,proxy,redirect).Run()
	Email.Email(url,agent,proxy,redirect).Run()
	MultiIndex.MultiIndex(url,agent,proxy,redirect).Run()
	Captcha.Captcha(url,agent,proxy,redirect).Run()
	ApacheUsers.ApacheUsers(url,agent,proxy,redirect).Run()
	ApacheXss.ApacheXss(url,agent,proxy,redirect).Run()
	HtmlObject.HtmlObject(url,agent,proxy,redirect).Run()
	LDAPInjection.LDAPInjection(url,agent,proxy,redirect).Run()
	ModStatus.ModStatus(url,agent,proxy,redirect).Run()
	AdminInterfaces.AdminInterfaces(url,agent,proxy,redirect).Run()
	Backdoor.Backdoors(url,agent,proxy,redirect).Run()
	Backup.Backup(url,agent,proxy,redirect).Run()
	CommonDirectory.CommonDirectory(url,agent,proxy,redirect).Run()
	CommonFile.CommonFile(url,agent,proxy,redirect).Run()

def AdminInterface(url,agent,proxy,redirect):
	AdminInterfaces.AdminInterfaces(url,agent,proxy,redirect).Run()

def Misconfiguration(url,agent,proxy,redirect):
	MultiIndex.MultiIndex(url,agent,proxy,redirect).Run()
	ModStatus.ModStatus(url,agent,proxy,redirect).Run()
	Backdoor.Backdoors(url,agent,proxy,redirect).Run()
	Backup.Backup(url,agent,proxy,redirect).Run()
	CommonDirectory.CommonDirectory(url,agent,proxy,redirect).Run()
	CommonFile.CommonFile(url,agent,proxy,redirect).Run()


def InfoDisclosure(url,agent,proxy,redirect):
	Robots.Robots(url,agent,proxy,redirect).Run()
	ClientAccessPolicy.ClientAccessPolicy(url,agent,proxy,redirect).Run()
	PrivateIP.PrivateIP(url,agent,proxy,redirect).Run()
	Email.Email(url,agent,proxy,redirect).Run()

