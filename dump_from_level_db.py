from binascii import hexlify, unhexlify

import plyvel
# from bitcoin.messages import MsgSerializable
#
# from __future__ import print_function

from bitcoin_tools.analysis.status.utils import b128_decode, deobfuscate_value, \
    parse_ldb

# parse_ldb('coinstats.out', 'coinstats/db/', False)

db = plyvel.DB('coinstats/db/', create_if_missing=False, compression=None)
#
#
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])
#
#
o_key = db.get((unhexlify("0e00") + "obfuscate_key"))
if o_key is not None:
    o_key = hexlify(o_key)[2:]

heights = []
for key, value in db.iterator():
    height = int.from_bytes(key[2:], "big")
    hexed_key = hexlify(key)
    heights.append(height)

    hexed_value = hexlify(value)
    if hexed_value is not None:
        reverse_xor = deobfuscate_value(value=hexed_value, obfuscation_key=o_key)

    decoded_value = b128_decode(hexed_value)
print(decoded_value)

print(min(heights), max(heights))

#
#     string_value = value.decode()
#
#     print(string_key, string_value)
#     # serialized_key = MsgSerializable.from_bytes(key)
#     # serialized_value = MsgSerializable.from_bytes(value)
#     # print(serialized_key, serialized_value)