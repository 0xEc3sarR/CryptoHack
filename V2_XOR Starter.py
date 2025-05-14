from pwn import *

word = 'label'
n = 13

print("crypto{", end='')
result = xor(word, n)

print(result.decode(), end='')
print("}")