#!/usr/bin/env python3

import crypt
import os
import json

# To Do: Use the xkcdpass library versus calling it from the command line.
xkcd_command = "xkcdpass --delimiter '-' --numwords '6' --case 'first'"

stream = os.popen(xkcd_command)
output = stream.read()

new_password = output.rstrip()
new_hash = crypt.crypt(new_password, crypt.mksalt(crypt.METHOD_SHA512))

secrets = {}
secrets['password'] = new_password
secrets['hash'] = new_hash

data = json.dumps(secrets)

print(data)
