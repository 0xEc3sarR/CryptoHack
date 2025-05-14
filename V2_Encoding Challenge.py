from pwn import *
import json
import base64
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    requests = json.dumps(hsh).encode()
    r.sendline(requests)

    # types of decodification
def types_encoding(encoding, encoded_value):
    if encoding == "base64":
        return base64.b64decode(encoded_value).decode() # por defecto el decode es utf-8
    elif encoding == "hex":
        return bytes.fromhex(encoded_value).decode() # decodificar de bytes a hexadecimal
    elif encoding == "rot13":
        return codecs.decode(encoded_value, "rot_13")
    elif encoding == "utf-8":
        if isinstance(encoded_value, int):
            return chr(encoded_value)
        return ''.join(chr(num) for num in encoded_value)
    elif encoding == "bigint":
        hex_str = encoded_value[2:] if encoded_value.startswith('0x') else encoded_value
        return bytes.fromhex(hex_str).decode()
    else:
        return


while True:
    received = json_recv()
    # si ya encontramos la flag, rompemos el programa
    if "flag" in received:
        print(f"Flag: {received['flag']}")
        break

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    # empezamos a decodificar los mensajes
    solution = types_encoding(received["type"], received["encoded"])

    json_send({"decoded": solution})



#solution = types_encoding(received["type"], received["encoded"])

#json_send({"decoded": solution})