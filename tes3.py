import hashlib
from ecdsa import SigningKey, SECP256k1

def private_key_to_public_key(private_key_hex: str) -> str:
    private_key_bytes = bytes.fromhex(private_key_hex)
    signing_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    verifying_key = signing_key.verifying_key
    public_key_bytes = b'\x04' + verifying_key.to_string()
    public_key_hex = public_key_bytes.hex()
    
    return public_key_hex

def compress_public_key(public_key_hex: str) -> str:
    public_key_bytes = bytes.fromhex(public_key_hex)
    x = public_key_bytes[1:33]  
    y = public_key_bytes[33:]  
    if y[-1] % 2 == 0:
        prefix = b'\x02' 
    else:
        prefix = b'\x03'  
    
    # Compressed public key format: prefix + x-coordinate
    compressed_public_key = prefix + x
    compressed_public_key_hex = compressed_public_key.hex()
    
    return compressed_public_key_hex

# Example usage
private_key_hex = ""
public_key = private_key_to_public_key(private_key_hex)
compressed_public_key = compress_public_key(public_key)

print("Uncompressed Public Key:", public_key)
print("Compressed Public Key:", compressed_public_key)
