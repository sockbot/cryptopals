def get_xor(buffer1: bytes, buffer2: bytes) -> bytes:
    if len(buffer1) != len(buffer2):
        raise ValueError("Input buffers must be of equal size.")

    return bytes([bit1 ^ bit2 for bit1, bit2 in zip(buffer1, buffer2)])
