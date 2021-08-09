from base64 import b64encode


def main():
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    hex_bytes = bytes.fromhex(hex)
    b64 = b64encode(hex_bytes)
    print(b64.decode())


if __name__ == "__main__":
    main()
