#!/usr/bin/env python3

import crypt
import os
import json

def __generatePassword():
    xkcd_command = "xkcdpass --delimiter '-' --numwords '6' --case 'first'"
    stream = os.popen(xkcd_command)
    password_string = stream.read()
    password_string = password_string.rstrip()
    return password_string

def __generateHashWithSalt(password_string):
    hash_with_salt = crypt.crypt(password_string, crypt.mksalt(crypt.METHOD_SHA512))
    return hash_with_salt

def __serializeSecrets(password_string, hash_with_salt):
    secrets = {}
    secrets['password'] = password_string
    secrets['hash'] = hash_with_salt
    serialized_secrets = json.dumps(secrets)
    return serialized_secrets

def main():
    new_password = __generatePassword()
    new_hash = __generateHashWithSalt(new_password)
    new_secrets = __serializeSecrets(new_password,new_hash)
    print(new_secrets)

main()
