import os
import sys

# call using port.py 2> /dev/null
c = 'nc -zvw3 192.168.1.1 '
for i in range(1, 10000):
    if os.system(c + str(i)) == 0:
        print "XXXXXXXXXXXXXX", i

