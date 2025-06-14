import struct

def jayden_hash_ultra(data: str) -> str:
    # Convert to bytes
    data_bytes = data.encode('utf-8')

    # Pad to a multiple of 8 bytes
    while len(data_bytes) % 8 != 0:
        data_bytes += b'\x00'

    # Initialize 64-bit state (like SHA-256 but small)
    state = [0x123456789ABCDEF0, 0x0FEDCBA987654321]

    # Some random-looking round constants
    constants = [0x243F6A8885A308D3, 0x13198A2E03707344,
                 0xA4093822299F31D0, 0x082EFA98EC4E6C89]

    # Process input in 8-byte blocks
    for i in range(0, len(data_bytes), 8):
        block = struct.unpack("<Q", data_bytes[i:i+8])[0]  # 64-bit little-endian

        for r in range(4):  # 4 rounds of mixing
            state[0] ^= (block + constants[r]) & 0xFFFFFFFFFFFFFFFF
            state[0] = ((state[0] << 13) | (state[0] >> (64 - 13))) & 0xFFFFFFFFFFFFFFFF
            state[1] ^= (state[0] + block) & 0xFFFFFFFFFFFFFFFF
            state[1] = ((state[1] << 17) | (state[1] >> (64 - 17))) & 0xFFFFFFFFFFFFFFFF
            state[0] = (state[0] + state[1]) & 0xFFFFFFFFFFFFFFFF
            state[1] = (state[1] ^ constants[r]) & 0xFFFFFFFFFFFFFFFF

    # Combine into a final hash string
    final_hash = f"{state[0]:016X}{state[1]:016X}"
    return final_hash
    
password = "Password Test 12345"
hashed = jayden_hash_ultra(password)
print("Password:", password)
print("JHA-64:", hashed)
