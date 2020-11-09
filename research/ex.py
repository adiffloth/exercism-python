"""
Perform Run Length Encoding compression on a string.
"""


def compress(raw: str) -> bytes:
    """
    Compress the raw string to bytes using RLE.
    """
    if not raw:
        return b''

    input_bytes = bytes(raw, 'UTF-8')
    compressed_bytes = bytearray()
    prev_byte = input_bytes[0]
    run = 1
    for byte in bytes(raw, 'UTF-8')[1:]:
        if byte != prev_byte:
            compressed_bytes.append(run)
            compressed_bytes.append(prev_byte)
            prev_byte = byte
            run = 1
        else:
            run += 1
    compressed_bytes.append(run)
    compressed_bytes.append(prev_byte)

    return compressed_bytes


assert compress('abbcccddddaaaaaa') == b'\x01a\x02b\x03c\x04d\x06a'
assert compress('abbcccddddaaaaaat') == b'\x01a\x02b\x03c\x04d\x06a\x01t'
print('Tests passed.')
