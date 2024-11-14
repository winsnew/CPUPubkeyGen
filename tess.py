import binascii
from ecdsa import SECP256k1, VerifyingKey

def get_uncompressed_pubkey(scriptsig_hex):
    pubkey_hex = scriptsig_hex[-66:]
    pubkey_bytes = binascii.unhexlify(pubkey_hex)
    vk = VerifyingKey.from_string(pubkey_bytes, curve=SECP256k1)
    uncompressed_pubkey = vk.to_string("uncompressed")
    uncompressed_pubkey_hex = binascii.hexlify(uncompressed_pubkey).decode('ascii')
    
    return "04" + uncompressed_pubkey_hex

scriptsig_hex = ""

uncompressed_pubkey = get_uncompressed_pubkey(scriptsig_hex)

print("Uncompressed Public Key:")
print(uncompressed_pubkey)
