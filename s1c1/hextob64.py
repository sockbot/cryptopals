from base64 import b64encode


def hextob64(hex: bytes) -> bytes:
    return b64encode(hex)
