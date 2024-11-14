import hashlib
import base58

 # Remove '04' prefix if present
def public_key_to_btc_address(public_key):
    if public_key.startswith('04'):
        public_key = public_key[2:]
    public_key_bytes = bytes.fromhex(public_key)
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    versioned_hash = b'\x00' + ripemd160_hash
    hash_1 = hashlib.sha256(versioned_hash).digest()
    hash_2 = hashlib.sha256(hash_1).digest()

    checksum = hash_2[:4]

    binary_address = versioned_hash + checksum
    btc_address = base58.b58encode(binary_address).decode('utf-8')
    return btc_address

uncompressed_key = ""

btc_address = public_key_to_btc_address(uncompressed_key)
print("Bitcoin address:")
print(btc_address)
