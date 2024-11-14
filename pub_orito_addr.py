import hashlib
import base58

def public_key_to_address(public_key):
    sha256_hash = hashlib.sha256(public_key.encode('utf-8')).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    prefix = b'\x00' 
    prefixed_hash = prefix + ripemd160_hash
    checksum = hashlib.sha256(hashlib.sha256(prefixed_hash).digest()).digest()[:4]
    address_bytes = prefixed_hash + checksum
    address = base58.b58encode(address_bytes)
    
    return address.decode('utf-8')

public_key = ""

btc_address = public_key_to_address(public_key)

print("Alamat Bitcoin:", btc_address)
