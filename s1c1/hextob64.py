from base64 import b64encode


def hextob64(hex: str) -> str:
    hex_bytes = bytes.fromhex(hex)
    b64 = b64encode(hex_bytes)
    return b64.decode()
