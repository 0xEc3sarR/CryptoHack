from Crypto.Util.number import *
from pwn import *
import json, codecs

dictionary = {
    "base64": b64d,
    "hex": unhex,
    "rot13": lambda s: codecs.encode(s, "rot_13").encode(),
    "bigint": lambda s: long_to_bytes(int(s, 0)),
    "utf-8": bytes
}

def dec(o):
    return dictionary[o["type"]](o["encoded"])

io = remote("socket.cryptohack.org", 13377)

for _ in range(100):
    o = json.loads(io.recvline())
    io.sendline(json.dumps({"decoded": dec(o).decode()}))

io.interactive()



