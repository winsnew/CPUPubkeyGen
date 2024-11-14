from ecdsa import SECP256k1, SigningKey
import binascii

# min_private_key = 0x10000000000000000
# max_private_key = 0xffffffffffffffff

def get_public_key(private_key_int):
    private_key_bytes = private_key_int.to_bytes(32, 'big')
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    public_key = sk.verifying_key
    
    # public key (hex format)
    uncompressed_public_key = b"04" + public_key.to_string()
    uncompressed_public_key_hex = binascii.hexlify(uncompressed_public_key).decode()
    # Compressed public key 
    public_key_bytes = public_key.to_string()
    prefix = b"\x02" if public_key_bytes[32] % 2 == 0 else b"\x03"
    compressed_public_key = prefix + public_key_bytes[:32]
    compressed_public_key_hex = binascii.hexlify(compressed_public_key).decode()

    return uncompressed_public_key_hex, compressed_public_key_hex

print(f"Private Key Range: {hex(min_private_key)} to {hex(max_private_key)}")
print("\nTesting with sample private keys in the range:\n")

test_keys = [min_private_key, (min_private_key + max_private_key) // 2, max_private_key]

for private_key_int in test_keys:
    private_key_hex = hex(private_key_int)
    uncompressed_public_key_hex, compressed_public_key_hex = get_public_key(private_key_int)
    
    print(f"Private Key (Hex): {private_key_hex}")
    print(f"Uncompressed Public Key (Hex): {uncompressed_public_key_hex}")
    print(f"Compressed Public Key (Hex): {compressed_public_key_hex}")
    print("-" * 80)
