text = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

text_hex = bytes.fromhex(text)

print(f"Esta es la cadena hexadecimal a bytes {text_hex}\ny el primer caracter es {text_hex[0]} o sea '{chr(text_hex[0])}'")


key = text_hex[0] ^ ord('c')

print(f"Esta es la key en hexadecimal {hex(key)} lo cual equivale a {key}\n, una vez que tenemos la clave funciona algo asi: 0x73 ^ 0x63 -> c : {chr(key ^ ord('s'))}")
print("Por lo tanto podemos hacer lo mismo con la clave haciendole xor a todo el text_her")
print(f"Flag: {''.join(chr(c^key) for c in text_hex)}")