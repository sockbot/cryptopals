from get_xor import get_xor


def test_get_xor():
    buffer1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    buffer2 = bytes.fromhex("686974207468652062756c6c277320657965")
    assert get_xor(buffer1, buffer2) == bytes.fromhex(
        "746865206b696420646f6e277420706c6179")
