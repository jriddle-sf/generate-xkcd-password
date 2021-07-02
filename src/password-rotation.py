#!/usr/bin/env python3

import crypt
import os
import json
from xkcdpass import xkcd_password

def __generateCuratedWordlist():
    full_wordlist = xkcd_password.locate_wordfile()
    curated_wordlist = xkcd_password.generate_wordlist(
            wordfile=full_wordlist,
            min_length=4,
            max_length=9)
    return curated_wordlist

def __generatePassword():
    password = xkcd_password.generate_xkcdpassword(
        __generateCuratedWordlist(),
        delimiter="-",
        case='first')
    password = password.rstrip()
    return password

def __generateHashWithSalt(password):
    salted_hash = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))
    return salted_hash

def __serializeSecretsAsJSON(password, salted_hash):
    secrets = {}
    secrets['password'] = password
    secrets['hash'] = salted_hash
    serialized_secrets = json.dumps(secrets)
    return serialized_secrets

def main():
    password = __generatePassword()
    salted_hash = __generateHashWithSalt(password)
    secrets = __serializeSecretsAsJSON(password,salted_hash)
    print(secrets)

main()
