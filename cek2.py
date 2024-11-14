import hashlib
import base58
import ecdsa
from binascii import unhexlify, hexlify

def public_key_to_address(public_key_hex):
    public_key_bytes = bytes.fromhex(public_key_hex)
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    public_key_hash = ripemd160.digest()
    versioned_key_hash = b'\x00' + public_key_hash
    checksum = hashlib.sha256(hashlib.sha256(versioned_key_hash).digest()).digest()[:4]
    binary_address = versioned_key_hash + checksum
    address = base58.b58encode(binary_address).decode('utf-8')
    
    return address

def compress_pubkey(pubkey_bytes):
    x = int(pubkey_bytes[1:33].hex(), 16)
    y = int(pubkey_bytes[33:].hex(), 16)
    prefix = b'\x02' if y % 2 == 0 else b'\x03'
    compressed_pubkey = prefix + x.to_bytes(32, 'big')
    return hexlify(compressed_pubkey).decode()

def point_addition(pubkey_hex, n=1):
    pubkey_bytes = unhexlify(pubkey_hex)
    curve = ecdsa.SECP256k1.curve

    # Check compress / uncompress pubkey
    if pubkey_bytes[0] == 0x04:  
        x = int(pubkey_bytes[1:33].hex(), 16)
        y = int(pubkey_bytes[33:].hex(), 16)
    elif pubkey_bytes[0] in [0x02, 0x03]: 
        x = int(pubkey_bytes[1:].hex(), 16)
        curve_p = curve.p()
        x2 = (x**3 + 7) % curve_p
        y = pow(x2, (curve_p + 1) // 4, curve_p)
        if y % 2 != pubkey_bytes[0] % 2:
            y = curve_p - y
    else:
        raise ValueError("Invalid public key format")

    point = ecdsa.ellipticcurve.Point(curve, x, y)
    generator = ecdsa.SECP256k1.generator
    new_point = point + n * generator
    new_pubkey = b'\x04' + new_point.x().to_bytes(32, 'big') + new_point.y().to_bytes(32, 'big')
    
    return hexlify(new_pubkey).decode()

def search_for_matching_address(start_pubkey, target_address, max_iterations=100000):
    pubkey_hex = start_pubkey
    for i in range(max_iterations):
        # Generate addr
        calculated_address = public_key_to_address(pubkey_hex)
        # Check if the address matches the target address
        if calculated_address == target_address:
            print(f"Found matching address after {i+1} iterations!")
            print(f"Public Key: {pubkey_hex}")
            return pubkey_hex
        
        # Add one more point to the public key 
        pubkey_hex = point_addition(pubkey_hex, 1)
        
    print("No matching address found within the given iterations.")
    return None

target_address = ""
initial_pubkey_hex = ""

# Searchingg
matching_pubkey = search_for_matching_address(initial_pubkey_hex, target_address)

if matching_pubkey:
    print(f"Matching Public Key: {matching_pubkey}")
else:
    print("No match found.")
