import hashlib
from ecdsa import SigningKey, SECP256k1
import base58

def generate_bitcoin_address(private_key):
    # Generate public key
    sk = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1)
    public_key = sk.get_verifying_key().to_string()
    sha256_hash = hashlib.sha256(public_key).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    version_ripemd160 = b'\x00' + ripemd160_hash
    sha256_hash = hashlib.sha256(version_ripemd160).digest()
    sha256_hash_2 = hashlib.sha256(sha256_hash).digest()
    checksum = sha256_hash_2[:4]
    binary_address = version_ripemd160 + checksum
    base58_address = base58.b58encode(binary_address)
    
    return base58_address.decode()

# private key
start_private_key = ""

# private_key to integer
start_int = int(start_private_key, 16)

# range
range_start = ""
range_end = ""

# print addresses
for i in range(start_int, range_end + 1):
    private_key = format(i, '064x')
    address = generate_bitcoin_address(private_key)
    print(f"Private Key: {private_key}")
    print(f"Bitcoin Address: {address}")
    print()

    break

    # Opsii: looping condition take break (no updatess)
    # if i - start_int >= 1000:
    #     break
