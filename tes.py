def decode_scriptsig(hex_scriptsig):
    """Decode ScriptSig into its components: Signature and Public Key."""
    scriptsig = bytes.fromhex(hex_scriptsig)
    sig_len = scriptsig[0]
    signature = scriptsig[1:sig_len + 1]
    pubkey = scriptsig[sig_len + 2:]
    signature_hex = signature.hex()
    pubkey_hex = pubkey.hex()
    
    return signature_hex, pubkey_hex

scriptsig_hex = ""
signature, public_key = decode_scriptsig(scriptsig_hex)

print("Signature (hex):", signature)
print("Public Key (hex):", public_key)
