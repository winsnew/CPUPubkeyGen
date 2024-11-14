import hashlib
import base58

def public_key_hash_to_address(public_key_hash):
    network_byte = b'\x00' + public_key_hash
    checksum = hashlib.sha256(hashlib.sha256(network_byte).digest()).digest()[:4]
    address_bytes = network_byte + checksum
    bitcoin_address = base58.b58encode(address_bytes).decode('utf-8')
    
    return bitcoin_address


public_key_hash = bytes.fromhex("")

btc_address = public_key_hash_to_address(public_key_hash)
print(f"Bitcoin Address: {btc_address}")
