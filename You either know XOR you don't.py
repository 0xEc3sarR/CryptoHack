from pwn import xor

text = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
text_hex = bytes.fromhex(text)

print(f"Hexadecimal a bytes {text_hex}")

# el ejercicio me dice lo siguiente: Remember the flag format and how it might help you in this challenge!

flag_format = b'crypto{' # tiene 7 bytes, por lo tanto debemos trabajar con los primeros 7 bytes

partial_xor = xor(text_hex[:7], flag_format)

print(f"Observamos que la salida de esto nos da algo muy interesante: {partial_xor}")
print("Lo podemos completar con 'myXORkey' agregandole una 'y' a ver que nos da:")

decrypted = xor(text_hex, b"myXORkey")
print(decrypted.decode())

