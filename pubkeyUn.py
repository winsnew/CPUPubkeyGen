# start_private_key = "0000000000000000000000000000000000000000000000000000000000000000"
# private_key_range = 10000000000000000:fffffffffffffffff

import os
from ecdsa import SigningKey, SECP256k1
import hashlib
import binascii

def hash160(pubkey):
    sha = hashlib.sha256()
    ripemd = hashlib.new('ripemd160')
    sha.update(pubkey)
    ripemd.update(sha.digest())
    return ripemd.digest()

# Checking hash
def check_public_key_hash(private_key, target_hash):
    sk = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1)
    vk = sk.verifying_key
    public_key = b'\x04' + vk.to_string()  
    pubkey_hash = hash160(public_key)
    return pubkey_hash.hex() == target_hash

# Range private key 
start_private_key_hex = "0000000000000000000000000000000000000000000000000000000000000000"
end_private_key_hex = "7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

# Target public key hash 
target_hash = "739437bb3dd6d1983e66629c5f08c70e52769371"

# Konversi range private key to int
start_int = int(start_private_key_hex, 16)
end_int = int(end_private_key_hex, 16)

# Init Variable
found = False
private_key_int = start_int

# search active
while private_key_int <= end_int and not found:
    private_key_hex = format(private_key_int, '064x')
    print(f"Testing private key: {private_key_hex}")
    if check_public_key_hash(private_key_hex, target_hash):
        print(f"Matching private key: {private_key_hex}")
        found = True
    private_key_int += 1

# n0t found
if not found:
    print("No matching private key found within the given range.")
