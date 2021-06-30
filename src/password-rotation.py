#!/usr/bin/env python3

import crypt
import os

# To Do: Use the xkcdpass library versus calling it from the command line.
xkcd_command = 'xkcdpass --numwords \'6\' --case \'first\''

stream = os.popen(xkcd_command)
output = stream.read()

new_password = output
new_hash = crypt.crypt(new_password, crypt.mksalt(crypt.METHOD_SHA512))

print("Password: " + new_password)
print("Hash: " + new_hash)
