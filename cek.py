import hashlib
import base58

def public_key_to_address(public_key_hex):
    # Decode 
    public_key_bytes = bytes.fromhex(public_key_hex)
    # SHA-256 hashing 
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    # RIPEMD-160 hashing on the SHA-256 
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    public_key_hash = ripemd160.digest()
    # Add version byte in front (0x00 for Mainnet)
    versioned_key_hash = b'\x00' + public_key_hash
    # SHA-256 twice on the extended RIPEMD-160 result
    checksum = hashlib.sha256(hashlib.sha256(versioned_key_hash).digest()).digest()[:4]
    binary_address = versioned_key_hash + checksum
    address = base58.b58encode(binary_address).decode('utf-8')
    
    return address


public_key_hex = ""
expected_address = ""


calculated_address = public_key_to_address(public_key_hex)

print("Calculated Address:", calculated_address)
print("Expected Address:", expected_address)
print("Match:", calculated_address == expected_address)
