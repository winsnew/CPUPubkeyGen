import hashlib
import base58

# with SHA-256 hash
def public_key_to_address(public_key_compressed):
    pubkey_bytes = bytes.fromhex(public_key_compressed)
    sha256_pubkey = hashlib.sha256(pubkey_bytes).digest()
    ripemd160 = hashlib.new('ripemd160', sha256_pubkey).digest()
    network_byte = b'\x00' + ripemd160
    checksum = hashlib.sha256(hashlib.sha256(network_byte).digest()).digest()[:4]

    address = network_byte + checksum
    
    bitcoin_address = base58.b58encode(address).decode('utf-8')
    
    return bitcoin_address

public_key_compressed = ""
btc_address = public_key_to_address(public_key_compressed)
print(f"Bitcoin Address: {btc_address}")
