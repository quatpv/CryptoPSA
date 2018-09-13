import random
import hashlib
import base64
import os

proof = base64.b64encode(os.urandom(9))
test = raw_input("Proof of work: ")
ha = hashlib.sha1()
ha.update(test)
if test[0:12] == proof or ha.digest().endswith('\x00\x00\x00'):
	print "[+] Flag: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
else:	
	print "Bad proof of work."