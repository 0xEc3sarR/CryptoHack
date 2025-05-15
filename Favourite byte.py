from Crypto.Util.number import *
from pwn import xor

text = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

text_hex = bytes.fromhex(text)

# cada caracter se representa con 1 solo byte, pero ese byte es secreto

print(f"Este es el hexadecimal transformado en bytes: {text_hex}")

# vamos a usar ciclo for para poder probar una decodificacion con cada bytes
# sabemos que los caracteres ascii tienen de 0 a 128 caracteres y probaremos con cada uno de ellos

# tengo un caracter ascii digamos a = 41

print("Hexadecimal transformado de bytes hexadecimales a caracteres ascii")

lista_caracteres = []

def to_asc():
    x = text_hex.decode()
    for c in x:
        a = ord(c)
        lista_caracteres.append(a)
    print(lista_caracteres)

lista_caracteres_xor = []
def try_bytes():
    for i in range(0, 128):
        a = xor(lista_caracteres, i)
        lista_caracteres_xor.append(a)

def decod():
    for i in range(0, 128):
        a = lista_caracteres_xor[i].decode()
        if a.startswith("crypto"):
            print(a)


if __name__ == "__main__":
    to_asc()
    try_bytes()
    decod()
